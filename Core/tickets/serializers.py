from rest_framework import serializers
from .models import *


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