# Generated by Django 5.1.2 on 2024-11-06 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pedidos_App', '0006_rename_menucount_pedidos_menus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidos',
            name='tiempoEstimado',
            field=models.DateTimeField(auto_now=True, help_text='Tiempo estimado para el pedido que quiere el cliente', null=True),
        ),
    ]
