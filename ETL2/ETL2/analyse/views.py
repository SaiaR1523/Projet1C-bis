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
from .models import *
import psycopg2
from sqlalchemy import create_engine
engine = create_engine('postgresql://postgres:0000@localhost:5432/dashboard2')

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
        data = TextIOWrapper(data, encoding="ISO-8859-1", newline="")
        print("--------------------")
        
        #pour transformer le fichier en data frames
        df = pd.read_csv(data, delimiter=",")
        
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
        
        #transformer les entêtes pour que ça soit le même avec la data base 
        df = df.rename(columns={'InvoiceNo': 'numFacture', 'StockCode': 'numProduit', 
                                'Description': 'nomProduit', 'UnitPrice': 'PU', 'InvoiceDate': 'dateFact',
                                'Quantity' : 'qte','Country': 'pays' })
        # The DataFrame now has the new column names
        print(df)
        
        #importation table PAYS
        dfpays = df[['pays']]
        dfpays.drop_duplicates(keep='first',inplace=True)
        
        row_iter0 = dfpays.iterrows()
        objs1 =[
          Pays (
            pays = row ['pays'],
          )
          for index, row in row_iter0
               ]
        Pays.objects.bulk_create(objs1)

        #importation table PRODUIT
        dfproduit = df[['numProduit','nomProduit' , 'PU' ]].copy()  #pour suppriemr les doublons entre les 3 colonnes de num produit
        #description et prix unitaire
        dfproduit.drop_duplicates(subset=['numProduit'],inplace=True)
        dfproduit
        row_iter = dfproduit.iterrows()
        objs =[
          Produit (
            numproduit = row ['numProduit'],
            nomproduit = row ['nomProduit'],
            pu = row ['PU'],
          )
          for index, row in row_iter
               ]
        Produit.objects.bulk_create(objs)
        
        #importation table FACTURE
        dffacture = df [['numFacture' , 'dateFact' , 'pays']].copy()  #pour suppriemr les doublons entre les 3 colonnes de num produit
                #description et prix unitaire
        dffacture.drop_duplicates(subset=['numFacture'],inplace=True)
        dffacture["dateFact"] = pd.to_datetime(dffacture["dateFact"])
        dffacture
        
        dffacture.to_sql (
            name="FACTURE",
            con=engine,
            if_exists='append',
            index=False,
        )
        
        dfDTLFACT = df [['numFacture' , 'numProduit' , 'qte']].copy() 
        
        
        #Importation de la table FACTURE
        dfDTLFACT.to_sql (
            name="DTLFACT",
            con=engine,
            if_exists='append',
            index="false",
        )
        
        
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