from rest_framework.routers import SimpleRouter, DefaultRouter
from Core.users.views import UserViewSet
from Core.authorization.views import LoginViewSet, RegistrationViewSet, RefreshViewSet
from Core.tickets.api import RouteViewSet, LocationViewSet, PostTicketViewSet, DetailRouteViewSet, \
    DetailPostTicketViewSet, ReviewViewSet, OrderViewSet, ScheduleViewSet, TicketPersonViewSet
from Core.authorization.views import LoginViewSet, RegistrationViewSet, RefreshViewSet, VerifyViewSet

# AUTHENTICATION
routes = SimpleRouter()
routes.register(r'auth/login', LoginViewSet, basename='auth-login')
routes.register(r'auth/register', RegistrationViewSet, basename='auth-register')
routes.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')
routes.register(r'auth/verify', VerifyViewSet, basename='auth-verify')

# USER
routes.register(r'users', UserViewSet, basename='users')

# TICKETS
router = DefaultRouter()
detRouter = DefaultRouter()
router.register('routes',RouteViewSet,basename='routes')
router.register('location',LocationViewSet, basename='location')
router.register('ticket',PostTicketViewSet,basename='ticket')
detRouter.register('routes',DetailRouteViewSet,basename='routes')
detRouter.register('ticket',DetailPostTicketViewSet,basename='ticket')

# Ticket Person
ticketPersonRouter = DefaultRouter()
ticketPersonRouter.register('ticketPersons', TicketPersonViewSet, basename="ticketPerson")
# ticketPersonAsView = TicketPersonViewSet.as_view({
#     'post': 'create'
# })

# Schedule
scheduleRouter = DefaultRouter()
scheduleRouter.register("schedules", ScheduleViewSet, basename="schedule")


# REVIEWS
reviewRouter = DefaultRouter()
reviewRouter.register('reviews',ReviewViewSet, basename = 'reviews')
urlpatterns = [
    *routes.urls
]
# Order
orderRouter = DefaultRouter()
reviewRouter.register('order',OrderViewSet,basename= 'order')