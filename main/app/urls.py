from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('admin/login/', views.admin_login, name='admin_login'),
    path('admin/dashboard/', views.admindashboard, name='admin_dashboard'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
