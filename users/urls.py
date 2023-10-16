from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('login_adminONG/', views.login_adminONG, name='login_adminONG'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('register_adminONG/', views.register_adminONG, name='register_adminONG'),
    

]
