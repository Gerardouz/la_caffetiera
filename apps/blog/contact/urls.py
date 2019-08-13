from django.urls import path
from .views import Contacto_view

urlpatterns = [

    path('', Contacto_view, name = 'contact')
]