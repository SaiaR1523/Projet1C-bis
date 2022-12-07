from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

# Create your views here.
@login_required (login_url='login')
def menuDb(request):
  return render(request, 'menuDb.html', {})

@login_required (login_url='login')
def graph1(request):
  return render(request, 'graph1.html', {})

@login_required (login_url='login')
def graph2(request):
  return render(request, 'graph2.html', {})

@login_required (login_url='login')
def graph3(request):
  return render(request, 'graph3.html', {})