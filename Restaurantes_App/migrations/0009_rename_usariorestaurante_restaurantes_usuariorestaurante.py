# Generated by Django 5.1.2 on 2024-10-20 23:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurantes_App', '0008_restaurantes_usariorestaurante'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurantes',
            old_name='usarioRestaurante',
            new_name='usuarioRestaurante',
        ),
    ]
