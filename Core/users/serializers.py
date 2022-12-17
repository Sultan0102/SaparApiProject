from Core.authorization.models import User
from rest_framework import serializers


class UserUpdateSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    email = serializers.CharField(max_length=250)
    firstName = serializers.CharField(max_length=250)
    lastName = serializers.CharField(max_length=250)
        
        
    
