# Generated by Django 2.2.4 on 2019-08-12 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('mensaje', models.TextField(verbose_name='Mensaje')),
            ],
        ),
    ]