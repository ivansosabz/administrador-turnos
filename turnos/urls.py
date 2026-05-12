from django.urls import path
from . import views

urlpatterns = [
    path('responsables/', views.responsables, name='responsables'),
    path('responsables/crear/', views.responsables_crear, name='responsables_crear'),
    path('responsables/editar/<int:pk>/', views.responsables_editar, name='responsables_editar'),
    path('responsables/eliminar/<int:pk>/', views.responsables_eliminar, name='responsables_eliminar'),
]