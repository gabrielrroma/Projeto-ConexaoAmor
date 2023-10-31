from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('professor_registration/', views.professor_registration, name='professor_registration'),
    path('professor_login/', views.professor_login, name='professor_login'),
    path('professor_success/', views.professor_success, name='professor_success'),

    path('adminong_registration/', views.adminong_registration, name='adminong_registration'),
    path('adminong_login/', views.adminong_login, name='adminong_login'),
    path('adminong_success/', views.adminong_success, name='adminong_success'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
