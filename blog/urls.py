# blog/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # 1. LISTADO (Pages)
    path('', views.PostListView.as_view(), name='post_list'), 
    
    # 2. CREAR POST (Funciona correctamente)
    path('new/', views.PostCreateView.as_view(), name='post_create'),
    
    # 3. DETALLE DEL POST (DEBE ser dinámica para que funcione el enlace)
    path('<int:pk>/', views.PostDetailView.as_view(), name='post_detail'), 
    
    # 4. ACTUALIZAR POST (Necesaria para los botones en post_detail.html)
    path('<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_update'),
    
    # 5. ELIMINAR POST (Necesaria para los botones en post_detail.html)
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
]