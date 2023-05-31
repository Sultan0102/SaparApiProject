from rest_framework.fields import empty
from Core.authorization.models import User, Driver
from rest_framework import serializers
from Core.authorization.serializers import UserSerializer



class UserUpdateSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    email = serializers.CharField(max_length=250)
    firstName = serializers.CharField(max_length=250)
    lastName = serializers.CharField(max_length=250)
        
        
    
class DriversSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Driver
        fields = ['id', 'phoneNumber', 'photo', 'user', 'yearExperience']
        read_only_fields = ['id']
        depth=1
    
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.Meta.depth = self.context.get('depth', 0)
    