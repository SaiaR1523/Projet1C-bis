from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UploadFileForm
from django import forms
from .handle_uploaded_file import handle_uploaded_file
import pandas as pd
from csv import DictReader
from io import TextIOWrapper

# Create your views here.
@login_required (login_url='login')
def db(request):
  return render(request, 'dashboard.html', {})

@login_required (login_url='login')
def importF (request):
      if request.method == 'POST':
        data = request.FILES['data']
        print("---------------------")
        print(data)
        print("--------------------")
        # import pdb; pdb.set_trace()
        file1 = TextIOWrapper(data, encoding="ISO-8859-1", newline="")
        print("--------------------")
        df = pd.read_csv(file1, delimiter=",")
        infos1 = df.head ()
        context = {
            'n1': 2000 ,
            'n2': 3000 ,
            'n3' :infos1,
            }
        template = loader.get_template('retourImp.html')
        return HttpResponse(template.render(context, request)) 

      return render(request, 'import.html', {})