from django.db import models
class PostTicket(models.Model):
    id = models.AutoField(primary_key=True)
    route_id = models.ForeignKey('Route', on_delete=models.PROTECT, blank=True,related_name='routes')
    cost = models.IntegerField(db_index=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Route(models.Model):
    id = models.AutoField(primary_key=True)
    destination = models.ForeignKey('Location', on_delete=models.PROTECT, blank=True, related_name='destination')
    source = models.ForeignKey('Location', on_delete=models.PROTECT, blank=True, related_name='source')
    duration = models.TimeField(db_index=True)
    distance = models.FloatField()


class Location(models.Model):
    id = models.AutoField(primary_key=True)
    coordinates = models.CharField(db_index=True, max_length=255)
    name = models.CharField(db_index=True, max_length=255)
