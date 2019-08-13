from django.shortcuts import render

# Create your views here.

def Index(request):

    return render(request,'core/index.html')

def About(request):

    return render(request,'core/about.html')

def Store(request):

    return render(request,'core/store.html')






