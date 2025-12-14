# mensajeria/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Mensaje
from .forms import MensajeForm # Asume que este archivo forms.py existe

# Obtenemos el modelo de usuario correcto (sea el por defecto o un Profile)
User = get_user_model()

@login_required
def bandeja_entrada(request):
    # 1. Mensajes Recibidos (donde el usuario actual es el DESTINATARIO)
    mensajes_recibidos = Mensaje.objects.filter(destinatario=request.user).order_by('-fecha_envio')
    
    # 2. Mensajes Enviados (donde el usuario actual es el REMITENTE)
    mensajes_enviados = Mensaje.objects.filter(remitente=request.user).order_by('-fecha_envio')
    
    contexto = {
        'mensajes': mensajes_recibidos,          # Usado para la pestaña "Recibidos"
        'mensajes_enviados': mensajes_enviados, # ¡VARIABLE NECESARIA PARA LA PESTAÑA "Enviados"!
    }
    return render(request, 'mensajeria/bandeja_entrada.html', contexto)

@login_required
def enviar_mensaje(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.remitente = request.user
            mensaje.save()
            # Django Messages Framework (opcional, para notificar éxito)
            # from django.contrib import messages
            # messages.success(request, 'Mensaje enviado correctamente.') 
            return redirect('bandeja_entrada')
    else:
        form = MensajeForm()
        
    # Asumimos que el template es 'mensajeria/enviar.html'
    return render(request, 'mensajeria/enviar.html', {'form': form})