from django.shortcuts import render
from blogApp.models import PostModel, CategoriaModel
from django.contrib.auth.decorators import login_required
from .forms import Formulario_blog

# Create your views here.

@login_required
def blog(request):
    
    posts = PostModel.objects.all()
    return render(request, 'blog/blog.html', {'posts': posts})

def categoria(request, categoria_id):

    categoria = CategoriaModel.objects.get(id=categoria_id)
    posts = PostModel.objects.filter(categorias=categoria)
    return render(request, 'blog/categorias.html', {'categoria': categoria, 'posts': posts})

def form_blog(request):
    if request.method=="POST":

        formulariob = Formulario_blog(request.POST, request.FILES)

        if formulariob.is_valid():

            informacionblog = formulariob.cleaned_data
            formblog = PostModel(titulo=informacionblog['titulo'], contenido=informacionblog['contenido'],
            imagen=informacionblog['imagen'], autor=informacionblog['autor'])#, categorias=informacionblog['categorias'])
            formblog.save()
            return render(request, 'blog/blog.html')
        
    else:
        formulariob = Formulario_blog()
        
    return render(request, 'blog/formblog.html', {"formulariob": formulariob})

def editar_blog(request, titulo_blog):

    eblog = PostModel.objects.get(titulo = titulo_blog)

    if request.method == 'POST':

        formulariob = Formulario_blog(request.POST, request.FILES)

        if formulariob.is_valid():

            informacionblog = formulariob.cleaned_data

            eblog.titulo = informacionblog['titulo']
            eblog.contenido = informacionblog['contenido']
            eblog.imagen = informacionblog['imagen']
            eblog.save()

            return render(request, "blog/blog.html")
    else:
        formulariob = Formulario_blog(initial={'titulo': eblog.titulo, 'contenido': eblog.contenido, 'imagen': eblog.imagen})
    
    return render(request, 'blog/editarblog.html', {'formulariob': formulariob, 'titulo_blog': titulo_blog})
