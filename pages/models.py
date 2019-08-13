from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Page(models.Model):

    titulo = models.CharField(verbose_name = "Título", max_length = 100)
    contenido = RichTextField(verbose_name = "Contenido")
    orden = models.SmallIntegerField(verbose_name="Orden", default=0)
    fecha_creacion = models.DateTimeField(verbose_name = "Fecha de Creación", auto_now_add= True)
    fecha_actualizacion = models.DateTimeField(verbose_name = "Fecha de Modificación", auto_now= True)
  
    class Meta():

        verbose_name = 'Página'
        verbose_name_plural = 'Páginas'
        ordering = ['orden','titulo']

    def __str__(self):

        return self.titulo