from django.urls import path
from . import views

urlpatterns = [
    path('gotinhas/cadastroGotinhas/', views.cadastrarGotinhas, name='cadastro_Gotinhas'),
    path('gotinhas/listarGotinhas/', views.planilhaGotinhas, name='planilha_Gotinhas'),
    path('gotinhas/confirmarGotinhas/', views.confirmarGotinhas, name='confirmar_Gotinhas'),

    # Defina outras URLs do seu aplicativo aqui
]
