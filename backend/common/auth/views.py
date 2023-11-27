from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView


class LoginView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return Response(data={
            "code": 200,
            "data": {
                "token": response.data['access'],
                "refreshToken": response.data['refresh'],
            },
            "message": "login success"
        })


class UserInfoView(APIView):
    def get(self, request, *args, **kwargs):
        return Response(data={
            "code": 200,
            "data": {
                "name": request.user.username
            },
            "message": "login success"
        })
