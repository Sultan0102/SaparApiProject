from rest_framework.routers import SimpleRouter, DefaultRouter
from Core.users.views import UserViewSet, GuideViewSet
from Core.authorization.views import LoginViewSet, RegistrationViewSet, RefreshViewSet
from Core.tickets.api import CachedTicketPersonViewSet, PassportNumberTypeViewSet, RouteViewSet, LocationViewSet, \
    PostTicketViewSet, DetailRouteViewSet, \
    DetailPostTicketViewSet, ReviewViewSet, OrderViewSet, ScheduleViewSet, TicketPersonViewSet, TicketViewSet, \
    TouristTourViewSet
from Core.authorization.views import LoginViewSet, RegistrationViewSet, RefreshViewSet, VerifyViewSet
from Core.payment.api import PaymentViewSet
from Core.applications.api import DocumentViewSet, ApplicationViewSet, DocumentsViewSet, ApplicationDriverViewSet

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
detRouter.register('routes',DetailRouteViewSet,basename='routes')
detRouter.register('tickets', TicketViewSet, basename="tickets")
detRouter.register('tours', TouristTourViewSet, basename='tour')
detRouter.register('docs', DocumentViewSet, basename='doc')
detRouter.register('applications', ApplicationViewSet, basename='application')
detRouter.register('guides', GuideViewSet, basename='guide')

# Ticket Person
ticketRouter = DefaultRouter()
#PassportNumber
ticketRouter.register('passportTypes',PassportNumberTypeViewSet,basename='passportTypes')

# Ticket Person
ticketPersonRouter = DefaultRouter()
ticketPersonRouter.register('ticketPersons', TicketPersonViewSet, basename="ticketPerson")

# Cached Ticket Person
cachedTicketPersonRouter = DefaultRouter()
cachedTicketPersonRouter.register('cachedTicketPersons', CachedTicketPersonViewSet, basename="cachedTicketPerson")


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
orderRouter.register('orders', OrderViewSet,basename= 'orders')
orderRouter.register('payment', PaymentViewSet, basename='payment')
#For Application
# Schedule
scheduleRouter = DefaultRouter()
scheduleRouter.register("schedules", ScheduleViewSet, basename="schedule")
# Application
applicationRouter = DefaultRouter()
applicationRouter.register("driver/applications", ApplicationDriverViewSet, basename="applications")
# Documents
documentsRouter = DefaultRouter()
documentsRouter.register("documents",DocumentsViewSet,basename="documents")