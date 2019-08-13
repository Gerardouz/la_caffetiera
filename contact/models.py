from django.db import models

# Create your models here.

class Contact(models.Model):

    nombre = models.CharField(verbose_name = "Nombre", max_length = 100)
    email = models.EmailField(verbose_name = "Email")
    mensaje = models.TextField(verbose_name="Mensaje")
