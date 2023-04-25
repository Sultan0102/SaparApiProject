from rest_framework import status
from rest_framework import viewsets, generics, permissions
from Core.applications.serializers import DocumentSerializer
from Core.applications.models import Document, Application


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

class ApplicationViewSet(viewsets.ModelViewSet):
    pass 



