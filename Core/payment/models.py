from django.db import models
from Core.tickets.models import Order
from Core.authorization.models import User


# Create your models here.
class Payment(models.Model): 
    id = models.AutoField(primary_key=True)
    method = models.CharField(max_length=255)
    payDate = models.DateTimeField()
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    payedAmount = models.FloatField()

    class Meta:
        db_table="Payment"
