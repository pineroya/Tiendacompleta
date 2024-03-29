from django import forms
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserCreationFormsConMail(UserCreationForm):
    email = forms.EmailField(required=True,
        help_text = "Requerido. 250 caracteres como máximo y debe ser un mail válido.")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")