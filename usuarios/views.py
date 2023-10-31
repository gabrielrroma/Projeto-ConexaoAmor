from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .models import Professor, AdminOng

def professor_registration(request):
    if request.method == 'POST':
        # Coletar os dados do POST
        username = request.POST['username']
        password = request.POST['password']

        # Verificar se o usuário já existe
        if Professor.objects.filter(username=username).exists():
            messages.error(request, 'Este nome de usuário já está em uso.')
        else:
            # Criar um novo usuário "Professor"
            professor = Professor.objects.create_user(username=username, password=password)

            # Fazer login automaticamente após o registro
            login(request, professor)

            return redirect('professor_success')
    return render(request, 'professor/professor_registration.html')

def professor_login(request):
    if request.method == 'POST':
        # Processar o formulário de login do Professor
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None and user.is_professor:
            login(request, user)
            return redirect('/conexaoAmor/atividades/')
        else:
            # Lidar com o login inválido
            messages.error(request, 'Credenciais inválidas. Certifique-se de que você é um professor.')
    return render(request, 'professor/professor_login.html')

def professor_success(request):
    return render(request, 'professor/professor_success.html')

def adminong_registration(request):
    if request.method == 'POST':
        # Coletar os dados do POST
        username = request.POST['username']
        password = request.POST['password']

        # Verificar se o usuário já existe
        if AdminOng.objects.filter(username=username).exists():
            messages.error(request, 'Este nome de usuário já está em uso.')
        else:
            # Criar um novo usuário "AdminOng"
            adminong = AdminOng.objects.create_user(username=username, password=password)

            # Fazer login automaticamente após o registro
            login(request, adminong)

            return redirect('adminong_success')
    return render(request, 'adminOng/adminong_registration.html')

def adminong_login(request):
    if request.method == 'POST':
        # Processar o formulário de login do AdminOng
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None and user.is_adminong:
            login(request, user)
            return redirect('/conexaoAmor/atividades/')
        else:
            # Lidar com o login inválido
            messages.error(request, 'Credenciais inválidas. Certifique-se de que você é um AdminOng.')
    return render(request, 'adminOng/adminong_login.html')

def adminong_success(request):
    return render(request, 'adminOng/adminong_success.html')
