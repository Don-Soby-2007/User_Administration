from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache, cache_control
from .models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.


@never_cache
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_active:

            login(request, user)
            return redirect('dashboard')

        else:

            return render(request, 'login.html', {'error': 'Invalid username or password'})

    return render(request, 'login.html')


@never_cache
def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        email = request.POST.get('email')

        if password != confirm_password:
            return render(request, 'signup.html', {'error': 'Passwords do not match'})

        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error': 'Username already exists'})

        if User.objects.filter(email=email).exists():
            return render(request, 'signup.html', {'error': 'Email already exists'})

        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()

        return render(request, 'dashboard.html')
    else:
        return render(request, 'signup.html')


@never_cache
def admin_login_view(request):
    return render(request, 'admin.html')


@login_required(login_url='login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def dashboard_view(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard.html')
    else:
        return render(request, 'login.html')


@login_required
@never_cache
def admindashboard_view(request):
    return render(request, 'admin-dashboard.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
