from django.shortcuts import render
from Core.users.serializers import UserUpdateSerializer
from Core.authorization.models import IsAdmin, IsGuide, User
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from rest_framework import status
from rest_framework.response import Response


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'delete', 'put']
    serializer_class = UserUpdateSerializer
    permission_classes = (IsAuthenticated, )

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

    def update(self, request, pk, *args, **kwargs):
        request.data['id'] = pk;
        serializer = self.get_serializer(data=request.data);
        
        if serializer.is_valid():
            upd_user = serializer.validated_data
            print(upd_user)
            user = User.objects.get(id=upd_user['id'])
            user.email = upd_user['email'];
            user.firstName = upd_user['firstName'];
            user.lastName = upd_user['lastName'];
            
            user.save();

            return Response(data=serializer.validated_data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        