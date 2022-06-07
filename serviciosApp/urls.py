from django.urls import path
from serviciosApp import views


urlpatterns = [
    path('', views.servicios, name='Servicios'),
]