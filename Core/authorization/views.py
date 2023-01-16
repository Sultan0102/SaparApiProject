from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from Core.authorization.serializers import UserSerializer
from Core.authorization.models import User
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from Core.authorization.serializers import LoginSerializer, RegisterSerializer
from django.core.mail import send_mail
class UserViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['updated']
    ordering = ['-updated']

    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.all()


class LoginViewSet(ModelViewSet, TokenObtainPairView):
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class RegistrationViewSet(ModelViewSet, TokenObtainPairView):
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        res = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }

        return Response({
            "user": serializer.data,
            "refresh": res["refresh"],
            "token": res["access"]
        }, status=status.HTTP_201_CREATED)


class RefreshViewSet(viewsets.ViewSet, TokenRefreshView):
    permission_classes = (AllowAny,)
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return Response(serializer.validated_data, status=status.HTTP_200_OK)

@csrf_exempt
def forgot_password(request):
    email = request.POST.get('email')
    verify = User.objects.filter(email=email).first()
    if verify:
        link = f"http://127.0.0.1:8000/change-password/{verify.id}/"
        send_mail(
            'Verify Account',
            'Please Verify your account',
            'saparServicePass@yandex.ru',
            [email],
            fail_silently=False,
            html_message=f'<p>To change password u need to follow this link</p><p>{link}</p>'
        )
        return JsonResponse({'bool': True, 'msg': 'Please Check your Email'})
    else:
        return JsonResponse({'bool': False, 'msg': 'Invalid Email'})
def change_password(request,user_id):
    password=request.POST.get('password')
    verify = User.objects.filter(id=user_id).first()
    if verify:
        verify = User.objects.filter(id=user_id).update(password=password)
        return JsonResponse({'bool': True, 'msg': 'Password has been changed'})
    else:
        return JsonResponse({'bool': False, 'msg': 'Error'})