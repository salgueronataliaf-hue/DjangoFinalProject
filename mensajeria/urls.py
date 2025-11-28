from django.urls import path
from .views import bandeja_entrada_view, MensajeCreateView

urlpatterns = [
    # Bandeja de Entrada (vista FVB)
    path('', bandeja_entrada_view, name='bandeja_entrada'),
    
    # Enviar Nuevo Mensaje (vista CBV)
    path('nuevo/', MensajeCreateView.as_view(), name='enviar_mensaje'),
]