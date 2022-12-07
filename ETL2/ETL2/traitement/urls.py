from django.urls import path, include
from . import views

urlpatterns = [
    path('menuDb', views.menuDb, name='menuDb'),
    path('graph1', views.graph1, name='graph1'),
    path('graph2', views.graph2, name='graph2'),
    path('graph3', views.graph3, name='graph3')
]