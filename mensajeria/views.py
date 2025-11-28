from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from .models import Mensaje
from .forms import MensajeForm

# ----------------------------------------------------
# 1. Bandeja de Entrada (Ver Mensajes Recibidos)
# ----------------------------------------------------
@login_required
def bandeja_entrada_view(request):
    """Muestra todos los mensajes recibidos por el usuario logueado."""
    
    # Obtener mensajes recibidos por el usuario actual (destinatario)
    mensajes_recibidos = Mensaje.objects.filter(destinatario=request.user)
    
    # Opcional: Marcar todos los mensajes como leídos al ver la bandeja (si no se usa un detalle)
    # mensajes_recibidos.update(leido=True) 
    
    context = {
        'mensajes': mensajes_recibidos,
        'mensajes_enviados': Mensaje.objects.filter(remitente=request.user) # Para mostrar también los enviados
    }
    return render(request, 'mensajeria/bandeja_entrada.html', context)

# ----------------------------------------------------
# 2. Enviar Nuevo Mensaje (CBV)
# ----------------------------------------------------
class MensajeCreateView(LoginRequiredMixin, CreateView):
    """Permite a un usuario logueado crear y enviar un mensaje."""
    model = Mensaje
    form_class = MensajeForm
    template_name = 'mensajeria/mensaje_form.html'
    login_url = '/accounts/login/' # Requisito del Mixin
    
    # Redirigir a la bandeja de entrada después de enviar
    def get_success_url(self):
        messages.success(self.request, "¡Mensaje enviado exitosamente!")
        return reverse('bandeja_entrada')

    # Sobrescribir para asignar el remitente antes de guardar
    def form_valid(self, form):
        # Asigna el usuario logueado como el remitente
        form.instance.remitente = self.request.user
        return super().form_valid(form)
