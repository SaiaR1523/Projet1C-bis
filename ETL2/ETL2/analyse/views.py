from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required (login_url='login')
def db(request):
  return render(request, 'dashboard.html', {})