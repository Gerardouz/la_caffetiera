"""la_caffettiera URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from apps.core.views import Index
from django.conf import settings

urlpatterns = [
    #admin
    path('admin/',admin.site.urls),
    path('',Index, name = 'index'),
    #aplicación core
    path('',include('apps.core.urls')),
    path('services/',include('apps.services.urls')),
    path('blogs/',include('apps.blog.urls')),
    path('page/',include('apps.pages.urls')),
    path('contact/',include('apps.contact.urls')),

]
if (settings.DEBUG):

    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)