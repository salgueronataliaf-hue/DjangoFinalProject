from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'subtitulo', 'cuerpo', 'imagen']
        # No incluimos autor ni fecha porque se llenan solos