from rest_framework import serializers, status
from rest_framework.response import Response

from Core.applications.models import Application, Document, ApplicationStatus
from Core.authorization.models import Driver
from Core.tickets.models import Schedule


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


class ScheduleDriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ('__all__')
        read_only_fields = ('language_id', )

    def __init__(self,*args,**kwargs):
        super(ScheduleDriverSerializer, self).__init__(*args,**kwargs)
        self.Meta.depth = 3

class ApplicationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')

class ApplicationDriverSerializer(serializers.ModelSerializer):
    senderUser = serializers.HiddenField(default=serializers.CurrentUserDefault())
    receiverUser = serializers.HiddenField(default=None)
    documents = DocumentSerializer(many=True,read_only=True)
    status = serializers.HiddenField(default=ApplicationStatus.objects.first())
    class Meta:
        model = Application
        fields = ('__all__')

    def create(self, validated_data):
        user = self.context['request'].user
        documents = Document.objects.filter(owner=user)

        validated_data.pop('senderUser', None)  # Remove senderUser from validated_data
        receiver_user = validated_data.pop('receiverUser', None)  # Remove receiverUser from validated_data

        application = Application.objects.create(senderUser=user, **validated_data)
        application.documents.set(documents)  # Assign the related documents using set()

        return application



    def __init__(self, *args, **kwargs):
        if kwargs.get('context', {}).get('request', {}).method == 'GET':
            self.Meta.depth = 1

        super(ApplicationDriverSerializer, self).__init__(*args, **kwargs)

class ApplicationSerializerRetrieve(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ('__all__')

    def __init__(self, *args, **kwargs):
        super(ApplicationSerializerRetrieve, self).__init__(*args, **kwargs)
        self.Meta.depth = 1

class DocumentsViewSetSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault(),
    )
    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user
        return super().create(validated_data)
    class Meta:
        model = Document
        fields = ('__all__')

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ('__all__')
