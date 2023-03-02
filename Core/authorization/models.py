from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import UserManager
from Core.authorization.managers import CustomUserManager
from rest_framework import permissions


# class Role(models.Model):
#     id = models.AutoField(primary_key=True)
#     roleName = models.CharField(max_length=20,blank=False)

#     class Meta:
#         db_table = "Roles"

class User(AbstractBaseUser, PermissionsMixin):

    ADMIN = 1
    CUSTOMER = 2
    GUIDE =3
    BUSINESS_PERSON =3

    ROLE_CHOICES = (
          (ADMIN, 'Admin'),
          (CUSTOMER, 'Customer'),
          (GUIDE, 'Guide'),
          (BUSINESS_PERSON, 'Business Person'), 
      )

    id = models.AutoField(primary_key=True)
    email = models.EmailField(db_index=True, max_length=254,unique=True)
    password = models.CharField(db_index=True, max_length=255)
    firstName = models.CharField(db_index=True, max_length=255,blank=True)
    lastName = models.CharField(db_index=True, max_length=255, blank=True)
    birthDate = models.DateField(db_index=True,blank=True,null=True)
    is_staff = models.BooleanField(default=False,blank=True)
    isDeleted = models.BooleanField(default=False,blank=True)
    isVerified = models.BooleanField(default=False,blank=True)
    creationDate = models.DateTimeField(auto_now_add=True)
    verificationCode = models.CharField(max_length=255,blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        db_table = "Users"
    

    def __str__(self):
        return self.email

class IsGuide(permissions.BasePermission):
    """
    Allows access only to guide users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.role == User.GUIDE)

class IsAdmin(permissions.BasePermission):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.role == User.ADMIN)
    

class IsBusinessPerson(permissions.BasePermission):
    """
    Allows access only to business person users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.role == User.BUSINESS_PERSON)