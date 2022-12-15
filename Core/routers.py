from rest_framework.routers import SimpleRouter, DefaultRouter
from Core.users.views import UserViewSet
from Core.authorization.views import LoginViewSet, RegistrationViewSet, RefreshViewSet
from Core.tickets.views import RouteViewSet, LocationViewSet, PostTicketViewSet

routes = SimpleRouter()

# AUTHENTICATION
routes.register(r'auth/login', LoginViewSet, basename='auth-login')
routes.register(r'auth/register', RegistrationViewSet, basename='auth-register')
routes.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')

# USER
routes.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    *routes.urls
]