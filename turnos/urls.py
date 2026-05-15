from django.urls import path
from . import views

urlpatterns = [
    #responsables
    path('responsables/', views.responsables, name='responsables'),
    path('responsables/crear/', views.responsables_crear, name='responsables_crear'),
    path('responsables/editar/<int:pk>/', views.responsables_editar, name='responsables_editar'),
    path('responsables/eliminar/<int:pk>/', views.responsables_eliminar, name='responsables_eliminar'),
    # ciclos
    path('ciclos/', views.ciclos, name='ciclos'),
    path('ciclos/crear/', views.ciclos_crear, name='ciclos_crear'),
    path('ciclos/editar/<int:pk>/', views.ciclos_editar, name='ciclos_editar'),
    path('ciclos/eliminar/<int:pk>/', views.ciclos_eliminar, name='ciclos_eliminar'),
    # ciclo orden
    path('ciclos/<int:ciclo_pk>/orden/', views.ciclos_orden, name='ciclos_orden'),
    path('ciclos/<int:ciclo_pk>/orden/crear/', views.ciclos_agregar, name='ciclos_agregar'),
    path('ciclos/<int:ciclo_pk>/orden/editar/<int:pk>/', views.ciclo_orden_editar, name='ciclo_orden_editar'),
    path('ciclos/<int:ciclo_pk>/orden/eliminar/<int:pk>/', views.ciclo_orden_eliminar, name='ciclo_orden_eliminar'),
]