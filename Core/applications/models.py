from django.db import models
from Core.authorization.models import User

# Create your models here.
class ApplicationType(models.Model):

    name = models.CharField(max_length=200)

    class Meta:
        db_table='ApplicationType'

class ApplicationStatus(models.Model):
    name = models.CharField(max_length=250)
    creationDate = models.DateTimeField(auto_now_add=True, db_index=True, null=True)

    class Meta:
        db_table='ApplicationStatus'

class Document(models.Model):
    owner = models.ForeignKey(User, on_delete=models.PROTECT, related_name='documents')
    creationDate = models.DateTimeField(auto_now_add=True)
    deleteDate = models.DateTimeField(null=True)
    type = models.ForeignKey('DocumentsType',on_delete=models.CASCADE,null=True)
    file = models.FileField(db_index=True, blank=True, null=True, upload_to='%Y/%m/%d/')

    class Meta:
        db_table='Document'

class Application(models.Model):
    senderUser = models.ForeignKey(User, on_delete=models.PROTECT, related_name='sent_applications')
    receiverUser = models.ForeignKey(User, on_delete=models.PROTECT, related_name='received_applications')
    status = models.ForeignKey(ApplicationStatus, on_delete=models.PROTECT)
    type = models.ForeignKey(ApplicationType, on_delete=models.PROTECT)
    creationDate = models.DateTimeField(auto_now_add=True)
    applicationData = models.JSONField()
    documents = models.ManyToManyField(Document, db_table="ApplicationDocuments", related_name="applications")

    class Meta:
        db_table='Application'


# class ApplicationDocuments(models.Model):
#     id = models.AutoField(primary_key = True)
#     name = models.CharField(db_index=True, max_length=255)
#     document = models.ForeignKey('Document',on_delete=models.CASCADE)
#     application = models.ForeignKey('Application', on_delete= models.CASCADE,default=1)
#
#     class Meta:
#         db_table = "ApplicationDocuments"


class DocumentsType(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(db_index=True, blank=True, max_length=255)
    creationDate = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        db_table = "DocumentsType"
