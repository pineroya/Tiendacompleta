from django.shortcuts import HttpResponse, render

# Create your views here.

def home(request):
    return render(request, "webApp/home.html")
