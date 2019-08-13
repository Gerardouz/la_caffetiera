from django.shortcuts import render, redirect
from .forms import ContactForm
from django.urls import reverse
from django.core.mail import EmailMessage

# Create your views here.
def Contacto_view(request):
    contactform = ContactForm()
    if (request.method == 'POST'):
        contactform = ContactForm(request.POST)
        if (contactform.is_valid()):
            nombre = request.POST.get('nombre','')
            email = request.POST.get('email','')
            mensaje = request.POST.get('mensaje','')
            contactform.save()

            email = EmailMessage(
                "La Caffettiera: nuevo mensaje de contacto ",
                "de {}<\n\nEscribió:\n\n{}".format(nombre, email, mensaje),
                "no-contestar@inbox.mailtrap.io",
                ['gerardouz-3bac3b@inbox.mailtrap.io'],
                reply_to=[email]
            )
            try:
                email.send()
            except:

                return redirect(reverse('contact')+"?0")


            return redirect(reverse('contact')+"?1")
        

    return render(request,'contact/contact.html', {'contactform':contactform})
