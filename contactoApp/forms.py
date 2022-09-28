from django import forms
from pkg_resources import require

class ContactoForm(forms.Form):
    nombre = forms.CharField(max_length=100, label='Nombre', required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label='Email', required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    mensaje = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))