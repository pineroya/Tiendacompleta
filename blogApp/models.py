from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CategoriaModel(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
    
    def __str__(self):
        return self.nombre

class PostModel(models.Model):
    titulo = models.CharField(max_length=500)
    contenido = models.TextField(max_length=200)
    imagen = models.ImageField(upload_to='blog', null = True, blank = True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    categorias = models.ManyToManyField(CategoriaModel)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
    
    def __str__(self):
        return self.titulo
