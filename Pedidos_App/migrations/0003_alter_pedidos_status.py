# Generated by Django 5.1.2 on 2024-10-20 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pedidos_App', '0002_remove_pedidos_fecha_remove_pedidos_precio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidos',
            name='status',
            field=models.CharField(choices=[('pendiente', 'Pendiente'), ('procesado', 'Procesado'), ('enviado', 'Enviado'), ('entregado', 'Entregado'), ('cancelado', 'Cancelado')], default='pendiente', help_text='Estado del pedido', max_length=255, null=True),
        ),
    ]
