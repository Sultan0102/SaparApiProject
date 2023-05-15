from django.shortcuts import render
from Core.users.serializers import UserUpdateSerializer
from Core.authorization.serializers import GuideSerializer
from Core.authorization.models import IsAdmin, IsGuide, User, Guide
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from Core.exceptions import ValidationAPIException


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    http_method_names = ['get', 'post', 'delete', 'put']
    serializer_class = UserUpdateSerializer
    permission_classes = (IsAuthenticated, )

    # def get_queryset(self):
    #     if self.request.user.is_superuser:
    #         return User.objects.all()
        
    
    def retrieve(self, request, pk):
        print('retrieve method!')
        user_id = pk;
        user = User.objects.get(id=user_id);


        if user:
            userResponse = {
                'id' : user_id,
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
    
class GuideViewSet(viewsets.ModelViewSet):
    queryset = Guide.objects.all()
    serializer_class = GuideSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['depth'] = 1
        return context

    @action(detail=False, methods=['post'], url_path='user')
    def getGuideByUserId(self, request):
        userId = request.data.get('userId', None)
        if userId is None:
            raise ValidationAPIException(detail="Schedule id not supplied")

        guide = Guide.objects.get(user_id=userId)
        serializer = self.get_serializer(guide)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    