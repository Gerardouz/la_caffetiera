from django.shortcuts import render, redirect
from .forms import ContactForm
from django.urls import reverse
from django.core.mail import EmailMessage
from django.core.mail import send_mail

# Create your views here.
def Contacto_view(request):
    contactform = ContactForm()
    if (request.method == 'POST'):
        contactform = ContactForm(request.POST)
        if (contactform.is_valid()):
            nombre = request.POST.get('nombre','')
            email = request.POST.get('email','')
            mensaje = request.POST.get('mensaje','')
            #contactform.save()
            asunto = "La Caffettiera: Nuevo mensaje de contacto"
            
            """
                email = EmailMessage(
                asunto,
                "De {} <{}>\n\nEscribió:\n\n{}".format(nombre, email, mensaje),
                "no-contestar@inbox.mailtrap.io",
                ["gerardouz13@gmail.com"],
                reply_to=[email]
            )
            """
            
            send_mail(asunto+" "+nombre,mensaje,email,["gerardouz13@gmail.com"])
            #email = EmailMessage(asunto,mensaje,to=['gerardouz13@gmail.com'])
            try:
                #email.send()
                send_email(asunto+nombre,mensaje,email,["gerardouz13@gmail.com"])
            except:

                return redirect(reverse('contact')+"?0")


            return redirect(reverse('contact')+"?1")
        

    return render(request,'contact/contact.html', {'contactform':contactform})
