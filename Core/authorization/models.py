from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import UserManager
from Core.authorization.managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(db_index=True, max_length=254,unique=True)
    username = models.CharField(db_index=True, max_length=255)
    password = models.CharField(db_index=True, max_length=255)
    firstName = models.CharField(db_index=True, max_length=255,blank=True)
    lastName = models.CharField(db_index=True, max_length=255, blank=True)
    birthDate = models.DateField(db_index=True,blank=True,null=True)
    is_staff = models.BooleanField(default=False,blank=True)
    isDeleted = models.BooleanField(default=False,blank=True)
    creationDate = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        db_table = "Users"
    

    def __str__(self):
        return self.email
