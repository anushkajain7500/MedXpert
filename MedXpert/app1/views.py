from json.encoder import JSONEncoder
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from .models import Profile
from .serializers import ProfileSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate,login
from django.contrib import auth

@api_view(['POST'])
def register(request):
    serializer=ProfileSerializer(data=request.data)
    print(request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({"result":"Registered Successfully"})
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return JsonResponse({"result":"Registered Invalid"})

@api_view(['POST'])
@csrf_exempt
def login_view(request):
    email1=request.POST.get('email',' ')
    password1=request.POST.get('password', ' ')
    # print(email1,password1)
    # users = authenticate(request, email=email1, password=password1)
    # print(users)
    # if users is not None:
    #     login(request, users)
    if Profile.objects.filter(email=email1).filter(password=password1):
    #     # profiles=Profile.objects.filter(email=email1).filter(password=password1) 
    #     # serializer1=ProfileSerializer(profiles,many=True)
    #     login(request, users)
        return JsonResponse({"result":"Log In Successfully"})
    return JsonResponse({"result":"Log In Failed"})

@api_view(['POST'])
def logout(request):
    auth.logout(request)
    return JsonResponse({"result":"Logged out"})

