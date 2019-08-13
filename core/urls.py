from django.urls import path
from .views import About,Store

urlpatterns = [

    path('about/',About, name = 'about'),
    path('store/',Store,name = 'store'),


]

