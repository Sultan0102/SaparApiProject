import time
import datetime
import pytz
import django_filters
from rest_framework import viewsets, generics, permissions, status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .models import *
from Core.authorization.models import Driver
from Core.exceptions import ValidationAPIException

from .serializers import CachedTicketPersonSerializer, PassportNumberTypeSerializer, \
    RouteSerializer, LocationSerializer, DetailRouteSerializer, LocationSer, ScheduleListSerializer, \
    ScheduleSerializer, TicketPersonSerializer, UpdateTicketSerializer, \
    WriteReviewSerializer, ReadReviewSerializer, TicketsSerializer, DetailTicketsSerializer, OrderSerializer, RouteQuerySerializer, \
    TouristTourSerializer, ScheduleRouteSerializer, ResourceCodeSerializer, BusSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated, AllowAny
from .permissions import IsAuthorOrReadOnly
from ..applications.models import Document, Application
from ..applications.serializers import DocumentsViewSetSerializer, ApplicationDriverSerializer, \
    ApplicationSerializerRetrieve, ScheduleDriverSerializer
from ..authorization.models import User
from rest_framework.decorators import action
import Core.validators
from django.db.transaction import atomic


class LocationViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class BusViewSet(viewsets.ModelViewSet):
    http_method_names=['get']
    queryset = Bus.objects.all()
    serializer_class = BusSerializer


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
    # filter_backends = (DjangoFilterBackend,)
    # filterset_class = RoutesFilter
    queryset = Route.objects.all()
    serializer_class = RouteSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        langId = self.request.data.get('languageId', None)
        if langId:
            context.update({"languageId": self.request.data['languageId']})
        return context


    @action(detail=False, methods=['post'], url_path='order/(?P<order_pk>[^/.]+)')
    def getRoutesByOrder(self, request, order_pk):
        if order_pk is None or Core.validators.validate_any(order_pk, '^[0-9]+$') == False:
            print('Error')
            return Response('Error', status=status.HTTP_400_BAD_REQUEST)
        order = Order.objects.get(id=order_pk)
        print(order.schedule.route.id)
        serializer = self.get_serializer(order.schedule.route)
        # serializer.is_valid(raise_exception=True);
        print(serializer.data)



        return Response(serializer.data, status=status.HTTP_200_OK);



class DetailRouteViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = RoutesFilter
    queryset = Route.objects.all()
    # serializer_class = DetailRouteSerializer

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
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, ]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        depth = 0
        try:
            depth = int(self.request.query_params.get('depth', 0))
        except ValueError:
            pass # Ignore non-numeric parameters and keep default 0 depth

        context['depth'] = depth

        return context

    def get_queryset(self):
        query_set = super().get_queryset();
        if self.request.user:
            query_set = Order.objects.filter(user=self.request.user)
        return query_set

    def create(self, request):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.data)
    # def get_permissions(self):
    #     if self.action in ("create",):
    #         self.permission_classes = [permissions.IsAuthenticated,]

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


class ScheduleDriverViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = Schedule.objects.all()

    def list(self, request):
        # driver = request.data['driver_id']
        # queryset = Schedule.objects.filter(driver= driver)
        queryset = Schedule.objects.all()
        serializer = ScheduleDriverSerializer(queryset, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def retrieve(self, request, pk=None, *args, **kwargs):
        queryset = Schedule.objects.filter(driver=pk)
        language_id = kwargs.get('lang_id')
        for instance in queryset:
            if language_id is not None:
                source_value = ResourceValue.objects.get(language_id=language_id,code=instance.route.source.nameCode)
                destination_value = ResourceValue.objects.get(language_id=language_id,code=instance.route.destination.nameCode)
                instance.route.source.nameCode.defaultValue = source_value.value
                instance.route.destination.nameCode.defaultValue = destination_value.value
        serializer = ScheduleDriverSerializer(queryset, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        print(request.data)
        serializer = ScheduleListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            fromDate = serializer.validated_data['fromDate']
            toDate = serializer.validated_data['toDate']
            lanugage_id = serializer.validated_data['language_id']

            filtered_data = self.queryset.filter(beginDate__range=(fromDate, toDate),
                                                 scheduleType__id=serializer.validated_data['scheduleType'])

            result = ScheduleSerializer(filtered_data, many=True, context={'language_id': lanugage_id})

            return Response(result.data, status=status.HTTP_200_OK)
        # print(serialized_data)
        return Response('No data', status=status.HTTP_204_NO_CONTENT)




class ScheduleFilterSet(filters.FilterSet):
    class Meta:
        model = Schedule
        fields = {
            'beginDate': ['gt', 'lt', 'exact'],
            'isActive': ['exact'],
            'scheduleType': ['exact']
        }

class ScheduleViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated,]
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

    def create(self, request, *args, **kwargs):
        print(request.data)
        serializer = ScheduleListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            fromDate = serializer.validated_data['fromDate']
            toDate = serializer.validated_data['toDate']
            lanugage_id = serializer.validated_data['language_id']
            isActive = request.data.get('isActive')
            locationType = 1 if serializer.validated_data['scheduleType'] == 1 else 2
            destination = request.data.get('destination')
            source = request.data.get('source')


            print(isActive)

            if toDate is None:
                toDate = '9999-12-31T00:00:00'

            filtered_data = self.queryset.filter(beginDate__range=(fromDate, toDate))
            filtered_data = filtered_data.filter(scheduleType__id=serializer.validated_data['scheduleType'])
            if isActive is not None:
                filtered_data = filtered_data.filter(isActive=isActive)

            if destination is not None and len(destination) > 0:
                print('Destination:', destination, sep=' ')
                destinationResourceCodeSet = set()
                [destinationResourceCodeSet.add(i.code.id) for i in ResourceValue.objects.filter(value__icontains=destination) ]
                filtered_data = filtered_data.filter(route__destination__nameCode__id__in=destinationResourceCodeSet).filter(route__destination__type__id=locationType)

            if source is not None and len(source) > 0:
                print('Source:', source, sep=' ')
                sourceResourceCodeSet = set()
                [sourceResourceCodeSet.add(i.code.id) for i in ResourceValue.objects.filter(value__icontains=source) ]
                filtered_data = filtered_data.filter(route__source__nameCode__id__in=sourceResourceCodeSet).filter(route__source__type__id=locationType)


            print(filtered_data)
            result = ScheduleSerializer(filtered_data, many=True, context={'language_id': lanugage_id})

            return Response(result.data, status=status.HTTP_200_OK)
        # print(serialized_data)

        return Response('No data', status=status.HTTP_204_NO_CONTENT)
    
    def validateCreateIntercityScheduleRequest(self, schedule):
        if schedule['weekDays'] is None or len(schedule['weekDays'])==0:
            raise ValidationAPIException('No week days provided!')
        
        if schedule['source'] is None:
            raise ValidationAPIException('No source provided!')
        
        if schedule['destination'] is None:
            raise ValidationAPIException('No destination provided!')
        
        if schedule['beginTime'] is None:
            raise ValidationAPIException('No begin time provided!')
        
        if schedule['endTime'] is None:
            raise ValidationAPIException('No end time provided!')
        
        if schedule['driver'] is not None:
            try:
                User.objects.get(id=schedule['driver'], role=5)
            except Driver.DoesNotExist:
                raise ValidationAPIException('Driver with such id does not exist')
        
        if schedule['bus'] is not None:
            try:
                Bus.objects.get(id=schedule['bus'])
            except Driver.DoesNotExist:
                raise ValidationAPIException('Bus with such id does not exist')
            

    def createOrGetRoute(self, source, destination):
        sourceLocation = Location.objects.get(id=source, type_id=1)
        destinationLocation = Location.objects.get(id=destination, type_id=1)

        route = Route.objects.filter(source=sourceLocation, destination=destinationLocation).filter().first()
        if route is None:
            route = Route.objects.create(source=sourceLocation, destination=destinationLocation);
        print("Route ID: ", route.id, sep=' ')

        return route
    
    @atomic
    @action(detail=False, methods=['post'], url_path='intercity')
    def createIntercitySchedule(self, request):
        scheduleRequest = {
            'weekDays': request.data.get('weekDays', None),
            'source': request.data.get('source', None),
            'destination': request.data.get('destination', None),
            'driver': request.data.get('driver', None),
            'bus': request.data.get('bus', None),
            'beginTime': request.data.get('beginTime', None),
            'endTime': request.data.get('endTime', None),
        }

        self.validateCreateIntercityScheduleRequest(scheduleRequest)
        
        route = self.createOrGetRoute(scheduleRequest['source'], scheduleRequest['destination']);

        current_date = datetime.date.today()
        delta = datetime.timedelta(days=1)
        # weekDays in python: Monday is 0 and Sunday is 6
        for i in range(1, 8):
            current_date+=delta
            if current_date.weekday() + 1 in scheduleRequest['weekDays']:
                beginTime = datetime.time(*[int(j) for j in scheduleRequest['beginTime'].split(':')])
                endTime = datetime.time(*[int(j) for j in scheduleRequest['endTime'].split(':')])

                beginDate = pytz.timezone('Asia/Almaty').localize(datetime.datetime.combine(current_date, beginTime))
                if endTime < beginTime:
                    endDate = pytz.timezone('Asia/Almaty').localize(datetime.datetime.combine(current_date+delta, endTime))
                else:
                    endDate = pytz.timezone('Asia/Almaty').localize(datetime.datetime.combine(current_date, endTime))
                schedule = {
                    'scheduleNumber': Schedule.generateScheduleNumber(),
                    'route': route,
                    'weekDay': current_date.weekday() + 1,
                    'beginDate': beginDate,
                    'endDate': endDate,
                    'isActive': False,
                    'scheduleType_id': 1,
                }

                if scheduleRequest['bus']:
                    schedule['bus_id'] = scheduleRequest['bus']
                if scheduleRequest['driver']:
                    schedule['driver_id'] = scheduleRequest['driver']

                schedule = Schedule.objects.create(**schedule)
        
        return Response('created', status=status.HTTP_200_OK)
    
    def validateUpdateIntercityScheduleRequest(self, schedule):
        if schedule['id'] is None:
            raise ValidationAPIException('No id provided!')
        
        if schedule['source'] is None:
            raise ValidationAPIException('No source provided!')
        
        if schedule['destination'] is None:
            raise ValidationAPIException('No destination provided!')
        
        if schedule['beginTime'] is None:
            raise ValidationAPIException('No begin time provided!')
        
        if schedule['endTime'] is None:
            raise ValidationAPIException('No end time provided!')
        
        if schedule['disabled'] is None:
            raise ValidationAPIException('No "disabled" flag provided!')
        
        if schedule['disabled'] == False:
            if schedule['driver'] is None:
                raise ValidationAPIException('No driver provided!')
        
            if schedule['bus'] is None:
                raise ValidationAPIException('No bus provided!')
            
            try:
                User.objects.get(id=schedule['driver'], role=5)
            except Driver.DoesNotExist:
                raise ValidationAPIException('Driver with such id does not exist')
            
            try:
                Bus.objects.get(id=schedule['bus'])
            except Driver.DoesNotExist:
                raise ValidationAPIException('Bus with such id does not exist')

    @atomic
    @action(detail=False, methods=['post'], url_path='intercity/update')
    def updateIntercitySchedule(self, request):
        scheduleRequest = {
            "id": request.data.get('scheduleId', None),
            "source": request.data.get('source', None),
            "destination": request.data.get('destination', None),
            "bus": request.data.get('bus', None),
            "driver": request.data.get('driver', None),
            "weekDay": request.data.get('weekDay', None),
            "beginTime": request.data.get('beginTime', None),
            "endTime": request.data.get('endTime', None),
            "disabled": request.data.get('disabled', None),
        }

        self.validateUpdateIntercityScheduleRequest(scheduleRequest)

        route = self.createOrGetRoute(scheduleRequest['source'], scheduleRequest['destination']);
        bus = Bus.objects.filter(id=scheduleRequest['bus']).first()
        driver = User.objects.filter(id=scheduleRequest['driver']).first()
        weekDay = scheduleRequest['weekDay']
        beginTime = datetime.time(*[int(j) for j in scheduleRequest['beginTime'].split(':')])
        endTime = datetime.time(*[int(j) for j in scheduleRequest['endTime'].split(':')])

        schedule = Schedule.objects.get(id=scheduleRequest['id'])

        print(driver)
        print(bus)
        schedule.bus = bus if bus is not None else schedule.bus
        schedule.driver = driver if driver is not None else schedule.driver
        schedule.route = route
        schedule.beginDate = schedule.beginDate.replace(hour=beginTime.hour, minute=beginTime.minute)
        schedule.endDate = schedule.endDate.replace(hour=endTime.hour, minute=endTime.minute)

        if scheduleRequest['disabled'] is False:
            tickets = Ticket.objects.filter(schedule_id=schedule.id)
            
            if(len(tickets) == 0):
                #create tickets
                for seatNumber in range(1, schedule.bus.type.capacity+1):
                    ticket = {
                        'seatNumber': seatNumber,
                        'cost': 4000,
                        'schedule_id': schedule.id,
                        'status_id': 3,
                        'type_id': 1
                    }
                    Ticket.objects.create(**ticket)
        
        schedule.isActive = scheduleRequest['disabled'] is False
        schedule.save()
        
        return Response('success', status=status.HTTP_200_OK)




        

    




class TicketPersonViewSet(viewsets.ModelViewSet):
    queryset = TicketPerson.objects.all()
    serializer_class = TicketPersonSerializer
    permission_classes = [IsAuthenticated, ]
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            result = serializer.save()
            result['passportNumberType'] = result['passportNumberType'].id

            return Response(result, status=status.HTTP_201_CREATED)

        return Response('Validation Error', status=status.HTTP_400_BAD_REQUEST)

class CachedTicketPersonViewSet(viewsets.ModelViewSet):
    queryset = CachedTicketPerson.objects.all()
    serializer_class = CachedTicketPersonSerializer
    permission_classes = [IsAuthenticated, ]
    http_method_names = ['post', 'get']


    def create(self, request):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response("Validation error", status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        print(args)
        print(kwargs)

        userId = request.GET['userId']
        if userId:
            # self.queryset = self.get_queryset().filter(userId == userId)
            self.queryset = self.queryset.filter(user__id=userId)

        return super().list(request, *args, **kwargs)


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = UpdateTicketSerializer
    permission_classes = [IsAuthenticated, ]
    # http_method_names = ['put']

    def update(self, request, pk):
        request.data['id'] = pk;
        print("REquest datra")
        print(request.data)
        serializer = self.get_serializer(data=request.data, partial=True)

        if serializer.is_valid(raise_exception=True):
            result = serializer.save()
            return Response('success', status=status.HTTP_200_OK)


class PassportNumberTypeViewSet(viewsets.ModelViewSet):
    queryset = PassportNumberType.objects.all()
    serializer_class = PassportNumberTypeSerializer
    permission_classes = [IsAuthenticated, ]


class TouristTourViewSet(viewsets.ModelViewSet):
    queryset = TouristTour.objects.all()
    serializer_class = TouristTourSerializer
    permission_classes = [IsAuthenticated, ]
    currentLanguageId = 3

    def createOrGetRoute(self, sourceValue, destinationValue):
        sourceLocation = self.createOrGetLocationByName(sourceValue)
        destinationLocation = self.createOrGetLocationByName(destinationValue)

        route = Route.objects.filter(source=sourceLocation, destination=destinationLocation).filter().first()
        if route is None:
            route = Route.objects.create(source=sourceLocation, destination=destinationLocation);
        print("Route ID: ", route.id, sep=' ')

        return route

    def createOrGetLocationByName(self, value):
        resourceValue = ResourceValue.objects.filter(value__icontains=value, language__id=self.currentLanguageId).first()
        if resourceValue is None:
            resourceCode = ResourceCode.objects.filter(defaultValue__icontains=value).first()

            if resourceCode is None:
                resourceCode = ResourceCode.objects.create(defaultValue=value)

            resourceValue = ResourceValue.objects.create(value=value, language_id=self.currentLanguageId, code_id=resourceCode.id)

        location = Location.objects.filter(nameCode__id=resourceValue.code.id, type__id=2).first()

        if location is None:
            location = Location.objects.create(nameCode_id=resourceValue.code.id, type_id=2) #2 - LocationType for TouristPlace


        return location

    def createResourceCode(self, value):
        code = ResourceCode.objects.create(defaultValue=value)
        ResourceValue.objects.create(value=value, code_id=code.id, language_id=self.currentLanguageId)
        return code

    def get_queryset(self):
        user = self.request.user
        queryset = super().get_queryset()
        if user.role == User.BUSINESS_PERSON:
            queryset = queryset.filter(owner_id=user.id)

        non_deleted = self.request.query_params.get('non_deleted');
        print(non_deleted)

        if non_deleted and str.upper(non_deleted)=="TRUE":
            queryset = queryset.filter(deletedDate=None)


        return queryset

    @action(detail=False, methods=['post'], url_path='schedule')
    def getTourByScheduleId(self, request):
        print('Endpoint')
        scheduleId = request.data.get('scheduleId', None)
        if scheduleId is None:
            raise ValidationAPIException(detail="Schedule id not supplied")
        tour = TouristTour.objects.filter(schedules__in=[scheduleId]).first()
        # tour.schedules = tour.schedules.filter(id=scheduleId)
        tour.schedules.set([tour.schedules.get(id=scheduleId)])

        language_id = request.data.get('languageId')
        print(request.data)
        context = {}
        if language_id:
            context['language_id'] = language_id
        descriptionCodeSerializer = ResourceCodeSerializer(tour.descriptionNameCode)
        context['description'] = descriptionCodeSerializer.data
        serializer = TouristTourSerializer(tour, context=context)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @atomic
    def create(self, request):
        self.currentLanguageId = request.data['languageId']
        destinationValue = request.data['destination']
        sourceValue = request.data['source']
        route = self.createOrGetRoute(sourceValue, destinationValue);
        titleNameCode = self.createResourceCode(request.data['title'])
        descriptionNameCode = self.createResourceCode(request.data['description'])

        newTour = {
            'titleNameCode': titleNameCode.id,
            'descriptionNameCode': descriptionNameCode.id,
            'price': request.data['price'],
            'owner': request.data['owner'],
        }

        serializer = self.get_serializer(data=newTour)
        serializer.is_valid(raise_exception=True)
        newTour = serializer.save();


        current_date = datetime.date.today()
        delta = datetime.timedelta(days=1)
        # weekDays in python: Monday is 0 and Sunday is 6
        for i in range(1, 15):
            current_date+=delta
            if current_date.weekday() + 1 in request.data['weekDays']:
                beginTime = datetime.time(*[int(j) for j in request.data['beginTime'].split(':')])
                endTime = datetime.time(*[int(j) for j in request.data['endTime'].split(':')])

                beginDate = pytz.timezone('Asia/Almaty').localize(datetime.datetime.combine(current_date, beginTime))
                if endTime < beginTime:
                    endDate = pytz.timezone('Asia/Almaty').localize(datetime.datetime.combine(current_date+delta, endTime))
                else:
                    endDate = pytz.timezone('Asia/Almaty').localize(datetime.datetime.combine(current_date, endTime))
                schedule = {
                    'scheduleNumber': Schedule.generateScheduleNumber(),
                    'route': route,
                    'weekDay': current_date.weekday() + 1,
                    'beginDate': beginDate,
                    'endDate': endDate,
                    'isActive': False,
                    'scheduleType_id': 2
                }


                schedule = Schedule.objects.create(**schedule)
                newTour.schedules.add(schedule)

        newTour.save();


        return Response('create', status=status.HTTP_201_CREATED);

