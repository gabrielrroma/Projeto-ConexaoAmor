from django.urls import path
from . import views

urlpatterns = [
    path('gotinhas/cadastroGotinhas/', views.cadastrarGotinhas, name='cadastro_Gotinhas'),
    path('gotinhas/listarGotinhas/', views.planilhaGotinhas, name='planilha_Gotinhas'),
    path('gotinhas/confirmarGotinhas/', views.confirmarGotinhas, name='confirmar_Gotinhas'),
    path('gotinhas/excluir/<int:gotinha_id>/', views.excluir_gotinha, name='excluir_gotinha'),


    # Defina outras URLs do seu aplicativo aqui
]
