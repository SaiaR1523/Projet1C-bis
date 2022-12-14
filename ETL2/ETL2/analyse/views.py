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
  data = request.session.get('data')
  print (data)
  context = {'f1' : data}
  return render(request, 'dashboard.html', {})

@login_required (login_url='login')
def importF (request):
      if request.method == 'POST':
        data = request.FILES['data']
        request.session['data'] = str(data)
        print("---------------------")
        print(data)
        print("--------------------")
        # import pdb; pdb.set_trace()
        file1 = TextIOWrapper(data, encoding="ISO-8859-1", newline="")
        print("--------------------")
        #pour transformer le fichier en data frames
        df = pd.read_csv(file1, delimiter=",")
        #pour suprpimer les doublons à partir des deux premières colonnes
        df = df.drop_duplicates(['InvoiceNo','StockCode']) 
        print (df)
        #pour enlver les quantités négatives donc les avoir
        df = df.drop(df[df['Quantity'] < 0].index)
        print (df)
        #pour enlver les numéro de produits douteux 
        VS = ['M','POST', 'C2', 'DOT', 'BANK CHARGES', 'D', 'AMAZONFEE', 'S', 'gift_0001_10','gift_0001_20','gift_0001_30','gift_0001_40','gift_0001_50', 'PADS' ]
        df = df.drop(df[df['StockCode'].isin(VS)].index) # suppriemr les vlaeurs au dessus 
        print(df)
        #pour vérifier si les valeurs VS sont encore dans la data frame
        df[df['StockCode'].isin(VS)]
        print(df)
        
        infos1 = df.head()
        description = df.describe()
        context = {
            'n1': 2000 ,
            'n2': 3000 ,
            'n3' :infos1,
            'n4' : data,
            'n5' : description, 
            }
        template = loader.get_template('retourImp.html')
        return HttpResponse(template.render(context, request)) 

      return render(request, 'import.html', {})