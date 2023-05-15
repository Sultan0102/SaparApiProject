from django.core.exceptions import ObjectDoesNotExist
from Core.exceptions import BadCredentialsException, EmailAlreadyExistsException, \
InvalidPasswordException, InvalidVerificationCodeException, UserIsNotVerifiedException
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
        fields = ['id', 'email', 'password', 'firstName', 'lastName', 'birthDate', 'isDeleted', 'role', 'isVerified']
        read_only_field = ['isDeleted', 'creationDate', 'is_staff', 'isVerified']

class LoginSerializer(TokenObtainPairSerializer):

    def validate_isVerified(self, value):
        return value
    

    def validate(self, attrs):
        try:
            data = super().validate(attrs)
        except:
            raise BadCredentialsException();
        
        serialized_user = UserSerializer(self.user)
        
        if serialized_user.data['isVerified'] == False:
            raise UserIsNotVerifiedException()

        data['user'] = {
            'id': str(serialized_user.data['id']),
            'email': serialized_user.data['email'],
            'role': str(serialized_user.data['role']),
        }

        
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
        
        print("Validated Data: ")
        print(self.validated_data)
        return User.objects.create_user(**self.validated_data)

class VerifyUserSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, max_length=128)
    verificationCode = serializers.CharField(max_length=4, min_length=4, required=True)

    def validate_verificationCode(self, value):
        if validators.validate_verificationCode(value):
            return value
        else:
            raise InvalidVerificationCodeException()

    
        
