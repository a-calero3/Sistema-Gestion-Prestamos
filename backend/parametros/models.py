from django.db import models

# Create your models here.
class Parametro(models.Model):
    nombre_tabla =  models.CharField(max_length=20, verbose_name='Clase de Tipo')
    codigo = models.CharField(verbose_name='Codigo', max_length=10)
    descripcion = models.CharField(verbose_name='Descripcion', max_length=50)

    class Meta:
        db_table = 'parametro'
        verbose_name = 'Parametro'
        verbose_name_plural = 'Parametros'
        constraints = [
            models.UniqueConstraint(fields=['nombre_tabla', 'codigo'], name= 'unique_nombre_tabla_codigo')
        ]
    