from django.urls import path
from .views import VRegistro
from autenticacionApp import views


urlpatterns = [
    path('', VRegistro.as_view(), name='Registro'),
    path('cerrar_sesion', views.cerrar_sesion, name='cerrar_sesion'),
    path('loguear', views.loguear, name='loguear')
]