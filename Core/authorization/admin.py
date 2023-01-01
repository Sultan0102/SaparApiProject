from django.contrib import admin

# Register your models here.

from .models import *
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','email','firstName', 'lastName', 'birthDate', 'is_staff','isDeleted','creationDate')
    list_display_links = ('id','email')
    search_fields = ('email',)
    list_filter = ('isDeleted',)

admin.site.register(User,UserAdmin)
