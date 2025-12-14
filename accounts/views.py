from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as django_login, logout as django_logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required # Requisito: Decorador
from django.contrib import messages
from .models import Profile
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

# Función simple de inicio
def home(request):
    return render(request, 'accounts/home.html') 

# Función simple "Acerca de mí" (Ruta about/)
def about(request):
    return render(request, 'accounts/about.html') 

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            django_login(request, user)
            # Redirige a la página principal después de login
            return redirect('home') 
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def register_request(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # El Profile se crea automáticamente gracias a la "signal" en models.py
            django_login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def logout_request(request):
    django_logout(request)
    # messages.info(request, "Has cerrado sesión exitosamente.") # Puedes usar esto si lo necesitas
    return redirect('login')


# Decorador @login_required (Cumple requisito)
@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html')

# Decorador @login_required y manejo de formularios
@login_required
def editar_perfil(request):
    if request.method == 'POST':
        # Nota: request.FILES es esencial para subir el avatar
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Tu perfil ha sido actualizado.')
            return redirect('profile_view')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
        
    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'accounts/profile_edit.html', context)

# [¡LA FUNCIÓN QUE FALTABA!]
@login_required
def change_password(request):
    if request.method == 'POST':
        # Nota: PasswordChangeForm requiere el usuario actual como primer argumento
        form = PasswordChangeForm(request.user, request.POST) 
        if form.is_valid():
            user = form.save()
            # Esta función evita que el usuario se desloguee tras cambiar la contraseña
            update_session_auth_hash(request, user) 
            messages.success(request, 'Tu contraseña ha sido actualizada.')
            return redirect('profile_view')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/password_change_form.html', {'form': form})
# accounts/views.py (Añadir al final del archivo)

# La función que maneja la edición del perfil (User + Profile)
@login_required
def editar_perfil(request):
    # Asegúrate de que el objeto Profile exista. 
    # Si la "signal" no lo ha creado, lo creamos manualmente aquí para evitar errores.
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        # Instanciamos los formularios con los datos POST y los archivos (request.FILES)
        # y las instancias existentes del Usuario y el Perfil.
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Tu perfil ha sido actualizado exitosamente.')
            # Redirigimos a la vista del perfil (que aún no hemos revisado)
            return redirect('profile_view') 
        else:
            messages.error(request, 'Error al guardar los cambios. Revisa los campos.')
            
    else:
        # Si es un GET request, mostramos los formularios con los datos actuales
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    # **Asegúrate de que este template exista:** accounts/templates/accounts/editar_perfil.html
    return render(request, 'accounts/editar_perfil.html', context)

@login_required
def profile_view(request):
    """Muestra la vista del perfil de usuario."""
    # Puedes añadir la lógica para obtener el profile aquí
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = None

    return render(request, 'accounts/profile_view.html', {'profile': profile})


@login_required
def change_password(request):
    """Permite al usuario cambiar su contraseña."""
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Importante para mantener la sesión
            messages.success(request, 'Tu contraseña fue actualizada exitosamente!')
            return redirect('profile_view')
        else:
            messages.error(request, 'Por favor, corrige los errores debajo.')
    else:
        form = PasswordChangeForm(request.user)
    
    return render(request, 'accounts/change_password.html', {'form': form})