from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login

# Create your views here.


@never_cache
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username).first()

        if user and user.check_password(password):

            auth_login(request, user)
            return render(request, 'dashboard.html')

        else:

            return render(request, 'login.html', {'error': 'Invalid username or password'})

    return render(request, 'login.html')


@never_cache
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error': 'Username already exists'})

        if User.objects.filter(email=email).exists():
            return render(request, 'signup.html', {'error': 'Email already exists'})

        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()

        return render(request, 'login.html')
    else:
        return render(request, 'signup.html')


@never_cache
def admin_login(request):
    return render(request, 'admin.html')


@login_required
@never_cache
def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard.html')
    else:
        return render(request, 'login.html')


@login_required
@never_cache
def admindashboard(request):
    return render(request, 'admin-dashboard.html')
