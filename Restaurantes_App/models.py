from django.db import models

# Create your models here.
class Restaurantes(models.Model):
    nombre = models.CharField(max_length=255, help_text='Nombre del restaurante')
    ubicacion = models.CharField(max_length=255, help_text='Ubicación del restaurante')
    descripcion = models.CharField(max_length=255, help_text='Descripción del restaurante')
    telefono = models.CharField(max_length=255, help_text='Telefono del restaurante')
    tipoCocina = models.CharField(max_length=255, help_text='Tipo de cocina del restaurante')
    puntaje = models.IntegerField(help_text='Puntaje del restaurante')
    imagen = models.FileField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.nombre

class MenuRestaurantes(models.Model):
    restaurante = models.ForeignKey(Restaurantes, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255, help_text='Titulo del menu')
    nombre = models.CharField(max_length=255, help_text='Nombre del menu')
    precio = models.IntegerField(help_text='Precio del menu')
    fecha = models.DateTimeField(help_text='Fecha del menu')
    status = models.BooleanField(help_text='Estado del menu', default=False)
    imagen = models.FileField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.titulo
