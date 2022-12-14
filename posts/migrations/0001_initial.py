# Generated by Django 4.0 on 2022-08-20 08:53

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('administracion', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('fecha_modificacion', models.DateField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('fecha_eliminacion', models.DateField(auto_now=True, verbose_name='Fecha de Eliminación')),
                ('titulo', models.CharField(max_length=150, verbose_name='Título del Post')),
                ('slug', models.CharField(blank=True, max_length=150, unique=True, verbose_name='Slug')),
                ('contenido', ckeditor.fields.RichTextField()),
                ('imagen_referencial', models.ImageField(upload_to='imagenes/', verbose_name='Imagen Referencial')),
                ('publicado', models.BooleanField(default=False, verbose_name='Publicado/No Publicado')),
                ('fecha_publicacion', models.DateField(verbose_name='Fecha de publicación')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='auth.user')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.categoria')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
                'ordering': ['-fecha_publicacion'],
            },
        ),
    ]
