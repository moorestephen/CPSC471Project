#from django.contrib.auth.decorators import login_required, permission_required
#from django.shortcuts import render

def login_page(request):
    return HttpResponse("<h1>Login Page<h1>")

def swimmer_dashboard(request):
    #Swimmer-specific view logic
    return HttpResponse("<h1>Swimmer Dashboard<h1>")

def coach_dashboard(request):
    #Coach-specific view logic
    return HttpResponse("<h1>Coach Dashboard<h1>")

def admin_dashboard(request):
    #Admin-specific view logic
    return HttpResponse("<h1>Admin Dashboard<h1>")

from .models2 import DatabaseClub
from .serializers import ClubSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status, mixins, generics
from rest_framework.views import APIView

class ClubList(APIView):
    def get(self, request):
        clubs = DatabaseClub.objects.all()
        serializer = ClubSerializer(clubs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ClubSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)