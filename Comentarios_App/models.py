from django.db import models
from Login_App.models import Usuarios
from Restaurantes_App.models import Restaurantes, MenuRestaurantes
# Create your models here.

#hacer una tabla de comentarios para cada uno, restauarante y menus

class ComentariosRestaurantes(models.Model):
    restaurante = models.ForeignKey(Restaurantes, on_delete=models.CASCADE, null=True)
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE, null=True)
    comentario = models.CharField(max_length=255, help_text='Comentario del usuario')
    fecha = models.DateTimeField(auto_now_add=True)
    puntaje = models.IntegerField(help_text='Puntaje del comentario', null=True, default=0)

    def __str__(self):
        return f"Comentario de {self.usuario.correo} en {self.restaurante.nombre}"
