from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from rest_framework.permissions import IsAuthenticated
from .serializers import PostTicketsSerializer, RouteSerializer, LocationSerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [IsAuthenticated]

class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    permission_classes = [IsAuthenticated]

class PostTicketViewSet(viewsets.ModelViewSet):
    queryset = PostTicket.objects.all()
    serializer_class = PostTicketsSerializer
    permission_classes = [IsAuthenticated]


# Create your views here.
