from django import forms
from .models import Mensaje

class MensajeForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        # Usamos los campos que queremos que el usuario llene: destinatario, asunto y contenido
        fields = ['destinatario', 'asunto', 'contenido']