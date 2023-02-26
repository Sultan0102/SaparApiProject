from django.core.exceptions import ObjectDoesNotExist
from Core.exceptions import EmailAlreadyExistsException, InvalidPasswordException
from Core.authorization.models import *
from rest_framework import serializers
from django.contrib.auth.models import update_last_login
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings
import math, random
from Core import validators


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'firstName', 'lastName', 'birthDate', 'isDeleted', 'role']
        read_only_field = ['isDeleted', 'creationDate', 'is_staff']

class LoginSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        print(attrs)
        data = super().validate(attrs)
        data['user'] = {
            'id': str(UserSerializer(self.user).data['id']),
            'email': str(UserSerializer(self.user).data['email']),
            'role': str(UserSerializer(self.user).data['role']),
        }

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)
        
        return data


class RegisterSerializer(UserSerializer):
    password = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)
    email = serializers.EmailField(required=True, write_only=True, max_length=128)

    class Meta:
        model = User
        fields = ('__all__')

    def validate_password(self, value):
        
        if validators.validate_password(value) == False:
            raise InvalidPasswordException()
        return value
            


    def generateOTP(self):
        digits = '0123456789'
        OTP = ''

        for i in range(4):
            OTP += digits[math.floor(random.random() * 10)]

        return OTP

    def save(self):
        try:
            user = User.objects.get(email=self.validated_data['email'])
        except ObjectDoesNotExist:
            user = None
        
        if user:
            raise EmailAlreadyExistsException()
        
        self.validated_data['role'] = User.CUSTOMER
        self.validated_data['verificationCode'] = self.generateOTP();
        
        
        return User.objects.create_user(**self.validated_data)
        
