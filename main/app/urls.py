from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('admin/login/', views.admin_login_view, name='admin_login'),
    path('admin/dashboard/', views.admindashboard_view, name='admin_dashboard'),
    path('', views.dashboard_view, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('admin/create_user/', views.create_user_view, name='create_user'),
    path('admin/edit_user/', views.edit_user_view, name='edit_user'),
    path('admin/delete_user/<int:user_id>/', views.delete_user_view, name='delete_user'),
]
