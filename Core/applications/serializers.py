from rest_framework import serializers
from Core.applications.models import Application, Document, ApplicationStatus
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
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    status = serializers.HiddenField(default=ApplicationStatus.objects.first())
    class Meta:
        model = Application
        fields = ('__all__')

    def __init__(self, *args, **kwargs):
        if kwargs.get('context', {}).get('request', {}).method == 'GET':
            self.Meta.depth = 1

        super(ApplicationSerializer, self).__init__(*args, **kwargs)

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