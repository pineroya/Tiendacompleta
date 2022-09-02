from django.shortcuts import render, HttpResponse
from .models import ServiciosModel
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def servicios(request):

    servicios = ServiciosModel.objects.all()

    return render(request, "servicios/servicios.html", {"servicios": servicios})