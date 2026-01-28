from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny
from .serializers import RegistrationSerializer, LoginSerializer
from rest_framework.parsers import FormParser
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from drf_yasg.utils import swagger_auto_schema
User = get_user_model()

# Create your views here.


class RegisterUserView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer
    queryset = User.objects.all()
    parser_classes=[FormParser]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "message": "success"
        }, status=status.HTTP_201_CREATED)


class LoginUserView(APIView):
    permission_classes = [AllowAny]
    @swagger_auto_schema(request_body=LoginSerializer)
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)
        return Response({
            "message": "login successful",
            "tokens": {"refresh-token": str(refresh),
                       "access-token": str(refresh.access_token)
                       },
        })
