from django.shortcuts import render
from Core.users.serializers import DriversSerializer, UserUpdateSerializer
from Core.authorization.serializers import GuideSerializer
from Core.authorization.models import Driver, IsAdmin, IsGuide, User, Guide
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from Core.exceptions import ValidationAPIException
from django.db.transaction import atomic 
from django.db.models import Q



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
            raise ValidationAPIException(detail="User id not supplied")

        guide = Guide.objects.get(user_id=userId)
        serializer = self.get_serializer(guide)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class DriversViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriversSerializer
    permission_classes = [IsAuthenticated, ]

    @atomic
    def update(self, request, pk, *args, **kwargs):
        driverData = {
            "id": pk,
            "yearExperience": request.data['yearExperience'],
            "phoneNumber": request.data['phoneNumber']
        }

        userData = {
            "email": request.data['user']['email'],
            "firstName": request.data['user']['firstName'],
            "lastName": request.data['user']['lastName'],
        }

        driver = Driver.objects.get(id=pk)
        driver.phoneNumber = driverData['phoneNumber']
        driver.yearExperience = driverData['yearExperience']
        driver.save()

        userData['id'] = driver.user.id
        
        updateUserSerializer = UserUpdateSerializer(data=userData)
        if updateUserSerializer.is_valid():
            upd_user = updateUserSerializer.validated_data
            user = User.objects.get(id=upd_user['id'])
            user.email = upd_user['email'];
            user.firstName = upd_user['firstName'];
            user.lastName = upd_user['lastName'];
            
            user.save();

        driverSerializer = self.get_serializer(driver)

        return Response(driverSerializer.data, status=status.HTTP_202_ACCEPTED)

    @action(detail=False, methods=['post'],url_path='name')
    def getDriversByName(self, request):
        name = request.data.get('name', None)
        if name is None:
            raise ValidationAPIException(detail="Driver Name was not supplied!")
        
        driverUsers = User.objects.filter(role=5).filter(Q(firstName__icontains=name) | Q(lastName__icontains=name))
        print(driverUsers)
        drivers = Driver.objects.filter(user_id__in=[i.id for i in driverUsers])
        serializer = self.get_serializer(drivers, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK);

    @action(detail=False, methods=['post'], url_path="user")
    def getDriverByUserId(self, request):
        userId = request.data.get('userId', None)
        if userId is None:
            raise ValidationAPIException(detail="User id was not supplied!")

        driver = Driver.objects.get(user_id=userId);
        serializer = self.get_serializer(driver)

        return Response(serializer.data, status=status.HTTP_200_OK)
        
