from xml.etree.ElementInclude import include
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path,include
from .tickets.views import PostTicketViewSet, RouteViewSet, LocationViewSet
from .authorization.views import forgot_password,change_password

router = DefaultRouter()
router.register('routes',RouteViewSet,basename='routes')
router.register('location',LocationViewSet)
router.register('post_ticket',PostTicketViewSet,basename='post_ticket')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('api/', include(('Core.routers', 'Core'), namespace='core-api')),
    path('forgot-password/',forgot_password),
    path('change-password/<int:user_id>/',change_password),
]
