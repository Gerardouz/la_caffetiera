from django.contrib import admin
from .models import Services

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):

    readonly_fields = ('fecha_creacion', 'fecha_actualizacion')

admin.site.register(Services,ServiceAdmin)