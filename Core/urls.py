from xml.etree.ElementInclude import include

from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path,include

from .applications.api import ApplicationViewSet, ApplicationDriverViewSet
from .routers import router, detRouter, reviewRouter, scheduleRouter, ticketPersonRouter, cachedTicketPersonRouter, ticketRouter, driverRouter
from .tickets.api import PostTicketViewSet, RouteViewSet, LocationViewSet, LocationView, DetailPostTicketViewSet, \
    ScheduleDriverViewSet

from . import settings
from .routers import router, detRouter, reviewRouter, ticketPersonRouter, scheduleRouter, \
    applicationRouter, documentsRouter
from .tickets.api import PostTicketViewSet, RouteViewSet, LocationViewSet, LocationView, DetailPostTicketViewSet, \
    ScheduleViewSet
from .authorization.views import forgot_password,change_password

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
    path('api/', include(('Core.routers', 'Core'), namespace='core-api')),
    path('api/ticket/<int:pk>/<int:lang_id>/',DetailPostTicketViewSet.as_view({'get' : 'retrieve'})),
    path('api/ticket/<int:lang_id>/', DetailPostTicketViewSet.as_view({'get': 'list'})),
    path('api/', include(detRouter.urls)),
    path('api/', include(ticketRouter.urls)),
    path('api/', include(reviewRouter.urls)),
    path('api/', include(scheduleRouter.urls)),
    path('api/', include(ticketPersonRouter.urls)),
    path('api/', include(cachedTicketPersonRouter.urls)),
    path('forgot-password/', forgot_password),
    path('change-password/<int:user_id>/', change_password),
    # path('api/showtickets/<int:pk>', TicketView.as_view())
    path('api/getloc', LocationView.as_view()),
    path('api/', include(applicationRouter.urls)),
    path('api/schedules/<int:pk>/<int:lang_id>/', ScheduleDriverViewSet.as_view({'get': 'retrieve'})),
    path('api/applications/<int:pk>/', ApplicationDriverViewSet.as_view({'get': 'retrieve'})),
    path('api/',include(documentsRouter.urls)),
    path('api/',include(driverRouter.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
