from django.shortcuts import render, redirect
from .carro import Carro
from tiendaApp.models import ProductoModel



# Create your views here.

def agregar_producto(request, producto_id):
    carro = Carro(request)
    producto = ProductoModel.objects.get(id = producto_id)
    carro.agregar(producto = producto)
    return redirect("Tienda")

def eliminar_producto(request, producto_id):
    carro = Carro(request)
    producto = ProductoModel.objects.get(id = producto_id)
    carro.eliminar(producto = producto)
    return redirect("Tienda")

def restar_producto(request, producto_id):
    carro = Carro(request)
    producto = ProductoModel.objects.get(id = producto_id)
    carro.restar(producto = producto)
    return redirect("Tienda")

def limpiar_carro(request, producto_id):
    carro = Carro(request)
    carro.limpiar()
    return redirect("Tienda")
