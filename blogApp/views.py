from django.shortcuts import render
from blogApp.models import PostModel, CategoriaModel

# Create your views here.

def blog(request):

    posts = PostModel.objects.all()
    return render(request, "blog/blog.html", {'posts': posts})

def categoria(request, categoria_id):
    
    categoria = CategoriaModel.objects.get(id=categoria_id)
    posts = PostModel.objects.filter(categoria=categoria)
    return render(request, "blog/categorias.html", {'categoria': categoria, 'posts': posts})