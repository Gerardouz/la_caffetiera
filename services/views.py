from django.shortcuts import render
from .models import Services
# Create your views here.

def Servicios_view(request):

    lista = Services.objects.all()
  
    return render(request, 'services/services.html', {'lista': lista})

