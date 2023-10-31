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