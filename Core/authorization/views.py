from Core.authorization.serializers import UserSerializer, VerifyUserSerializer
from Core.exceptions import EmailNotFoundException, InvalidVerificationCodeException, \
ValidationAPIException, FailedToSendEmailException, RefreshTokenInvalidException, InvalidTokenException
from django.http import JsonResponse
from django.core.mail import send_mail
from django.core.exceptions import ObjectDoesNotExist
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
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken, AuthenticationFailed
from Core.authorization.serializers import LoginSerializer, RegisterSerializer
from rest_framework.exceptions import ValidationError



class LoginViewSet(ModelViewSet, TokenObtainPairView):
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidTokenException()

        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class RegistrationViewSet(ModelViewSet, TokenObtainPairView):
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            raise ValidationAPIException(serializer.errors)

        user = serializer.save()
        
        try:
            send_mail(
                subject="Account Verification",
                html_message=f"<h2>Your Verification Code: {user.verificationCode}</h2>",
                from_email="saparServicePass@yandex.ru",
                receipient_list=[user.email],
                fail_silently=False
            )
        except:
            raise FailedToSendEmailException()
            
        return Response(status=status.HTTP_201_CREATED)
        


class RefreshViewSet(viewsets.ViewSet, TokenRefreshView):
    permission_classes = (AllowAny,)
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise RefreshTokenInvalidException()
            # return Response(data=e.args[0], status=status.HTTP_401_UNAUTHORIZED)
            # raise InvalidToken(e.args[0])

        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class VerifyViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)
    http_method_names = ['post']

    def create(self, request):
        try:
            serializer = VerifyUserSerializer(data=request.data)
            
            serializer.is_valid(raise_exception=True)
            
            user = User.objects.get(email=serializer.validated_data['email'])
            if user.verificationCode != serializer.validated_data['verificationCode']:
                raise InvalidVerificationCodeException();
        
            user.isVerified = True;
            user.verificationCode = '';
            user.save();

            return Response("Successfully verified", status=status.HTTP_200_OK)

        except ObjectDoesNotExist as e:
            """Do something"""
            raise EmailNotFoundException();


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

    