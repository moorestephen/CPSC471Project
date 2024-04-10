#from django.contrib.auth.decorators import login_required, permission_required
#from django.shortcuts import render
from django.http import HttpResponse

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