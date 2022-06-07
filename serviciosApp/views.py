from django.shortcuts import render, HttpResponse
from .models import ServiciosModel

# Create your views here.

def servicios(request):

    servicios = ServiciosModel.objects.all()

    return render(request, "servicios/servicios.html", {"servicios": servicios})