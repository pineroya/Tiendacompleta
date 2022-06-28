from django import forms
from pkg_resources import require

class ContactoForm(forms.Form):
    nombre = forms.CharField(max_length=100, label='Nombre', required=True)
    email = forms.EmailField(label='Email', required=True)
    mensaje = forms.CharField(widget=forms.Textarea)