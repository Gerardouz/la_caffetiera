# Generated by Django 2.2.4 on 2019-08-09 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190809_1246'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='Categorias',
            new_name='categorias',
        ),
    ]
