from django.shortcuts import render , redirect
from django.contrib.auth import login, authenticate , logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

from .forms import RegisterAdminONGForm


# Create your views here.

def login_adminONG(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('/conexaoAmor/atividades/')
		else:
			messages.success(request, ("Usuário ou senha incorretos!"))	
			return redirect('/users/login_adminONG')	


	else:
		return render(request, 'adminONG/login_adminONG.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, ("Logout realizado com sucesso!"))
    return redirect('home')
    

def register_adminONG(request):
	if request.method == "POST":
		form = RegisterAdminONGForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, ("Registration Successful!"))
			return redirect('/users/login_adminONG')
	else:
		form = RegisterAdminONGForm()

	return render(request, 'adminONG/register_adminONG.html', {
		'form':form,
		})
