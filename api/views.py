from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import make_password


# Create your views here.


class UserAPI(APIView):
    def post(self, request):
        data = request.data
        if request.user.is_authenticated:
            logout(request)
        user = User.objects.filter(username=data['username']).first()
        if user:
            login(request, user)
        else:
            user = User.objects.create_user(username=data['username'],
                                            password=make_password(data['username']))
            login(request, user)
        return Response({'Status': 'OK'})


class LogoutAPI(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            return Response({'Status': 'OK'})
        else:
            return Response({'Status': 'Error', 'Message': 'User is not authenticated'})
