# Generated by Django 2.2.4 on 2019-08-09 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190809_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categorias',
            field=models.ManyToManyField(related_name='get_posts', to='blog.Categoria', verbose_name='Categorías'),
        ),
    ]
