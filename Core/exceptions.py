from rest_framework.views import exception_handler
from rest_framework.exceptions import APIException


def custom_exception_handler(ex, context):
    """Custom API exception handler"""

    response = exception_handler(ex, context)

    print(type(ex))
    if response is not None:
        response.data = {
                'status_code': response.status_code,
                'detail': ex.detail,
                'error_code': ex.default_code
            }
    
    return response
    
    

class ValidationAPIException(APIException):
    status_code = 400
    default_detail = "Validation error!"
    default_code = 'validation_error'

class EmailAlreadyExistsException(ValidationAPIException):
    default_detail = { 'email': 'User with given email already exists'}
    default_code = "email_already_exists"

class BadCredentialsException(ValidationAPIException):
    default_detail = {
        'email':'Invalid Email',
        'password':'Password should have at least 8 symbols including one upper case letter, lower case letter, a digit and a special character',
    }
    default_code = "bad_credentials"

class InvalidPasswordException(ValidationAPIException):
    default_detail = "The password should have at least 8 symbols including one upper case letter, lower case letter, a digit and a special character"
    default_code = "invalid_password"

class UserIsNotVerifiedException(ValidationAPIException):
    default_detail = "User is not verified!"
    default_code = "user_not_verified"

class FailedToSendEmailException(APIException):
    status_code = 503
    default_detail = "Failed to send an email!"
    default_code = "failed_to_send_email"
    
class InvalidVerificationCodeException(ValidationAPIException):
    default_detail = "The verification code is invalid or expired!"
    default_code = "invalid_verification_code"

class EmailNotFoundException(ValidationAPIException):
    default_code = "email_not_found"
    default_detail = "Given email does not exist!"
    
class InvalidTokenException(APIException):
    status_code = 401
    default_code = "invalid_token"
    default_detail = "Token is invalid or expired!"

class RefreshTokenInvalidException(InvalidTokenException):
    default_code = "refresh_token_invalid"
    default_detail = "Refresh token is invalid or expired!"