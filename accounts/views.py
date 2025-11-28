from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from blog.models import Post # Importa el modelo Post
from .forms import UserRegisterForm, UserEditForm, ProfileForm
from .models import Profile # Importa el modelo Profile

# --- VISTA DE REGISTRO ---
def register_request(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # Guarda el nuevo usuario
            user = form.save()
            # Crea un perfil asociado (Signal podría hacer esto automáticamente)
            Profile.objects.create(user=user) 
            messages.success(request, "Registro exitoso. Ahora puedes iniciar sesión.")
            return redirect("login")
        messages.error(request, "Registro no válido. Información incorrecta o usuario ya existe.")
    
    form = UserRegisterForm()
    return render(request, "accounts/register.html", {"register_form": form})

# --- VISTA DE LOGIN ---
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.info(request, f"Hola {username}! Has iniciado sesión.")
                return redirect("/") # Redirige al home
            else:
                messages.error(request, "Nombre de usuario o contraseña inválidos.")
        else:
            messages.error(request, "Nombre de usuario o contraseña inválidos.")
            
    form = AuthenticationForm()
    return render(request, "accounts/login.html", {"login_form": form})

# --- VISTA DE LOGOUT ---
@login_required # Solo permite cerrar sesión si ya estás logueado
def logout_request(request):
    logout(request)
    messages.info(request, "Has cerrado sesión exitosamente.")
    return redirect("/")

# --- VISTA DE PERFIL (LECTURA) ---
@login_required
def profile_view(request):
    try:
        # Intenta obtener el perfil del usuario actual (si existe)
        profile = request.user.profile
    except Profile.DoesNotExist:
        # Si no existe, crea uno (esto no debería pasar si se usa signals o la creación en register_request)
        profile = Profile.objects.create(user=request.user)

    # CORRECCIÓN CLAVE: Usamos 'creador' para filtrar los posts, no 'author'
    user_posts = Post.objects.filter(creador=request.user).order_by('-fecha_creacion')

    context = {
        'profile': profile,
        'user_posts': user_posts,
    }
    return render(request, 'accounts/profile.html', context)

# --- VISTA DE EDICIÓN DE PERFIL ---
@login_required
def profile_edit_view(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=request.user)
    
    if request.method == 'POST':
        # Instancia ambos formularios con los datos POST y los archivos si existen (para el avatar)
        user_form = UserEditForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Tu perfil se ha actualizado correctamente.')
            return redirect('profile_view')
        else:
            messages.error(request, 'Por favor, corrige los errores en el formulario.')
    else:
        # Si es un GET, instancia los formularios con los datos actuales
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileForm(instance=profile)
    
    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'accounts/profile_edit.html', context)