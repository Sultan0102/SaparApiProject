from django.http import Http404
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets, generics, permissions
from Core.applications.serializers import DocumentSerializer, ApplicationSerializer, ApplicationDriverSerializer, \
    ApplicationSerializerRetrieve, DocumentsViewSetSerializer, DriverSerializer
from Core.applications.models import Document, Application
from rest_framework.decorators import action

from Core.authorization.models import Driver
from Core.exceptions import ValidationAPIException
from django.db.models import Q



class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    @action(detail=False, methods=['post'], url_path="user")
    def getApplicationByUser(self, request):
        print('Applications by User Endpoint')
        userId = request.data.get('userId', None)


        applications = Application.objects.all()
        if userId:
            applications = applications.filter(Q(senderUser__id=userId) | Q(receiverUser__id=userId))
            
        serializer = ApplicationSerializer(applications, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
        
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


