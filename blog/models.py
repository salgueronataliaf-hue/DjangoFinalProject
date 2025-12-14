from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200)
    cuerpo = RichTextField()  # Campo de texto enriquecido (Requisito)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='posts_images', null=True, blank=True)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} - {self.autor}"