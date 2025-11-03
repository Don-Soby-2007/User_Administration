from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')


def home(request):
    return HttpResponse("Welcome to the Home Page!")


def admin_login(request):
    return render(request, 'admin.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def admindashboard(request):
    return render(request, 'admin-dashboard.html')
