# blog/models.py
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField # Importamos el campo de texto enriquecido

class Post(models.Model):
    # Enlace al usuario que creó el Post
    creador = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Campos del Post
    titulo = models.CharField(max_length=200, unique=True)
    subtitulo = models.CharField(max_length=200, blank=True, null=True)
    
    # Usamos RichTextField para el contenido editable (CKEditor)
    contenido = RichTextField() 
    
    # Imagen de portada/principal del post
    imagen = models.ImageField(upload_to='posts/', blank=True, null=True)
    
    # Metadatos del Post
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Los posts más nuevos aparecerán primero
        ordering = ['-fecha_creacion']

    def __str__(self):
        return self.titulo