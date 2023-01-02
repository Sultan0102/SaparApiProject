from django.core.exceptions import ObjectDoesNotExist
from Core.exceptions import EmailAlreadyExistsException
from Core.authorization.models import *
from rest_framework import serializers
from django.contrib.auth.models import update_last_login
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'firstName', 'lastName', 'birthDate', 'isDeleted']
        read_only_field = ['isDeleted', 'creationDate', 'is_staff']

class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['user'] = {
            'id': str(UserSerializer(self.user).data['id']),
            'email': str(UserSerializer(self.user).data['email']),
            'roles': 'notImplementedYet',
            'accessToken': str(refresh.access_token),
            'refreshToken': str(refresh),
        }

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)
        print(data)
        return data


class RegisterSerializer(UserSerializer):
    password = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)
    email = serializers.EmailField(required=True, write_only=True, max_length=128)

    class Meta:
        model = User
        fields = ('__all__')

    def save(self):
        try:
            user = User.objects.get(email=self.validated_data['email'])
        except ObjectDoesNotExist:
            user = None
        
        if user:
            raise EmailAlreadyExistsException()
        
        return User.objects.create_user(**self.validated_data)
        
