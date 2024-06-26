# Generated by Django 5.0.6 on 2024-06-29 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zar', '0003_delete_curso_delete_descripcion_delete_entregable_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfume_woman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen_perfume', models.ImageField(default='Error.', upload_to='perfumes_woman/')),
                ('nombre', models.CharField(default='Nombre no disponible', max_length=100)),
                ('descripcion', models.TextField(default='Descripción no disponible')),
                ('inspiracion', models.CharField(default='Nombre no disponible', max_length=100)),
                ('imagen_inspiracion', models.ImageField(default='Error.', upload_to='inspiraciones_woman/')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen_usuario', models.ImageField(default='Error.', upload_to='usuario/')),
                ('nombre', models.CharField(default='Nombre no disponible', max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='perfume',
            name='inspiracion',
            field=models.CharField(default='Nombre no disponible', max_length=100),
        ),
    ]
