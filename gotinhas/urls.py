from django.urls import path
from . import views

urlpatterns = [
    path('gotinhas/cadastroGotinhas/', views.cadastrarGotinhas, name='cadastro_Gotinhas'),
    path('gotinhas/listarGotinhas/', views.planilhaGotinhas, name='planilha_Gotinhas'),
    path('gotinhas/confirmarGotinhas/', views.confirmarGotinhas, name='confirmar_Gotinhas'),
    path('gotinhas/excluir/<int:gotinha_id>/', views.excluir_gotinha, name='excluir_gotinha'),

    path('gotinhas/selecionar_gotinha/', views.selecionar_gotinha, name='selecionar_gotinha'),
    path('gotinhas/adicionar_anotacoes/<int:gotinha_id>/', views.adicionar_anotacoes, name='adicionar_anotacoes')


    # Defina outras URLs do seu aplicativo aqui
]
