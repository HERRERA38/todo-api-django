from rest_framework import serializers
from .models import Tarea


class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = ['id', 'nombre', 'descripcion', 'fecha_caducidad', 'completada', 'fecha_creacion', 'usuario']
        read_only_fields = ['fecha_creacion']