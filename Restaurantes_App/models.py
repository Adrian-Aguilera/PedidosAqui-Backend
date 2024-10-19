from django.db import models

# Create your models here.
class Restaurantes(models.Model):
    nombre = models.CharField(max_length=255, help_text='Nombre del restaurante')
    ubicacion = models.CharField(max_length=255, help_text='Ubicación del restaurante')
    descripcion = models.CharField(max_length=255, help_text='Descripción del restaurante')
    telefono = models.CharField(max_length=255, help_text='Telefono del restaurante')
    tipoCocina = models.CharField(max_length=255, help_text='Tipo de cocina del restaurante')
    puntaje = models.IntegerField(help_text='Puntaje del restaurante')
    imagen = models.CharField(max_length=255, help_text='Imagen del restaurante')

    def __str__(self):
        return self.nombre

class Pedidos(models.Model):
    restaurante = models.ForeignKey(Restaurantes, on_delete=models.CASCADE)
    pedido = models.CharField(max_length=255, help_text='Pedido del restaurante')
    precio = models.IntegerField(help_text='Precio del pedido')
    fecha = models.DateTimeField(help_text='Fecha del pedido')
    status = models.CharField(max_length=255, help_text='Estado del pedido')
    ubicacionEntrega = models.CharField(max_length=255, help_text='Ubicación de entrega del pedido')

    def __str__(self):
        return self.pedido