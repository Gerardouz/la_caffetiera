# Generated by Django 2.2.4 on 2019-08-07 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='servicios',
            options={'ordering': ['-fecha_creacion'], 'verbose_name': 'servicio', 'verbose_name_plural': 'servicios'},
        ),
    ]