from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache, cache_control
from .models import User
from django.db.models import Q
from django.db import DatabaseError
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse, HttpResponseServerError
from django.core.paginator import Paginator
import logging

# Create your views here.

logger = logging.getLogger(__name__)


@never_cache
def login_view(request):

    try:

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

    except DatabaseError as db_err:
        logger.error(f"Database error during login : {db_err}")
        return render(request, 'error.html', {'message': 'Database error. Please try again later.'})

    except Exception as e:
        logger.exception(f"Unexpected login error {e}")
        return render(request, 'error.html', {'message': 'Something went wrong during login. '})


@never_cache
def signup_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm-password')
        email = request.POST.get('email')

        import re

        if not re.match(r'^[A-Za-z0-9_]+$', username):
            messages.error(request, "Username can only contain letters, numbers, and underscores.")
            return redirect('signup')

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
    if request.user.is_authenticated and request.user.is_admin:
        return redirect('admin_dashboard')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_active and user.is_admin:

            login(request, user)
            return redirect('admin_dashboard')

        else:
            return render(request, 'admin.html', {'error': 'Invalid admin credentials'})

    return render(request, 'admin.html')


@login_required(login_url='login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@never_cache
def dashboard_view(request):
    if request.user.is_authenticated and request.user.is_active:

        if request.user.is_admin:
            return redirect('admin_dashboard')

        return render(request, 'dashboard.html')
    else:
        return render(request, 'login.html')


@login_required(login_url='admin_login')
@never_cache
def admindashboard_view(request):
    if not request.user.is_admin:
        return redirect('login')

    query = request.GET.get('q', '')
    users = User.objects.filter(is_admin=False, is_active=True).order_by('-id')

    if query:
        users = users.filter(Q(username__icontains=query) | Q(email__icontains=query))

    paginator = Paginator(users, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'query': query,
        }

    return render(request, 'admin-dashboard.html', context)


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required(login_url='admin_login')
@never_cache
def create_user_view(request):

    if request.method == 'POST' and request.user.is_admin:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return JsonResponse({'success': False, 'message': 'Username already exists'})

        if User.objects.filter(email=email).exists():
            return JsonResponse({'success': False, 'message': 'Email already exists'})

        User.objects.create_user(username=username, email=email, password=password)
        return JsonResponse({'success': True, 'message': 'User created successfully'})

    return redirect('admin_dashboard')


@login_required(login_url='admin_login')
@never_cache
def edit_user_view(request):
    if request.method == 'POST' and request.user.is_admin:
        user_id = request.POST.get('user_id')
        username = request.POST.get('username')
        email = request.POST.get('email')
        make_admin = request.POST.get('make_admin') == 'true'

        try:
            user = User.objects.get(id=user_id, is_active=True)

            if User.objects.filter(username=username).exclude(id=user_id).exists():
                return JsonResponse({'success': False, 'message': 'Username already exists'})

            if User.objects.filter(email=email).exclude(id=user_id).exists():
                return JsonResponse({'success': False, 'message': 'Email already exists'})

            user.username = username
            user.email = email
            user.is_admin = make_admin
            user.save()

            return JsonResponse({'success': True, 'message': 'User updated successfully'})

        except User.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'User does not exist'})

    return redirect('admin_dashboard')


@login_required(login_url='admin_login')
@never_cache
def delete_user_view(request, user_id):
    if request.user.is_admin:

        user = User.objects.get(id=user_id, is_active=True)
        user.is_active = False
        user.save()

    return redirect('admin_dashboard')
