import time
from rest_framework import status
import django_filters
from rest_framework import viewsets, generics, permissions
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .models import *
from .serializers import RouteSerializer, LocationSerializer, DetailRouteSerializer, LocationSer, ScheduleListSerializer, ScheduleSerializer, \
    WriteReviewSerializer, ReadReviewSerializer, TicketsSerializer, DetailTicketsSerializer, OrderSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthorOrReadOnly
from ..authorization.models import User


class LocationViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class RoutesFilter(filters.FilterSet):
    source = CharFilterInFilter(field_name='source__nameCode__value', lookup_expr='in')
    destination = CharFilterInFilter(field_name='destination__nameCode__value', lookup_expr='in')

    class Meta:
        model = Route
        fields = ['source','destination']


class TicketFilter(filters.FilterSet):
    source = CharFilterInFilter(field_name='schedule__route__source__nameCode__value', lookup_expr='in')
    destination = CharFilterInFilter(field_name='schedule__route__destination__nameCode__value', lookup_expr='in')
    beginDate = filters.DateTimeFilter(field_name='schedule__beginDate',lookup_expr='gte')
    endDate = filters.DateTimeFilter(field_name='schedule__endDate',lookup_expr='lte')

    class Meta:
        model = Ticket
        fields =['schedule','order']


class RouteViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = RoutesFilter
    queryset = Route.objects.all()
    serializer_class = RouteSerializer

class DetailRouteViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = RoutesFilter
    queryset = Route.objects.all()
    serializer_class = DetailRouteSerializer

class LocationView(generics.RetrieveAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSer
    def get(self,request,*args,**kwargs):
        id = request.data['id']
        language = request.data['language']
        location = Location.objects.get(id = id)
        location_value = ResourceValue.objects.get(nameCode= location.nameCode, language_id= language)
        return Response({
            "location_id" : location.id,
            "locationName" : location_value.value
        })
class PostTicketViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TicketFilter
    serializer_class = TicketsSerializer
    queryset = Ticket.objects.all()

class DetailPostTicketViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = TicketFilter
    serializer_class = DetailTicketsSerializer
    queryset = Ticket.objects.all()
    ordering_fields = ['cost','id','schedule__beginDate','schedule__endDate']

    def retrieve(self, request, *args, **kwargs):
        language_id = kwargs.get('lang_id')
        instance = self.get_object()
        if language_id is not None:
            source_value = ResourceValue.objects.get(language_id=language_id, nameCode= instance.schedule.route.source.nameCode)
            destination_value = ResourceValue.objects.get(language_id=language_id, nameCode=instance.schedule.route.destination.nameCode)
            instance.schedule.route.source.nameCode.value = source_value.value
            instance.schedule.route.destination.nameCode.value = destination_value.value
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
    def list(self, request, *args, **kwargs):
       queryset = self.filter_queryset(self.get_queryset())
       language_id = kwargs.get('lang_id')
       for instance in queryset:
           if language_id is not None:
             source_value = ResourceValue.objects.get(language_id=language_id, nameCode=instance.schedule.route.source.nameCode)
             destination_value = ResourceValue.objects.get(language_id=language_id,nameCode=instance.schedule.route.destination.nameCode)
             instance.schedule.route.source.nameCode.value = source_value.value
             instance.schedule.route.destination.nameCode.value = destination_value.value
       serializer = self.get_serializer(queryset, many=True)
       return Response(serializer.data)

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    def create(self, request):
        ticket_id = request.data['id']
        ticket = Ticket.objects.get(id=ticket_id)
        order = Order.objects.create(schedule= ticket.schedule, user= self.request.user, totalPrice=ticket.cost)
        ticket.order = order
        ticket.save()
        serializer = OrderSerializer(order)
        return Response(serializer.data)
    # def get_permissions(self):
    #     if self.action in ("create",):
    #         self.permission_classes = (permissions.IsAuthenticated,)

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()

    def list(self, request):
        tour_id = request.data['id']
        queryset = Review.objects.filter(tour= tour_id)
        serializer = ReadReviewSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        pass

    def get_serializer_class(self):
        if self.action in ("create", "update", "partial_update", "destroy"):
            return WriteReviewSerializer
        return ReadReviewSerializer
    def get_permissions(self):
        if self.action in ("create",):
            self.permission_classes = (permissions.IsAuthenticated,)
        elif self.action in ("update", "partial_update", "destroy"):
            self.permission_classes = (IsAuthorOrReadOnly)
        else:
            self.permission_classes = (permissions.AllowAny,)

        return super().get_permissions()




class ScheduleFilterSet(filters.FilterSet):
    class Meta:
        model = Schedule
        fields = {
            'beginDate': ['gt', 'lt', 'exact'],
            'isActive': ['exact'],
            'scheduleType': ['exact']
        }

class ScheduleViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated,]
    queryset = Schedule.objects.all()
    


    def create(self, request, *args, **kwargs):
        print(request.data)
        serializer = ScheduleListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            
            fromDate = serializer.validated_data['fromDate']
            toDate = serializer.validated_data['toDate']
            lanugage_id = serializer.validated_data['language_id']

            filtered_data = self.queryset.filter(beginDate__range=(fromDate, toDate), scheduleType__id=serializer.validated_data['scheduleType'])

            result = ScheduleSerializer(filtered_data, many=True, context={'language_id': lanugage_id})
            
            
            return Response(result.data, status=status.HTTP_200_OK)
        # print(serialized_data)

        return Response('nice', status=status.HTTP_200_OK)

