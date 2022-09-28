from traceback import format_stack
from django import forms
from PIL import Image
from .models import PostModel, CategoriaModel

class Formulario_blog(forms.ModelForm):

    class Meta:
        model = PostModel
        fields = ['titulo', 'contenido', 'imagen', 'autor']
    
    titulo = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control'}))
    contenido = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'class':'form-control'}))
    imagen = forms.ImageField(required=True)
    autor = forms.TextInput()
    categorias = forms.TextInput() #de momento no funciona

'''class Formulario_categoria(forms.ModelForm):

    class Meta:
        model = CategoriaModel
        fields = ['nombre']

    nombre = forms.TextInput()'''