from django.shortcuts import render, get_object_or_404, redirect
from .models import Atividade, Presenca
from gotinhas.models import Gotinhas
from django.http import HttpResponse

def criar_atividade(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        professor = request.POST.get('professor')
        atividade = Atividade.objects.create(nome=nome, professor=professor)
        return redirect('atividades:listar_atividades')
    return render(request, 'atividades/criar_atividade.html')

def detalhar_atividade(request, atividade_id):
    atividade = get_object_or_404(Atividade, pk=atividade_id)
    presencas = Presenca.objects.filter(atividade=atividade)

    # Calcula o status da presença
    for presenca in presencas:
        presenca.status = "Faltou" if presenca.falta else "Presente"

    return render(request, 'atividades/detalhar_atividade.html', {'atividade': atividade, 'presencas': presencas})

def adicionar_presenca(request, atividade_id):
    atividade = get_object_or_404(Atividade, pk=atividade_id)
    if request.method == 'POST':
        aluno_id = request.POST.get('aluno')
        falta = request.POST.get('falta') == 'on'
        data = request.POST.get('data')
        turma = request.POST.get('turma')

        aluno = get_object_or_404(Gotinhas, pk=aluno_id)

        Presenca.objects.create(atividade=atividade, aluno=aluno, falta=falta, data=data, turma=turma)
        return redirect('atividades:detalhar_atividade', atividade_id=atividade.id)

    gotinhas = Gotinhas.objects.all()
    return render(request, 'atividades/adicionar_presenca.html', {'atividade': atividade, 'gotinhas': gotinhas})

def listar_atividades(request):
    atividades = Atividade.objects.all()
    return render(request, 'atividades/listar_atividades.html', {'atividades': atividades})

def excluir_atividade(request, atividade_id):
    atividade = get_object_or_404(Atividade, pk=atividade_id)
    atividade.delete()
    return redirect('atividades:listar_atividades')

