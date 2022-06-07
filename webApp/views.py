from django.shortcuts import HttpResponse, render

# Create your views here.

def home(request):
    return render(request, "webApp/home.html")

def tienda(request):
    return render(request, "webApp/tienda.html")

def contacto(request):
    return render(request, "webApp/contacto.html")
