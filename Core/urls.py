from xml.etree.ElementInclude import include
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path,include
from .routers import router, detRouter
from .tickets.api import PostTicketViewSet, RouteViewSet, LocationViewSet, LocationView, DetailPostTicketViewSet
from .authorization.views import forgot_password,change_password

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('api/', include(('Core.routers', 'Core'), namespace='core-api')),
    path('api/post_ticket/<int:pk>/<int:lang_id>/',DetailPostTicketViewSet.as_view({'get' : 'retrieve'})),
    path('api/post_ticket/<int:lang_id>/', DetailPostTicketViewSet.as_view({'get': 'list'})),
    path('api/', include(detRouter.urls)),
    path('forgot-password/', forgot_password),
    path('change-password/<int:user_id>/', change_password),
    # path('api/showtickets/<int:pk>', TicketView.as_view())
    path('api/getloc', LocationView.as_view())
]
