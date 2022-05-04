from multiprocessing import AuthenticationError
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,request
from .forms import UserRegisterForm,PostFormulario
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from django.contrib.auth.models import User


# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')

def post(request):
    return render(request, 'post.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

@login_required
def publicar(request):
    return render(request, 'publicar.html')


def login_request(request):

    if request.method == 'POST':

        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            
            username = form.cleaned_data.get('username')
            contrasena = form.cleaned_data.get('contrasena')
            user = authenticate(username=username,password=contrasena)
            

            if user is not None:
                login(request, user)
                return render(request, 'inicio.html', {'mensaje':f'Bienvenido {username}'})
            else:
                return render(request, 'inicio.html', {'mensaje':'Error, Datos Incorrectos'})
            

    else:
        form = AuthenticationForm()

    return render(request, 'sign.html', {'form':form})


def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			messages.success(request, f'Usuario {username} creado')
			return redirect('inicio')
	else:
		form = UserRegisterForm()

	context = { 'form' : form }
	return render(request, 'registro.html', context)


@login_required
def post(request):
	current_user = get_object_or_404(User, pk=request.user.pk)
	if request.method == 'POST':
		form = PostFormulario(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.user = current_user
			post.save()
			messages.success(request, 'Post enviado')
			return redirect('inicio')
	else:
		form = PostFormulario()
	return render(request, 'post.html', {'form' : form })

def feed(request):
	posts = post.objects.all()

	context = { 'posts': posts}
	return render(request, 'feed.html', context)