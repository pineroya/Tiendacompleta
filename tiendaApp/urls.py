from django.urls import path
from tiendaApp import views

urlpatterns = [
    path('', views.tienda, name='Tienda'),
]