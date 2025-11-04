from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache, cache_control
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.


@never_cache
def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

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
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm-password')
        email = request.POST.get('email')

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect('signup')

        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)

        return redirect('dashboard')
    else:
        return render(request, 'signup.html')


@never_cache
def admin_login_view(request):
    if request.user.is_authenticated:
        if request.user.is_admin:
            return redirect('admin_dashboard')
        return redirect('login')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_active and user.is_admin:

            login(request, user)
            return render(request, 'admin-dashboard.html')

        else:
            return render(request, 'admin.html', {'error': 'Invalid admin credentials'})

    return render(request, 'admin.html')


@login_required(login_url='login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@never_cache
def dashboard_view(request):
    if request.user.is_authenticated:

        if request.user.is_admin:
            return render(request, 'admin-dashboard.html')

        return render(request, 'dashboard.html')
    else:
        return render(request, 'login.html')


@login_required(login_url='admin_login')
@never_cache
def admindashboard_view(request):
    if request.user.is_authenticated and request.user.is_admin:
        users = User.objects.filter(is_admin=False, is_active=True).order_by('-id')
        dataset = {'users': users}
        return render(request, 'admin-dashboard.html', dataset)
    else:
        return redirect('admin_login')


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
