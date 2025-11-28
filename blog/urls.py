from django.urls import path
from . import views # Para home_view y about_view
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView, 
    PostUpdateView, 
    PostDeleteView
)

urlpatterns = [
    # VISTAS GENERALES (FVB)
    path('', views.home_view, name='home'),             # Usado para el home (puede ser tu lista principal)
    path('acerca-de/', views.about_view, name='about'), # Requisito: Vista "Acerca de mí"
    
    # VISTAS DE POSTS (CRUD - CBV)
    
    # 1. LISTAR POSTS (Usaremos la misma vista para la lista principal)
    path('pages/', PostListView.as_view(), name='post_list'),
    
    # 2. CREAR POST (Requiere LoginRequiredMixin)
    path('pages/nuevo/', PostCreateView.as_view(), name='post_create'),
    
    # 3. DETALLE DE POST
    path('pages/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    
    # 4. EDITAR POST (Requiere LoginRequiredMixin + UserPassesTestMixin)
    path('pages/<int:pk>/editar/', PostUpdateView.as_view(), name='post_edit'),
    
    # 5. BORRAR POST (Requiere LoginRequiredMixin + UserPassesTestMixin)
    path('pages/<int:pk>/borrar/', PostDeleteView.as_view(), name='post_delete'),
]