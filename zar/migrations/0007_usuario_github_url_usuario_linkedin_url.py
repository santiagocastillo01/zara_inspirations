# Generated by Django 5.0.6 on 2024-07-03 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zar', '0006_rename_acerca_de_usuario_sobre_mi'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='github_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='linkedin_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]