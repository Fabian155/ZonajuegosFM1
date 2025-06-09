from django.urls import path
from . import views  

urlpatterns = [
    path('', views.listarVideojuegos, name='listarVideojuegos'),  
    path('nuevoVideojuego/', views.nuevoVideojuego, name='nuevoVideojuego'),  
    path('guardarVideojuego/', views.guardarVideojuego, name='guardarVideojuego'),  
    path('eliminarVideojuego/<int:id>/', views.eliminarVideojuego, name='eliminarVideojuego'),  
    path('editarVideojuego/<int:id>/', views.editarVideojuego, name='editarVideojuego'),  
    path('procesarEdicionVideojuego/<int:id>/', views.procesarEdicionVideojuego, name='procesarEdicionVideojuego'),  
]
