from django.db import models
class TicketStatus(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(db_index=True,max_length=255)
    class Meta:
        db_table = "TicketStatus"
class PassportNumberType(models.Model):
    id = models.AutoField(primary_key=True)
    typeName = models.CharField(db_index=True,max_length=255)
    format = models.CharField(db_index=True,max_length=255)
    class Meta:
        db_table = "PassportNumberType"
class TicketPerson(models.Model):
    id = models.AutoField(primary_key=True)
    firstName = models.CharField(db_index=True,max_length=255)
    lastName = models.CharField(db_index=True, max_length=255)
    secondName = models.CharField(db_index=True, max_length=255)
    passportNumber= models.CharField(db_index=True, max_length=255)
    passportNumberType = models.ForeignKey('PassportNumberType', on_delete=models.PROTECT, blank=True)
    class Meta:
        db_table = "TicketPerson"
class PostTicket(models.Model):
    id = models.AutoField(primary_key=True)
    route = models.ForeignKey('Route', on_delete=models.PROTECT, blank=True,related_name='routes')
    person = models.ForeignKey('TicketPerson',on_delete=models.PROTECT,blank=True)
    status = models.ForeignKey('TicketStatus', on_delete=models.PROTECT,blank=True)
    cost = models.IntegerField(db_index=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "PostTicket"


class Route(models.Model):
    id = models.AutoField(primary_key=True)
    destination = models.ForeignKey('Location', on_delete=models.PROTECT, blank=True, related_name='destination')
    source = models.ForeignKey('Location', on_delete=models.PROTECT, blank=True, related_name='source')
    duration = models.CharField(db_index=True,max_length=255)
    distance = models.FloatField()

    class Meta:
        db_table = "Route"

class ResourceCode(models.Model):
    id = models.AutoField(primary_key=True)
    value = models.CharField(db_index=True,max_length=255)

    class Meta:
        db_table = "ResourceCode"

class Language(models.Model):
    id = models.AutoField(primary_key=True)
    resourcecode = models.ForeignKey('ResourceCode', on_delete=models.PROTECT,blank=True)
    nativeName = models.CharField(db_index=True, max_length=255)

    class Meta:
        db_table = "Language"

class ResourceValue(models.Model):
    id = models.AutoField(primary_key=True)
    language = models.ForeignKey('Language',on_delete=models.PROTECT,blank=True)
    nameCode = models.ForeignKey('ResourceCode',on_delete=models.PROTECT,blank=True)
    value = models.CharField(db_index=True, max_length=255)
    deleteDate = models.DateTimeField

    class Meta:
        db_table = "ResourceValue"

class Location(models.Model):
    id = models.AutoField(primary_key=True)
    coordinates = models.CharField(db_index=True, max_length=255)
    nameCode = models.ForeignKey('ResourceCode',on_delete=models.PROTECT)

    class Meta:
        db_table = "Location"

class BusType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(db_index=True, max_length=255)
    capacity = models.IntegerField(db_index=True, blank=True)

    class Meta:
        db_table = "BusType"

class Bus(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(db_index=True, max_length=255)
    type = models.ForeignKey('BusType', on_delete=models.PROTECT,blank=True)
    availableCapacity= models.IntegerField(db_index=True, blank=True)

    class Meta:
        db_table = "Bus"
