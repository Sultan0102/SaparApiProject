from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import PostTicketsSerializer, RouteSerializer, LocationSerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer

class PostTicketViewSet(viewsets.ModelViewSet):
    queryset = PostTicket.objects.all()
    serializer_class = PostTicketsSerializer


# Create your views here.
