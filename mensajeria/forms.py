from django import forms
from .models import Mensaje
from django.contrib.auth.models import User

class MensajeForm(forms.ModelForm):
    """
    Formulario usado para la vista MensajeCreateView.
    """
    # Campo personalizado para el destinatario (excluye al usuario logueado)
    destinatario = forms.ModelChoiceField(
        queryset=User.objects.all().order_by('username'),
        label="Destinatario"
    )

    class Meta:
        model = Mensaje
        fields = ['destinatario', 'contenido']
        widgets = {
            'contenido': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Escribe tu mensaje aquí...'}),
        }