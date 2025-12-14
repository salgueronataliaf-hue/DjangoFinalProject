from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars', null=True, blank=True, default='avatars/default.png')
    biografia = models.TextField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    fecha_cumpleanos = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"