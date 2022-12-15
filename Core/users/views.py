from django.shortcuts import render
from Core.users.serializers import UserSerializer
from Core.authorization.models import User
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from rest_framework import status
from rest_framework.response import Response


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'delete', 'update']
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.all()
    
    def retrieve(self, request, pk):
        print('retrieve method!')
        user_id = pk;
        user = User.objects.get(id=user_id);


        if user:
            userResponse = {
                'firstName': user.firstName,
                'lastName': user.lastName,
                'email': user.email
            }
            return Response(data=userResponse, status=status.HTTP_200_OK);
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
