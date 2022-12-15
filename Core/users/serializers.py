from Core.authorization.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'firstName', 'lastName', 'birthDate', 'isDeleted']
        read_only_field = ['isDeleted', 'creationDate', 'is_staff']
