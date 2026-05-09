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
    path('grupos/crear/', views.crear_grupo, name='crear_grupo'),
    # path('grupos/editar/<int:pk>/', views.editar_grupo, name='editar_grupo'),
    # path('grupos/eliminar/<int:pk>/', views.eliminar_grupo, name='eliminar_grupo'),
]
# se le agrega _view porque django ya tiene funciones login y logut