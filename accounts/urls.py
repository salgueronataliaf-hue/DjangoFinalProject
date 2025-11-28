from django.urls import path
from . import views

urlpatterns = [
    # Autenticación Personalizada
    path('register/', views.register_request, name='register'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    
    # Perfil de Usuario
    path('profile/', views.profile_view, name='profile_view'),
    # CORRECCIÓN: Usar profile_edit_view
    path('profile/edit/', views.profile_edit_view, name='profile_edit'), 
]