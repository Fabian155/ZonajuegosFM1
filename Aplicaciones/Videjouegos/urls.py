from django.urls import path
from. import views

urlpatterns = [
    path('', views.inicio1, name='inicioJ'),
    path('NuevoJuego', views.NuevoJuego, name='NuevoJuego'), 
    path('GuardarJ', views.GuardarJ), 
    path('EliminarJ/<id>', views.EliminarJuego),
    path('editarJ/<id>', views.editarJuego),
    path('GuardarEdicion1', views.GuardarEdicion1),
]