from django import forms
from .models import Post # Importa el modelo Post

# ----------------------------------------------------------------------
# PostForm: Formulario para crear y editar publicaciones (Posts)
# ----------------------------------------------------------------------
class PostForm(forms.ModelForm):
    """
    ModelForm basado en el modelo Post. 
    Se utiliza para las vistas PostCreateView y PostUpdateView.
    """
    
    class Meta:
        model = Post
        # Los campos que se exponen al usuario:
        # 'creador' y 'fecha_creacion' se asignan automáticamente en la vista.
        fields = ['titulo', 'subtitulo', 'contenido', 'imagen']

        # Opcional: Si quieres personalizar el campo de texto enriquecido o añadir widgets:
        # widgets = {
        #     'titulo': forms.TextInput(attrs={'placeholder': 'Título del Post'}),
        #     'contenido': forms.Textarea(attrs={'rows': 15}), # CKEditor normalmente ignora esto
        # }