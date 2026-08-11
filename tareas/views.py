from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Tarea
from .serializers import TareaSerializer


class TareaViewSet(viewsets.ModelViewSet):
    serializer_class = TareaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Tarea.objects.filter(usuario=self.request.user)