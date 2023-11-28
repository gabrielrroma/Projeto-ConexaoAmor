from django.urls import path
from . import views

app_name = 'atividades'

urlpatterns = [
    path('listar_atividades/', views.listar_atividades, name='listar_atividades'),
    path('criar_atividade/', views.criar_atividade, name='criar_atividade'),
    path('detalhar/<int:atividade_id>/', views.detalhar_atividade, name='detalhar_atividade'),
    path('adicionar_presenca/<int:atividade_id>/', views.adicionar_presenca, name='adicionar_presenca'),
    path('excluir_atividade/<int:atividade_id>/', views.excluir_atividade, name='excluir_atividade'),


]
