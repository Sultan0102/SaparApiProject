from django.contrib import admin
from .models import *
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('id','cost','route_id')
    list_display_links = ('id', 'route_id')
class RouteAdmin(admin.ModelAdmin):
    list_display = ('id','destination','source','duration','distance')

class LocationAdmin(admin.ModelAdmin):
    list_display = ('id','coordinates','name')

class ResourceAdmin(admin.ModelAdmin):
    list_display = ('id','value')

admin.site.register(PostTicket,PostAdmin)
admin.site.register(Route,RouteAdmin)
admin.site.register(Location,LocationAdmin)
admin.site.register(ResourceCode,ResourceAdmin)