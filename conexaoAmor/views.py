from django.shortcuts import render

def home(request):
    return render(request, 'conexaoAmor/home.html')

def atividades(request):
    return render(request, 'conexaoAmor/atividades.html')
