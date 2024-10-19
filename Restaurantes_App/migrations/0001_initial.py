# Generated by Django 5.1.2 on 2024-10-19 22:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurantes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre del restaurante', max_length=255)),
                ('ubicacion', models.CharField(help_text='Ubicación del restaurante', max_length=255)),
                ('descripcion', models.CharField(help_text='Descripción del restaurante', max_length=255)),
                ('telefono', models.CharField(help_text='Telefono del restaurante', max_length=255)),
                ('tipoCocina', models.CharField(help_text='Tipo de cocina del restaurante', max_length=255)),
                ('puntaje', models.IntegerField(help_text='Puntaje del restaurante')),
                ('imagen', models.CharField(help_text='Imagen del restaurante', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Pedidos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pedido', models.CharField(help_text='Pedido del restaurante', max_length=255)),
                ('precio', models.IntegerField(help_text='Precio del pedido')),
                ('fecha', models.DateTimeField(help_text='Fecha del pedido')),
                ('status', models.CharField(help_text='Estado del pedido', max_length=255)),
                ('ubicacionEntrega', models.CharField(help_text='Ubicación de entrega del pedido', max_length=255)),
                ('restaurante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Restaurantes_App.restaurantes')),
            ],
        ),
    ]