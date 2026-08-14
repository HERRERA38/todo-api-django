from rest_framework import serializers
from .models import Tarea
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password


class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = ['id', 'nombre', 'descripcion', 'fecha_caducidad', 'completada', 'fecha_creacion', 'usuario']
        read_only_fields = ['fecha_creacion', 'usuario']

class RegistroSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )