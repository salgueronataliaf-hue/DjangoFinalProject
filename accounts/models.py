from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    # Relación uno a uno: Un perfil está asociado a un solo usuario
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # Campo para la biografía (TextField permite texto largo)
    bio = models.TextField(
        max_length=500, 
        blank=True,  # Permite dejar el campo vacío en formularios
        null=True    # Permite que el campo sea NULL en la base de datos
    )
    
    # Campo para la imagen de perfil (avatar)
    avatar = models.ImageField(
        upload_to='avatars/', # Las imágenes se guardarán en MEDIA_ROOT/avatars/
        null=True, 
        blank=True
    )

    def __str__(self):
        # Muestra el nombre de usuario del perfil en el panel de administración
        return f'Perfil de {self.user.username}'