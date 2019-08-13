from django.urls import path
from .views import Servicios_view

urlpatterns = [

    path('',Servicios_view,name = 'servicios'),



]