from django.shortcuts import render, redirect
from .forms import ContactoForm
from django.core.mail import EmailMessage
from django.conf import settings

# Create your views here.

def contacto(request):

    formulario_contacto = ContactoForm()

    if request.method == 'POST':

        formulario_contacto = ContactoForm(data=request.POST)

        if formulario_contacto.is_valid():
            
            nombre = request.POST.get('nombre')
            email = request.POST.get('email')
            mensaje = request.POST.get('mensaje')

            email = EmailMessage("Mensaje desde TiendaCompleta",
            "Usuario {}, con la dirección {}, escribe lo siguiente:\n\n {}".format(nombre, email, mensaje),
            "", ["mispruebas.yam@gmail.com"], reply_to=[email])

            try:
                email.send()

                return redirect("/contacto/?valido")

            except:
                return redirect("/contacto/?novalido")

    return render(request, 'contacto/contacto.html', {'miFormulario': formulario_contacto})