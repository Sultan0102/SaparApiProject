from rest_framework import serializers
from .models import *
from .. import validators
from ..exceptions import InvalidPassportNumberException


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id','coordinates', 'nameCode']

    def __init__(self,*args,**kwargs):
        super(LocationSerializer, self).__init__(*args,**kwargs)
        self.Meta.depth = 1


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ['id','destination','source','duration','distance']


class DetailRouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ['id','destination','source','duration','distance']

    def __init__(self,*args,**kwargs):
        super(DetailRouteSerializer, self).__init__(*args,**kwargs)
        self.Meta.depth = 2


class TicketsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['id','type','schedule','seatNum','cost','status','created','updated','person','order']
        read_only_field = ['created','updated']


class DetailTicketsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['id','type','schedule','seatNum','cost','status','created','updated','person','order']
        read_only_field = ['created','updated']

    def __init__(self,*args,**kwargs):
        super(DetailTicketsSerializer, self).__init__(*args,**kwargs)
        self.Meta.depth = 4

class LocationSer(serializers.Serializer):
    id = serializers.IntegerField
    language = serializers.IntegerField

class ReadReviewSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField()

    def get_author_name(self, review):
        return f"{review.author.firstName} {review.author.lastName}"

    class Meta:
        model = Review
        fields = ('id', 'author_name', 'tour', 'text', 'created_date')
class WriteReviewSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Review
        fields = ('id', 'author', 'tour', 'text', 'created_date')

class OrderSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Order
        fields = ('id','user','schedule','totalPrice','creationDate','isPaid')

class PassportNumberTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PassportNumberType
        fields = ('__all__')
class TicketPersonSerializer(serializers.ModelSerializer):
    passportNumberType = PassportNumberTypeSerializer
    class Meta:
        model = TicketPerson
        fields = ('__all__')

    def validate_passportNumber(self,value):
        passNumb = self.data['passportNumberType']
        if passNumb == 5:
            if validators.validate_passport_identation(value) == False:
                raise InvalidPassportNumberException
            return value
        if passNumb == 6:
            if validators.validate_passport_kz_passport(value) == False:
                raise InvalidPassportNumberException
            return value

class ScheduleTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['id', 'seatNumber', 'cost', 'status']


class ScheduleRouteSerializer(serializers.ModelSerializer):
    destinationName = serializers.SerializerMethodField('get_destination_name')
    sourceName = serializers.SerializerMethodField('get_source_name')


    def get_destination_name(self, obj):
        lang_id = self.context.get('language_id') if self.context.get('language_id') is not None else 1

        name = ResourceValue.objects.filter(code_id = obj.destination.nameCode.id, language_id=lang_id)[0].value
        return name;

    def get_source_name(self, obj):
        lang_id = self.context.get('language_id') if self.context.get('language_id') is not None else 1
        name = ResourceValue.objects.filter(code_id = obj.source.nameCode.id, language_id=lang_id)[0].value
        return name;

    class Meta:
        model = Route
        fields = ['id','destination','source','duration','distance', 'destinationName', 'sourceName']
        depth=1


class ScheduleSerializer(serializers.ModelSerializer):
    route = ScheduleRouteSerializer()
    tickets = serializers.SerializerMethodField()

    def get_tickets(self, obj):
        print(obj.id)
        tickets = ScheduleTicketSerializer(data=Ticket.objects.filter(schedule=obj.id).order_by('seatNumber'), many=True)
        tickets.is_valid()

        return tickets.data;

    class Meta:
        model = Schedule
        fields = ['id', 'scheduleNumber', 'beginDate', 'endDate', 'bus', 'driver', 'route', 'scheduleType', 'tickets']
        read_only_fields = ('language_id', )
        depth=2
class ScheduleListSerializer(serializers.Serializer):
    fromDate = serializers.DateTimeField()
    toDate = serializers.DateTimeField()
    language_id = serializers.IntegerField(min_value=1, max_value=3)
    scheduleType = serializers.IntegerField(min_value=1)

class ScheduleDriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ('__all__')
        read_only_fields = ('language_id', )

    def __init__(self,*args,**kwargs):
        super(ScheduleDriverSerializer, self).__init__(*args,**kwargs)
        self.Meta.depth = 3

class ApplicationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')

class ApplicationSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    status = serializers.HiddenField(default=ApplicationStatus.objects.first())
    class Meta:
        model = Application
        fields = ('__all__')

    def __init__(self, *args, **kwargs):
        if kwargs.get('context', {}).get('request', {}).method == 'GET':
            self.Meta.depth = 1

        super(ApplicationSerializer, self).__init__(*args, **kwargs)

class ApplicationSerializerRetrieve(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ('__all__')

    def __init__(self, *args, **kwargs):
        super(ApplicationSerializerRetrieve, self).__init__(*args, **kwargs)
        self.Meta.depth = 1

class DocumentsViewSetSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault(),
    )
    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user
        return super().create(validated_data)
    class Meta:
        model = Documents
        fields = ('__all__')