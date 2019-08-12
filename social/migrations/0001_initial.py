# Generated by Django 2.2.4 on 2019-08-09 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='enlace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.SlugField(max_length=100, unique=True, verbose_name='Nombre Clave')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('url', models.URLField(blank=True, null=True, verbose_name='URL')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificación')),
            ],
            options={
                'verbose_name': 'Enlace',
                'verbose_name_plural': 'Enlaces',
                'ordering': ['nombre'],
            },
        ),
    ]