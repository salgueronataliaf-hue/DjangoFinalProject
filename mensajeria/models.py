from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Mensaje(models.Model):
    """
    Representa un mensaje privado entre dos usuarios.
    """
    # Usamos la clave foránea (ForeignKey) para relacionar con el modelo User de Django
    # on_delete=models.CASCADE asegura que si el usuario es borrado, sus mensajes también.
    remitente = models.ForeignKey(User, related_name='mensajes_enviados', on_delete=models.CASCADE)
    destinatario = models.ForeignKey(User, related_name='mensajes_recibidos', on_delete=models.CASCADE)
    
    contenido = models.TextField(max_length=500)
    
    fecha_envio = models.DateTimeField(default=timezone.now)
    
    # Campo para saber si el mensaje ya fue leído (opcional, pero útil)
    leido = models.BooleanField(default=False)

    class Meta:
        # Los mensajes se ordenan del más nuevo al más viejo
        ordering = ['-fecha_envio']
        verbose_name = "Mensaje"
        verbose_name_plural = "Mensajes"

    def __str__(self):
        return f"De {self.remitente.username} a {self.destinatario.username}"