from rest_framework import serializers
from Core.applications.models import Application, Document



class DocumentSerializer(serializers.ModelSerializer):


    class Meta:
        model = Document
        fields = '__all__'
        read_only_fields = ['deleteDate']