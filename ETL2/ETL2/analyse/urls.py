from django.urls import path, include
from . import views

urlpatterns = [
    path('db', views.db, name='db'),
    path('importF', views.importF, name='importF'),
    path('menuDb', views.menuDb, name='menuDb'),
    path('graph1', views.graph1, name='graph1'),
    path('graph1-10', views.graph10, name='top10'),
    path('graph3', views.graph3, name='graph3')
]