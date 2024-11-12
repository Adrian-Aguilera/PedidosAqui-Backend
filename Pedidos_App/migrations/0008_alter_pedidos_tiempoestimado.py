# Generated by Django 5.1.2 on 2024-11-06 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pedidos_App', '0007_alter_pedidos_tiempoestimado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidos',
            name='tiempoEstimado',
            field=models.DateTimeField(blank=True, help_text='Tiempo estimado para el pedido que quiere el cliente', null=True),
        ),
    ]