from django.urls import path, include
from . import views

urlpatterns = [
    path('db', views.db, name='db'),
]