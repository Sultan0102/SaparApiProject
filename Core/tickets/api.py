import django_filters
from rest_framework import viewsets, generics, permissions
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .models import *
from .serializers import PostTicketsSerializer, RouteSerializer, LocationSerializer, DetailPostTicketsSerializer, \
    DetailRouteSerializer, LocationSer, WriteReviewSerializer, ReadReviewSerializer
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
    source = CharFilterInFilter(field_name='route__source__nameCode__value', lookup_expr='in')
    destination = CharFilterInFilter(field_name='route__destination__nameCode__value', lookup_expr='in')
    beginDate = filters.DateTimeFilter(field_name='order__schedule__beginDate',lookup_expr='gte')
    endDate = filters.DateTimeFilter(field_name='order__schedule__endDate',lookup_expr='lte')

    class Meta:
        model = PostTicket
        fields =['route','order']


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
    serializer_class = PostTicketsSerializer
    queryset = PostTicket.objects.all()

class DetailPostTicketViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = TicketFilter
    serializer_class = DetailPostTicketsSerializer
    queryset = PostTicket.objects.all()
    ordering_fields = ['cost','id','order__schedule__beginDate','order_schedule_endDate']

    def retrieve(self, request, *args, **kwargs):
        language_id = kwargs.get('lang_id')
        instance = self.get_object()
        if language_id is not None:
            source_value = ResourceValue.objects.get(language_id=language_id, nameCode= instance.route.source.nameCode)
            destination_value = ResourceValue.objects.get(language_id=language_id, nameCode=instance.route.destination.nameCode)
            instance.route.source.nameCode.value = source_value.value
            instance.route.destination.nameCode.value = destination_value.value
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    def list(self, request, *args, **kwargs):
       queryset = self.filter_queryset(self.get_queryset())
       language_id = kwargs.get('lang_id')
       for instance in queryset:
           if language_id is not None:
             source_value = ResourceValue.objects.get(language_id=language_id, nameCode=instance.route.source.nameCode)
             destination_value = ResourceValue.objects.get(language_id=language_id,nameCode=instance.route.destination.nameCode)
             instance.route.source.nameCode.value = source_value.value
             instance.route.destination.nameCode.value = destination_value.value
       serializer = self.get_serializer(queryset, many=True)
       return Response(serializer.data)

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

