from django.shortcuts import render
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from .serializers import UserRegistrationSerializer, OTPVerificationSerializer, UserLoginSerializer, ForgotPasswordSerializer, ResetPasswordSerializer

from rest_framework.exceptions import AuthenticationFailed
class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OTPVerificationView(APIView):
    def post(self, request):
        serializer = OTPVerificationSerializer(data=request.data)
        if serializer.is_valid():
            # Implement OTP verification logic
            return Response({"message": "OTP verified successfully"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            email_or_username = serializer.validated_data.get('email_or_username')
            otp = serializer.validated_data.get('otp')

            # Authenticate user
            user = authenticate(request=request, username=email_or_username, password=otp)

            if user is None:
                raise AuthenticationFailed("Invalid credentials")

            # Generate access and refresh tokens
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ForgotPasswordView(APIView):
    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        if serializer.is_valid():
            # Implement forgot password logic
            return Response({"message": "Password reset instructions sent to your email"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ResetPasswordView(APIView):
    def post(self, request):
        serializer = ResetPasswordSerializer(data=request.data)
        if serializer.is_valid():
            # Implement reset password logic
            return Response({"message": "Password reset successfully"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
