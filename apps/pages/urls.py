from django.urls import path
from .views import Page_view

urlpatterns = [

    path('<int:page_id>/<slug:page_slug>/', Page_view, name = 'sample'),

]