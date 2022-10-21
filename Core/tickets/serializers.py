from rest_framework import serializers
from .models import *
from .models import PostTicket
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id','coordinates','name']

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ['id','destination','source','duration','distance']

class PostTicketsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostTicket
        fields = ['id','route_id','cost']
        read_only_field = ['created','updated']