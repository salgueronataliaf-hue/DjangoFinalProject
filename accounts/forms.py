from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

# Formulario de Registro (Solicita username y password)
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='Email') # Agregando email al registro

    class Meta:
        model = User
        fields = ("username", "email") # Pedir email

# Formulario para editar datos del User (nombre, apellido, email)
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

# [¡CORRECCIÓN AQUÍ!] Usar 'avatar', 'biografia', 'link', 'fecha_cumpleanos'
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'biografia', 'link', 'fecha_cumpleanos'] 
        # Asegúrate que los nombres coincidan exactamente con accounts/models.py