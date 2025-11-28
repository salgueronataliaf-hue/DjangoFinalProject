from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required # Decorador requerido por consigna

from .models import Post
from .forms import PostForm # Necesario para las vistas Create/Update

# ----------------------------------------------------
# 1. Vistas Fijas (Usaremos Funciones Basadas en Vista - FVB)
# ----------------------------------------------------

def home_view(request):
    """Muestra la página de inicio con la lista de posts."""
    context = {}
    return render(request, 'blog/home.html', context)

def about_view(request):
    """Muestra la página 'Acerca de mí'."""
    context = {}
    return render(request, 'blog/about.html', context)

# ----------------------------------------------------
# 2. CRUD de Posts (Usaremos Clases Basadas en Vista - CBV)
# ----------------------------------------------------

# VISTA DE LISTADO (Requisito CBV #1)
class PostListView(ListView):
    """Muestra la lista de todos los Posts."""
    model = Post
    template_name = 'blog/post_list.html' # Debes crear este template
    context_object_name = 'posts'
    ordering = ['-fecha_creacion']
    paginate_by = 10 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Mensaje para 'No hay páginas aún'
        if not context['posts'] and not self.request.GET.get('q'):
            context['no_posts_message'] = "¡Oops! Aún no hay publicaciones en el blog."
        return context

# VISTA DE DETALLE
class PostDetailView(DetailView):
    """Muestra el detalle de un Post."""
    model = Post
    template_name = 'blog/post_detail.html' # Debes crear este template
    context_object_name = 'post'

# VISTA DE CREACIÓN (Requisito CBV #2 + Mixin)
class PostCreateView(LoginRequiredMixin, CreateView):
    """Permite a un usuario logueado crear un nuevo Post."""
    # Requisito de Consigna: Uso de Mixin (LoginRequiredMixin)
    
    model = Post
    form_class = PostForm
    template_name = 'blog/post_create_form.html'
    success_url = reverse_lazy('post_list') # Redirigir al listado después de crear
    login_url = '/accounts/login/' # Redirigir al login si no está autenticado

    # Sobrescribe para asignar el creador antes de guardar
    def form_valid(self, form):
        form.instance.creador = self.request.user
        return super().form_valid(form)

# VISTA DE EDICIÓN (Requiere que el usuario sea el autor del post)
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Permite editar un Post solo si eres el creador."""
    model = Post
    form_class = PostForm
    template_name = 'blog/post_update_form.html' # Debes crear este template
    success_url = reverse_lazy('post_list')
    login_url = '/accounts/login/'

    # Requisito de Mixin: UserPassesTestMixin para verificar permisos
    def test_func(self):
        post = self.get_object()
        return post.creador == self.request.user

# VISTA DE BORRADO (Requiere que el usuario sea el autor del post)
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Permite borrar un Post solo si eres el creador."""
    model = Post
    template_name = 'blog/post_confirm_delete.html' # Debes crear este template
    success_url = reverse_lazy('post_list')
    login_url = '/accounts/login/'

    # Requisito de Mixin: UserPassesTestMixin para verificar permisos
    def test_func(self):
        post = self.get_object()
        return post.creador == self.request.user

# ----------------------------------------------------
# 3. Vista Adicional (Requisito de Decorador ya cumplido)
# ----------------------------------------------------
# Nota: La vista de perfil en accounts/views.py ya usa el decorador @login_required.