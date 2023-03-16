from rest_framework import serializers

from Core.exceptions import ValidationAPIException
from Core.validators import validate_passportType
from .models import *
from django.core.exceptions import ObjectDoesNotExist


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

class ScheduleListSerializer(serializers.Serializer):
    fromDate = serializers.DateTimeField()
    toDate = serializers.DateTimeField()
    language_id = serializers.IntegerField(min_value=1, max_value=3)
    scheduleType = serializers.IntegerField(min_value=1)

class ResourceValueSerializer(serializers.ModelSerializer):

    class Meta:
        model = ResourceValue
        fields = ['id', 'value', 'code', 'language']

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


class ScheduleTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['id', 'seatNumber', 'cost', 'status']

class ScheduleSerializer(serializers.ModelSerializer):
    route = ScheduleRouteSerializer()
    tickets = serializers.SerializerMethodField()

    def get_tickets(self, obj):
        print(obj.id)
        tickets = ScheduleTicketSerializer(data=Ticket.objects.filter(schedule=obj.id), many=True)
        tickets.is_valid()

        return tickets.data;

    class Meta:
        model = Schedule
        fields = ['id', 'scheduleNumber', 'beginDate', 'endDate', 'bus', 'driver', 'route', 'scheduleType', 'tickets']
        read_only_fields = ('language_id', )
        depth=2

class PassportNumberTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = PassportNumberType
        fields = '__all__' 

class TicketPersonSerializer(serializers.ModelSerializer):

    ticketId = serializers.IntegerField(min_value=1)

    class Meta:
        model = TicketPerson
        fields = ['firstName', 'lastName', 'secondName', 'passportNumber', 'passportNumberType', 'ticketId']
    

    def validate(self, data):
        try:
            passNumberType = data['passportNumberType']
            if validate_passportType(data['passportNumber'], passNumberType.format) == False:
                raise ValidationAPIException(detail="Invalid passport number format!", code="invalid_passport_number_format")

        except ObjectDoesNotExist as e:
            raise ValidationAPIException(detail="Invalid passport number type!", code="invalid_passport_number_type",)

        return data

    def create(self, validated_data):

        try:
            
            ticketPerson = TicketPerson(
                firstName=validated_data['firstName'],
                lastName=validated_data['lastName'],
                secondName=validated_data['secondName'],
                passportNumber=validated_data['passportNumber'],
                passportNumberType=validated_data['passportNumberType'],
            );
            ticketPerson.save()

        except Exception as e:
            print("Error Creating Ticket PErson")
            raise e
        
        print("Ticket Person: ")
        print(ticketPerson.id)
        try:
            ticketId = validated_data['ticketId']
            print(ticketId)
            ticket = Ticket.objects.get(id=ticketId)
            ticket.person=ticketPerson
            ticket.save()

        except ObjectDoesNotExist as e:
            raise ValidationAPIException("No such Ticket")
        except Exception as e:
            print(e)
            raise Exception("Error binding ticket to ticket Person")

        return validated_data