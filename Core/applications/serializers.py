from rest_framework import serializers
from Core.applications.models import Application, Document



class DocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Document
        fields = '__all__'
    

class ApplicationSerializer(serializers.ModelSerializer):
    documents = serializers.PrimaryKeyRelatedField(many=True, queryset= Document.objects.all())

    class Meta:
        model = Application
        fields = ['id', 'senderUser', 'receiverUser', 'status', 'type', 'creationDate', 'applicationData', 'documents']
        read_only_fields = ['id']