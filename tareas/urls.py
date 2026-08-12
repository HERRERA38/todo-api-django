from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import TareaViewSet, RegistroView

router = DefaultRouter()
router.register(r'tareas', TareaViewSet, basename='tarea')

urlpatterns = [
    path('registro/', RegistroView.as_view(), name='registro'),
] + router.urls