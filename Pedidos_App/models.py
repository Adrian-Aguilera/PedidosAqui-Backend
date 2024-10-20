from django.db import models
from Login_App.models import Usuarios
from Restaurantes_App.models import Restaurantes, MenuRestaurantes
# Create your models here.
class Pedidos(models.Model):
    ESTADO_OPCIONES = [
        ('pendiente', 'Pendiente'),
        ('procesado', 'Procesado'),
        ('enviado', 'Enviado'),
        ('entregado', 'Entregado'),
        ('cancelado', 'Cancelado'),
    ]
    restaurante = models.ForeignKey(Restaurantes, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    menus = models.ManyToManyField(MenuRestaurantes, related_name='pedidos', help_text='Cantidad de pedidos que quiere el cliente')
    tiempoEstimado = models.DateTimeField(help_text='Tiempo estimado para el pedido que quiere el cliente', null=True)
    status = models.CharField(max_length=255, choices=ESTADO_OPCIONES, help_text='Estado del pedido', null=True, default='pendiente')
    ubicacionEntrega = models.CharField(max_length=255, help_text='Ubicación de entrega del pedido', null=True)

    def __str__(self) -> str:
        return f"Pedido de {self.cliente.correo} - Estado: {self.status}"