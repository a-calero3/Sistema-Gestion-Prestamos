from django.db import models
from django.contrib.auth.models import User
from parametros.models import Parametro

# Create your models here.
class PerfilUsuario(models.Model):
    # Relación uno a uno con el modelo base de Django
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuario')

    # Relacion de muchos a uno
    rol_id = models.ForeignKey(Parametro, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'perfil_usuarios'
        verbose_name = 'Perfil usuario'
        verbose_name_plural = 'Perfil Usuarios'
    
    def __str__(self):
        return f"{self.usuario.username} - {self.rol_id.descripcion}"