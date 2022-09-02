"""Tiendacompleta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from webApp import urls
from serviciosApp import urls
from contactoApp import urls
from tiendaApp import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('webApp.urls')),
    path('', include('django.contrib.auth.urls')),
    path('servicios/', include('serviciosApp.urls')),
    path('blog/', include('blogApp.urls')),
    path('contacto/', include('contactoApp.urls')),
    path('tienda/', include('tiendaApp.urls')),
    path('carro/', include('carroApp.urls')),
    path('usuario/', include('autenticacionApp.urls')),
]
