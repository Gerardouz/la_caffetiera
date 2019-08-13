from django.contrib import admin
from .models import Page
# Register your models here.

class PageAdmin(admin.ModelAdmin):

    readonly_fields = ('fecha_creacion','fecha_actualizacion')
    list_display = ('titulo','orden')

admin.site.register(Page,PageAdmin)