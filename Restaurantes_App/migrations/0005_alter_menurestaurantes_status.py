# Generated by Django 5.1.2 on 2024-10-20 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurantes_App', '0004_menurestaurantes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menurestaurantes',
            name='status',
            field=models.BooleanField(help_text='Estado del menu'),
        ),
    ]