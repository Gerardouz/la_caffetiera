from django.db import models

# Create your models here.

class Enlace(models.Model):

    key = models.SlugField(verbose_name = "Nombre Clave", max_length=100, unique = True)
    nombre = models.CharField(verbose_name = "Nombre", max_length = 100)
    url = models.URLField(verbose_name="URL",max_length = 200,null = True, blank = True)
    fecha_creacion = models.DateTimeField(verbose_name = "Fecha de Creación", auto_now_add= True)
    fecha_actualizacion = models.DateTimeField(verbose_name = "Fecha de Modificación", auto_now= True)
  
    class Meta():

        verbose_name = 'Enlace'
        verbose_name_plural = 'Enlaces'
        ordering = ['nombre']

    def __str__(self):

        return self.nombre