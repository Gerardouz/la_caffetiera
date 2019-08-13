from django.urls import path
from .views import Blog_view, Categoria_view

urlpatterns = [

    path('',Blog_view,name = 'blogs'),
    path('category/<int:Categoria_id>/', Categoria_view, name = 'categoria')



]