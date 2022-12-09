from random import randint
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from rest_framework.permissions import IsAuthenticated
from .serializers import PostTicketsSerializer, RouteSerializer, LocationSerializer
from ..authorization.models import User


class LocationViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class RouteViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Route.objects.all()
    serializer_class = RouteSerializer

class PostTicketViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = PostTicket.objects.all()
    serializer_class = PostTicketsSerializer

# Create your views here.
