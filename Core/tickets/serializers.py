from rest_framework import serializers
from Core.exceptions import FailedToCreateOrder, ValidationAPIException
from Core.validators import validate_passportType
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from django.db.transaction import atomic
from Core.authorization.serializers import UserSerializer

class ResourceValueByLanguageSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        langId = self.context.get('languageId', 0)

        if langId != 0:
            data = data.filter(language__id=langId)

        return super(ResourceValueByLanguageSerializer, self).to_representation(data)

class ResourceValueSerializer(serializers.ModelSerializer):

    class Meta:
        model = ResourceValue
        list_serializer_class=ResourceValueByLanguageSerializer
        fields = '__all__'
class ResourceCodeSerializer(serializers.ModelSerializer):
    codeResourceValues = ResourceValueSerializer(many=True)

    class Meta:
        model = ResourceCode
        fields = ['id', 'defaultValue', 'codeResourceValues']
    def create(self, validated_data):
        resourceValues_data = validated_data.pop('codeResourceValues')
        code = ResourceCode.objects.create(**validated_data)
        for resourceValue in resourceValues_data:
            ResourceValue.objects.create(code=code, **resourceValue)
        return code


class LocationSerializer(serializers.ModelSerializer):
    nameCode = ResourceCodeSerializer()

    class Meta:
        model = Location
        fields = ['id','coordinates', 'nameCode', 'type']

    def __init__(self,*args,**kwargs):
        super(LocationSerializer, self).__init__(*args,**kwargs)
        self.Meta.depth = 1


class RouteSerializer(serializers.ModelSerializer):
    source = LocationSerializer()
    destination = LocationSerializer()

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


class RouteQuerySerializer(serializers.Serializer):
    route = RouteSerializer()



class ScheduleListSerializer(serializers.Serializer):
    fromDate = serializers.DateTimeField()
    toDate = serializers.DateTimeField(allow_null=True)
    language_id = serializers.IntegerField(min_value=1, max_value=3)
    scheduleType = serializers.IntegerField(min_value=1)


class ScheduleRouteSerializer(serializers.ModelSerializer):
    destinationName = serializers.SerializerMethodField('get_destination_name')
    sourceName = serializers.SerializerMethodField('get_source_name')


    def get_destination_name(self, obj):
        lang_id = self.context.get('language_id') if self.context.get('language_id') is not None else 1

        name = ResourceValue.objects.filter(code_id = obj.destination.nameCode.id, language_id=lang_id).first()
        if name is None:
            name = obj.destination.nameCode.defaultValue
        else:
            name = name.value
            
        return name;

    def get_source_name(self, obj):
        lang_id = self.context.get('language_id') if self.context.get('language_id') is not None else 1
        name = ResourceValue.objects.filter(code_id = obj.source.nameCode.id, language_id=lang_id).first()
        if name is None:
            name = obj.source.nameCode.defaultValue
        else:
            name = name.value 
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
        tickets = ScheduleTicketSerializer(data=Ticket.objects.filter(schedule=obj.id).order_by('seatNumber'), many=True)
        tickets.is_valid()

        return tickets.data;

    class Meta:
        model = Schedule
        fields = ['id', 'scheduleNumber', 'beginDate', 'endDate', 'bus', 'driver', 'route', 'scheduleType', 'tickets', 'tours']
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
        fields = ['id', 'firstName', 'lastName', 'secondName', 'passportNumber', 'passportNumberType', 'ticketId']
        read_only_fields = ['id']


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
            validated_data['id'] = ticketPerson.id

        except Exception as e:
            print("Error Creating Ticket Person")
            raise e

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

class CachedTicketPersonSerializer(serializers.ModelSerializer):
    cachedPersonId = serializers.IntegerField(min_value=0, write_only=True)

    class Meta:
        model = CachedTicketPerson
        fields = ['id', 'firstName', 'lastName', 'secondName', 'passportNumber', 'passportNumberType', 'user', 'cachedPersonId']
        read_only_fields= ['id']
        extra_kwargs = {
            'user': {'write_only': True},
        }

    def validate(self, obj):
        if validate_passportType(obj['passportNumber'], obj['passportNumberType'].format) == False:
            raise ValidationAPIException(detail="Invalid passport number type!", code="invalid_passport_number_type",)

        return obj

    def save(self):
        if self.validated_data['cachedPersonId'] != 0:
            #update
            person = CachedTicketPerson.objects.get(id=self.validated_data['cachedPersonId'])
            person.firstName = self.validated_data['firstName']
            person.lastName = self.validated_data['lastName']
            person.secondName = self.validated_data['secondName']
            person.passportNumberType = self.validated_data['passportNumberType']
            person.passportNumber = self.validated_data['passportNumber']
            person.save();
        else:
            self._validated_data.pop('cachedPersonId')
            return self.create(self.validated_data)


        return self.validated_data




class OrderTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'
        depth=0

class OrderSerializer(serializers.ModelSerializer):
    ticket_ids = serializers.ListField(child=serializers.IntegerField(), write_only=True)
    tickets = serializers.SerializerMethodField('get_tickets')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.Meta.depth = self.context.get('depth', 0)

    def get_tickets(self, obj):
        if obj.id is None:
            return []

        serializer = OrderTicketSerializer(data=Ticket.objects.filter(order__id = obj.id), many=True)
        serializer.is_valid()

        return serializer.data



    class Meta:
        model = Order
        fields = ['id', 'user', 'schedule', 'totalPrice', 'ticket_ids', 'isPaid', 'tickets']
        read_only_fields=['id', 'totalPrice', 'isPaid', 'tickets']
        depth=0

    def validate_ticket_ids(self, value):

        if len(value) == 0:
            raise ValidationAPIException("cannot create order without ticket ids!")

        return value

    @atomic
    def create(self, validated_data):
        tickets = Ticket.objects.filter(id__in=validated_data['ticket_ids'])
        print(tickets)
        order_data = {
            'user': validated_data['user'],
            'schedule': validated_data['schedule'],
            'totalPrice': sum(i.cost for i in tickets),
            'isPaid': False
        }

        try:
            order = Order.objects.create(**order_data);
            print(order_data)
            tickets.update(status_id=1, order_id=order.id)

        except Exception as e:
            print("Could not create an order")
            raise FailedToCreateOrder()

        return order


class UpdateTicketSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Ticket
        fields = ['id', 'person']

    #update
    def save(self):
        print(self.validated_data)
        ticketId = self.validated_data['id']
        person = TicketPerson.objects.get(id=self.validated_data['person'].id)

        try:
            ticket = Ticket.objects.get(id=ticketId)
        except ObjectDoesNotExist as e:
            raise ValidationAPIException("No such tiket!")

        ticket.person = person

        try:
            ticket.save()
        except Exception as e:
            print("Error updating ticket person")

        return ticket


class GuideSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Guide
        fields = ['id', 'user', 'serviceRating']
        read_only_fields=['id']

class TourScheduleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Schedule

class TouristTourSerializer(serializers.ModelSerializer):
    schedules = ScheduleSerializer(read_only=True, many=True)
    guides = GuideSerializer(read_only=True, many=True)
    description = serializers.SerializerMethodField()
    def get_description(self, obj):
        if self.context.get('description', None):
            return self.context.get('description')

        return None

    class Meta:
        model = TouristTour
        fields = ['schedules', 'guides', 'price', 'titleNameCode', 'descriptionNameCode', 'owner', 'id', 'description', 'deletedDate']
        read_only_fields = ['id', 'deletedDate']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.Meta.depth = self.context.get('depth', 0)
    # For apllication

class BusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bus
        fields = '__all__'