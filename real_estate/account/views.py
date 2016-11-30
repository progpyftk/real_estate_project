from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, UserRegistrationForm
from django import views
from django.contrib.auth.models import User
from django.contrib import messages



def user_login(request):
	form = LoginForm(request.POST or None)
	# esse storage serve pra apagar a mensagem, para q se o cara atualizar a pagina a msg nao ficar aparecendo. 
	storage = messages.get_messages(request)
	storage.used = True
	if request.POST and form.is_valid():
		user = form.login(request)
		if user:
			label=login(request, user)
			return render(request, 'account/index.html')
	return render(request, 'account/login.html', {'form': form })

# usando esse decorator quando o cara tentar acessar uma página, se ele não estiver logado, manda ele pro login 
# e depois de logado ele volta pra pagina que tentou acessar


def index(request):
	return render(request, 'account/index.html', {'section': 'home'})

def base(request):
	return render(request, 'account/base.html')

def register(request):
	if request.method == 'POST':
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			user = User.objects.create_user(username=form.cleaned_data['username'], 
										password=form.cleaned_data['password'],
										email=form.cleaned_data['email'],
										first_name=form.cleaned_data['first_name'],
										last_name=form.cleaned_data['last_name'])
			return render(request, 'account/register_sucess.html')
	else:
		print("Renderizei o GET")
		form = UserRegistrationForm()
	return render (request, 'account/register.html', {'form':form})