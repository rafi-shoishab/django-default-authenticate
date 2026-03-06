from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.log_in, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('change-password/', views.change_password, name='change_password'),
]