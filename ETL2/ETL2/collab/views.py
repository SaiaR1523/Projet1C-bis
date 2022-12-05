from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

def login_user(request):
    if request.method == "POST" :   #ici c'est le deuxième chargement de la page 
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:     #si c'est un utilisateur ==> redirigé vers page dashoboard
            login(request, user)
            return redirect('db')
        else:    #si c'est pas un utilisateur  ==> redigirgé vers page de connexion
            messages.success (request, ("il y a eu une erreur, veilleuz retenter de nouveau") )
            return redirect('login')
            
    return render(request, 'login.html', {})  #ici c'est le premier chargement de la page

def logout_user(request):
    logout(request)
    messages.success(request, ("Session deconnectée"))
    return redirect('login')
