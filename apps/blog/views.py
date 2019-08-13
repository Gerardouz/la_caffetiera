from django.shortcuts import render, get_object_or_404
from .models import Post, Categoria

# Create your views here.

def Blog_view(request):

    posts = Post.objects.all()

    return render(request, 'blog/blog.html', {'posts':posts})

def Categoria_view(request,Categoria_id):
    categoria = get_object_or_404(Categoria,id=Categoria_id)
    return render(request, 'blog/category.html', {'categoria':categoria})