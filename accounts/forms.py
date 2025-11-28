from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import Profile 
from django.contrib.auth.models import User # Importa el modelo User de Django

# ----------------------------------------------------
# 1. Formulario de Registro (el que te está dando error)
# ----------------------------------------------------
class UserRegisterForm(UserCreationForm):
    # Añade los campos que quieras registrar (ej. email)
    email = forms.EmailField(required=True) 

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)

# ----------------------------------------------------
# 2. Formulario de Edición de Usuario (necesario para profile_edit_view)
# ----------------------------------------------------
class UserEditForm(UserChangeForm):
    # Excluye la contraseña, que se cambia en otra vista
    password = None 
    
    class Meta:
        model = User # Debe apuntar al modelo User de Django
        # Campos que el usuario puede editar directamente (email, nombre)
        fields = ['email', 'first_name', 'last_name'] 

# ----------------------------------------------------
# 3. Formulario de Edición de Perfil (para bio y avatar)
# ----------------------------------------------------
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        # Campos del modelo Profile que se van a editar
        fields = ['bio', 'avatar'] 

        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4}),
        }