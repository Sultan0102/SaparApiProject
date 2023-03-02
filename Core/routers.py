from rest_framework.routers import SimpleRouter, DefaultRouter
from Core.users.views import UserViewSet
from Core.authorization.views import LoginViewSet, RegistrationViewSet, RefreshViewSet
from Core.tickets.api import RouteViewSet, LocationViewSet, PostTicketViewSet, DetailRouteViewSet, \
    DetailPostTicketViewSet, ReviewViewSet
# AUTHENTICATION
routes = SimpleRouter()
routes.register(r'auth/login', LoginViewSet, basename='auth-login')
routes.register(r'auth/register', RegistrationViewSet, basename='auth-register')
routes.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')

# USER
routes.register(r'users', UserViewSet, basename='users')

# TICKETS
router = DefaultRouter()
detRouter = DefaultRouter()
router.register('routes',RouteViewSet,basename='routes')
router.register('location',LocationViewSet, basename='location')
router.register('post_ticket',PostTicketViewSet,basename='post_ticket')
detRouter.register('routes',DetailRouteViewSet,basename='routes')
detRouter.register('post_ticket',DetailPostTicketViewSet,basename='post_ticket')

# REVIEWS
reviewRouter = DefaultRouter()
reviewRouter.register('reviews',ReviewViewSet, basename = 'reviews')
urlpatterns = [
    *routes.urls
]