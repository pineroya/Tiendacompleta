from django.shortcuts import render, HttpResponse
from .models import ProductoModel, CategoriaProductoModel
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def tienda(request):

    productos = ProductoModel.objects.all()
    return render(request, "tienda/tienda.html", {'productos': productos})
