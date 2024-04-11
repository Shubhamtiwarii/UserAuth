from django.urls import path
from .views import UserRegistrationView, OTPVerificationView, UserLoginView, ForgotPasswordView, ResetPasswordView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('verify/', OTPVerificationView.as_view(), name='otp-verify'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot-password'),
    path('reset-password/', ResetPasswordView.as_view(), name='reset-password'),
]
