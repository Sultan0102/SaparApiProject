from rest_framework import serializers
from .models import *
from .models import PostTicket


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


class PostTicketsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostTicket
        fields = ['id','route','cost','status','created','updated','person']
        read_only_field = ['created','updated']


class DetailPostTicketsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostTicket
        fields = ['id','route','cost','status','created','updated','person']
        read_only_field = ['created','updated']

    def __init__(self,*args,**kwargs):
        super(DetailPostTicketsSerializer, self).__init__(*args,**kwargs)
        self.Meta.depth = 3

class LocationSer(serializers.Serializer):
    id = serializers.IntegerField
    language = serializers.IntegerField