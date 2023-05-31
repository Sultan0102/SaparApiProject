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
    GUIDE = 3
    BUSINESS_PERSON = 4
    DRIVER = 5

    ROLE_CHOICES = (
          (ADMIN, 'Admin'),
          (CUSTOMER, 'Customer'),
          (GUIDE, 'Guide'),
          (BUSINESS_PERSON, 'Business Person'), 
          (DRIVER, 'Driver'), 
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



class BusinessPerson(models.Model):
    id = models.AutoField(primary_key=True)
    companyName = models.CharField(max_length=255, blank=False)
    binNumber = models.CharField(max_length=12)
    legalAddress = models.CharField(max_length=255)
    serviceRating = models.FloatField(default=0)
    user = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False)

    class Meta:
        db_table = "BusinessPerson"

class Guide(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False)
    serviceRating = models.FloatField(default=0)
    
    class Meta:
        db_table = "Guide"
    

class GuideSpecialization(models.Model):
    id = models.AutoField(primary_key=True)
    guide = models.ForeignKey(Guide, on_delete=models.PROTECT, blank=False, null=False)
    name = models.CharField(max_length=255, blank=False)
    isMain = models.BooleanField(null=False)

    class Meta:
        db_table="GuideSpecialization"

class Driver(models.Model):
    yearExperience = models.IntegerField()
    phoneNumber = models.CharField(max_length=20)
    photo = models.FileField(null=True,upload_to='photos/%Y/%m/%d/')
    user = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False)

    class Meta:
        db_table = "Driver"
















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