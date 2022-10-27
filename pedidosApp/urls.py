from django.urls import path
from pedidosApp import views


urlpatterns = [
    path('', views.procesar_pedido, name="procesar_pedido"),
]