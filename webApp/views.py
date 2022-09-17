from django.shortcuts import HttpResponse, render
from carroApp.carro import Carro

# Create your views here.

def home(request):
    carro=Carro(request)
    return render(request, "web/home.html")

def acercade(request):
    return render(request, "web/acercade.html")
