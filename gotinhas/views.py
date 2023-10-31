from django.shortcuts import render , redirect , get_object_or_404

from .models import Gotinhas
from .forms import GotinhasForm
from django.core.paginator import Paginator

def planilhaGotinhas(request):
    gotinhas_list = Gotinhas.objects.all()
    
    paginator = Paginator(gotinhas_list, 10)  # Exibe 10 alunos por página
    
    page = request.GET.get('page')
    gotinhas = paginator.get_page(page)
    return render(request, 'gotinhas/planilha.html', {'gotinhas': gotinhas})

def cadastrarGotinhas(request):
    if request.method == 'POST':
        form = GotinhasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/gotinhas/listarGotinhas/')
    else:
        form = GotinhasForm()
    return render(request, 'gotinhas/cadastro.html', {'form': form})

def confirmarGotinhas(request):
    return render(request, 'gotinhas/confirmacao.html')

def excluir_gotinha(request, gotinha_id):
    gotinha = get_object_or_404(Gotinhas, id=gotinha_id)
    gotinha.delete()
    return redirect('/gotinhas/listarGotinhas/')


# views.py

def selecionar_gotinha(request):
    gotinhas = Gotinhas.objects.all()
    if request.method == 'POST':
        gotinha_id = request.POST.get('gotinha')
        return redirect('adicionar_anotacoes', gotinha_id=gotinha_id)
    return render(request, 'gotinhas/selecionar_gotinha.html', {'gotinhas': gotinhas})



def adicionar_anotacoes(request, gotinha_id):
    gotinha = get_object_or_404(Gotinhas, id=gotinha_id)

    # Verifique se há anotações existentes
    anotacoes_existentes = gotinha.anotacoes if gotinha.anotacoes else ''

    if request.method == 'POST':
        # Obtenha as anotações do POST
        anotacoes = request.POST.get('anotacoes')

        # Salve as anotações no "gotinha"
        gotinha.anotacoes = anotacoes
        gotinha.save()

        return redirect('selecionar_gotinha')  # Redirecione para a página 'selecionar_gotinha'

    return render(request, 'gotinhas/adicionar_anotacoes.html', {'gotinha': gotinha, 'anotacoes_existentes': anotacoes_existentes})