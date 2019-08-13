from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.

class Categoria(models.Model):

    nombre = models.CharField("Nombre",max_length = 100, blank = False, null = False)
    fecha_creacion = models.DateTimeField(verbose_name = "Fecha de Creación", auto_now_add= True)
    fecha_actualizacion = models.DateTimeField(verbose_name = "Fecha de Modificación", auto_now= True)

    class Meta():

        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['-fecha_creacion']

    def __str__(self):

        return self.nombre


class Post(models.Model):

    titulo = models.CharField(verbose_name = "Título", max_length = 100, blank = False, null = False)
    contenido = RichTextField(verbose_name = "Contenido")
    fecha_publicacion = models.DateTimeField(verbose_name = "Fecha de Publicación", default = now)
    imagen = models.ImageField(verbose_name = "Imagen", upload_to = "blog", blank = True, null = True )
    autor = models.ForeignKey(User, on_delete = models.CASCADE,verbose_name = "Autor")
    categorias = models.ManyToManyField(Categoria,verbose_name = "Categorías",related_name="get_posts")

    fecha_creacion = models.DateTimeField(verbose_name = "Fecha de Creación", auto_now_add= True)
    fecha_actualizacion = models.DateTimeField(verbose_name = "Fecha de Modificación", auto_now= True)

    class Meta():

        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'
        ordering = ['-fecha_creacion']

    def __str__(self):

        return self.titulo
