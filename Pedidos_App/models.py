from django.db import models
from Login_App.models import Usuarios
from Restaurantes_App.models import Restaurantes
# Create your models here.
class Pedidos(models.Model):
    restaurante = models.ForeignKey(Restaurantes, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    pedido = models.CharField(max_length=255, help_text='Pedido del restaurante')
    precio = models.IntegerField(help_text='Precio del pedido')
    fecha = models.DateTimeField(help_text='Fecha del pedido')
    status = models.CharField(max_length=255, help_text='Estado del pedido')
    ubicacionEntrega = models.CharField(max_length=255, help_text='Ubicación de entrega del pedido')

    def __str__(self):
        return self.pedido