from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    #usuarios
    path("login/", auth_views.LoginView.as_view(template_name="usuarios/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),
    path('signup/', views.sign_up, name='signup'),
    #grupos
    path('grupos/', views.grupo, name='grupo'),
    path('grupos/crear/', views.grupo_crear, name='grupo_crear'),
    path('grupos/editar/<int:pk>/', views.grupo_editar, name='grupo_editar'),
    path('grupos/eliminar/<int:pk>/', views.grupo_eliminar, name='grupo_eliminar'),
]