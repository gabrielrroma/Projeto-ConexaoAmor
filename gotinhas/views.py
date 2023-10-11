from django.shortcuts import render

def planilhaGotinhas(request):
    return render(request, 'gotinhas/planilha.html')

def cadastrarGotinhas(request):
    return render(request, 'gotinhas/cadastro.html')

def confirmarGotinhas(request):
    return render(request, 'gotinhas/confirmacao.html')