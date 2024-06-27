# Generated by Django 5.0.6 on 2024-06-26 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zar', '0002_descripcion_inspiracion_perfume'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Curso',
        ),
        migrations.DeleteModel(
            name='Descripcion',
        ),
        migrations.DeleteModel(
            name='Entregable',
        ),
        migrations.DeleteModel(
            name='Estudiante',
        ),
        migrations.DeleteModel(
            name='Inspiracion',
        ),
        migrations.DeleteModel(
            name='Profesor',
        ),
        migrations.AddField(
            model_name='perfume',
            name='descripcion',
            field=models.TextField(default='Descripción no disponible'),
        ),
        migrations.AddField(
            model_name='perfume',
            name='imagen_inspiracion',
            field=models.ImageField(default='Error.', upload_to='inspiraciones/'),
        ),
        migrations.AddField(
            model_name='perfume',
            name='imagen_perfume',
            field=models.ImageField(default='Error.', upload_to='perfumes/'),
        ),
        migrations.AddField(
            model_name='perfume',
            name='inspiracion',
            field=models.TextField(default='Inspiración no disponible'),
        ),
        migrations.AlterField(
            model_name='perfume',
            name='nombre',
            field=models.CharField(default='Nombre no disponible', max_length=100),
        ),
    ]