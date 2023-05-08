from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets, generics, permissions
from Core.applications.serializers import DocumentSerializer, ApplicationSerializer
from Core.applications.models import Document, Application
from rest_framework.decorators import action
from Core.exceptions import ValidationAPIException



class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    @action(detail=False, methods=['post'], url_path="user")
    def getApplicationByUser(self, request):
        print('Applications by User Endpoint')
        senderUser = request.data.get('senderUser', None)


        applications = Application.objects.all()
        if senderUser:
            applications = applications.filter(senderUser__id=senderUser)
            
        serializer = ApplicationSerializer(applications, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    # def create(self, request, *args, **kwargs):
    #     print(request.data)
    #     return Response("created", status=status.HTTP_200_OK)