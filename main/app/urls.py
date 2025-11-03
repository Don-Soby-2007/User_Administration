from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('admin/login/', views.admin_login, name='admin_login'),
    path('admin/dashboard/', views.admindashboard, name='admin_dashboard'),
    path('', views.dashboard, name='dashboard'),
]
