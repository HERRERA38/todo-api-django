from django.db import models
from django.contrib.auth.models import User


class Tarea(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    fecha_caducidad = models.DateField(null=True, blank=True)
    completada = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tareas')

    class Meta:
        ordering = ['-fecha_creacion']

    def __str__(self):
        return self.nombre