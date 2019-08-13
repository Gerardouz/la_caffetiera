from django.db import models

# Create your models here.

class Services(models.Model):

    titulo = models.CharField(verbose_name = "Título",max_length = 100)
    subtitulo = models.CharField(verbose_name = "Subtitulo",max_length = 100)
    contenido = models.TextField(verbose_name = "Contenido")
    imagen = models.ImageField(verbose_name = "Imagen", upload_to = 'servicios')
    fecha_creacion = models.DateTimeField(verbose_name = "Fecha de Creación", auto_now_add= True)
    fecha_actualizacion = models.DateTimeField(verbose_name = "Fecha de Modificación", auto_now= True)

    class Meta():

        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'
        ordering = ['-fecha_creacion']

    def __str__(self):

        return self.titulo