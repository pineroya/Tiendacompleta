from django.urls import path
from blogApp import views

urlpatterns = [
    path('', views.blog, name='Blog'),
    path('categoria/<categoria_id>/', views.categoria, name='Categoria'),
]