from django.urls import path
from . import views

urlpatterns = [
    path('cadastroGotinhas/', views.cadastrarGotinhas, name='cadastro_Gotinhas'),
    path('listarGotinhas/', views.planilhaGotinhas, name='planilha_Gotinhas'),
    path('confirmarGotinhas/', views.confirmarGotinhas, name='confirmar_Gotinhas'),
    # Defina outras URLs do seu aplicativo aqui
]
