from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache


# Create your views here.


@never_cache
def login(request):
    return render(request, 'login.html')



@never_cache
def signup(request):
    if user.is_authenticated:
        return render(request, 'dashboard.html')
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('login')
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
