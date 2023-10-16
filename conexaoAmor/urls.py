from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('conexaoAmor/atividades/', views.atividades, name='atividades'),
    # Defina outras URLs do seu aplicativo aqui
]
