import datetime

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from datetime import datetime


class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    email = models.CharField(db_index=True, max_length=255,unique=True)
    password = models.CharField(db_index=True, max_length=255)
    firstName = models.CharField(db_index=True, max_length=255)
    lastName = models.CharField(db_index=True, max_length=255)
    birthDate = models.DateField(db_index=True)
    isDeleted = models.BooleanField(default=False)
    creationDate = models.DateTimeField(auto_now_add=True)
    role_id = models.ForeignKey('Role', on_delete=models.PROTECT())
    class Meta:
        db_table = "Users"

class Role(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(db_index=True, max_length=255,unique=True)

    class Meta:
        db_table = "Roles"





