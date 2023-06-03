from django.http import Http404
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets, generics, permissions
from Core.applications.serializers import DocumentSerializer, ApplicationSerializer, ApplicationDriverSerializer, \
    ApplicationSerializerRetrieve, DocumentsViewSetSerializer, DriverSerializer, ApplicationTypeSerializer
from Core.applications.models import Document, Application, ApplicationStatus, ApplicationType
from rest_framework.decorators import action
from django.db.transaction import atomic
from Core.authorization.models import Driver
from Core.tickets.models import Schedule
from Core.exceptions import ValidationAPIException
from django.db.models import Q



class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    # http_method_names=['post', 'get', 'patch']

    def get_serializer_context(self):
        context = super().get_serializer_context()
        depth = self.request.query_params.get('depth', 0)
        context['depth'] = int(depth)
        return context

    @action(detail=False, methods=['get'], url_path='types')
    def getApplicationTypes(self, request):
        types = ApplicationType.objects.all()
        serializer = ApplicationTypeSerializer(types, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['patch'], url_path='status')
    @atomic
    def updateApplicationStatus(self, request):
        applicationId = request.data.get('applicationId', None)

        if applicationId is None:
            return Response('No applicationId id was provided', status=status.HTTP_400_BAD_REQUEST)
        
        statusId = request.data.get('status', None)

        if statusId is None:
            return Response('No status was provided', status=status.HTTP_400_BAD_REQUEST)

        application = Application.objects.get(id=applicationId)
        applicationStatus = ApplicationStatus.objects.get(id=statusId)

        if applicationStatus.id == 2:
            if application.type_id == 5:
                self.removeDriverFromRoute(application.senderUser.id, application.applicationData['Schedule id'])

        application.status_id = applicationStatus.id
        application.save();

        serializer = ApplicationSerializer(application)

        return Response(serializer.data, status=status.HTTP_200_OK)


    @action(detail=False, methods=['post'], url_path="user")
    def getApplicationByUser(self, request):
        print('Applications by User Endpoint')
        userId = request.data.get('userId', None)


        applications = Application.objects.all()
        if userId:
            applications = applications.filter(Q(senderUser__id=userId) | Q(receiverUser__id=userId))
        else:
            return Response('No user id was provided', status=status.HTTP_400_BAD_REQUEST)
        serializer = ApplicationSerializer(applications, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['post'], url_path='drivers')
    def getDriverApplications(self, request):
        applications = Application.objects.filter(type_id__in=[3, 4, 5, 6])
        serializer = ApplicationSerializer(applications, many=True, context={'depth': 2})

        return Response(serializer.data, status=status.HTTP_200_OK);

    def removeDriverFromRoute(self, driverUserId, scheduleId):
        print(driverUserId, scheduleId)
        schedule = Schedule.objects.get(id=scheduleId)

        if schedule.driver.id == driverUserId:
            schedule.driver = None
        schedule.save();

        
    # def create(self, request, *args, **kwargs):
    #     print(request.data)
    #     return Response("created", status=status.HTTP_200_OK)

class ApplicationDriverViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationDriverSerializer

    def retrieve(self, request, pk=None, *args, **kwargs):
        queryset = Application.objects.filter(senderUser=pk)
        serializer = ApplicationSerializerRetrieve(queryset,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    # def create(self, request):
    #     applicationData = request.data['applicationData']
    #     application = Application.objects.create(applicationData=applicationData)
    #     application.save()
    #     serializer = ApplicationSerializer(application)
    #     return Response(serializer.data)
class DocumentsViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentsViewSetSerializer

    def retrieve(self, request, pk=None, *args, **kwargs):
        queryset = Document.objects.filter(owner=pk)
        serializer = DocumentsViewSetSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    def retrieve(self, request, pk=None, *args, **kwargs):
            queryset = self.get_queryset().filter(user__pk=pk)
            instance = queryset.first()
            if instance:
                serializer = self.get_serializer(instance)
                return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['patch'])
    def update_photo(self, request, pk=None):
        driver = self.get_object()
        photo = request.FILES.get('photo')

        if photo:
            driver.photo = photo
            driver.save()
            return Response({'message': 'Photo updated successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'No photo provided'}, status=status.HTTP_400_BAD_REQUEST)


