from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):

    nombre = forms.CharField(widget = forms.TextInput(
        attrs={'class':'form-control','placeholder':'Escribe tu Nombre'}
    ), min_length=3, max_length= 100)
    email = forms.EmailField(widget = forms.TextInput(
        attrs={'class':'form-control','placeholder':'Escribe tu Email'}
    ), min_length=3, max_length= 100)

    mensaje = forms.CharField(widget = forms.Textarea(
        attrs= {'class':'form-control','placeholder':'Escribe tu Mensaje','rows':3}
    ), min_length=3, max_length= 1000)

    class Meta():

        model = Contact

        fields = ['nombre','email','mensaje']



