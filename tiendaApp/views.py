from django.shortcuts import render, HttpResponse
from .models import ProductoModel, CategoriaProductoModel

# Create your views here.

def tienda(request):

    productos = ProductoModel.objects.all()
    return render(request, "tienda/tienda.html", {'productos': productos})
