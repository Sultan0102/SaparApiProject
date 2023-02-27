from rest_framework.routers import SimpleRouter, DefaultRouter
from Core.users.views import UserViewSet
from Core.authorization.views import LoginViewSet, RegistrationViewSet, RefreshViewSet, VerifyViewSet
from Core.tickets.api import RouteViewSet, LocationViewSet, PostTicketViewSet, DetailRouteViewSet,DetailPostTicketViewSet

routes = SimpleRouter()
router = DefaultRouter()
detRouter= DefaultRouter()

# AUTHENTICATION
routes.register(r'auth/login', LoginViewSet, basename='auth-login')
routes.register(r'auth/register', RegistrationViewSet, basename='auth-register')
routes.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')
routes.register(r'auth/verify', VerifyViewSet, basename='auth-verify')

# USER
routes.register(r'users', UserViewSet, basename='users')

# TICKETS
router.register('routes',RouteViewSet,basename='routes')
router.register('location',LocationViewSet, basename='location')
router.register('post_ticket',PostTicketViewSet,basename='post_ticket')
detRouter.register('routes',DetailRouteViewSet,basename='routes')
detRouter.register('post_ticket',DetailPostTicketViewSet,basename='post_ticket')

urlpatterns = [
    *routes.urls
]