# Generated by Django 5.1.2 on 2024-11-08 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login_App', '0002_usuarios_iscliente'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='isRestaurante',
            field=models.BooleanField(default=False),
        ),
    ]