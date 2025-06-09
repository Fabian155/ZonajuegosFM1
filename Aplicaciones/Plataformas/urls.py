from django.urls import path
from . import views

urlpatterns = [
    path('', views.listarPlataformas, name='listarPlataformas'),  
    path('nuevaPlataforma/', views.nuevaPlataforma, name='nuevaPlataforma'),  
    path('guardarPlataforma/', views.guardarPlataforma, name='guardarPlataforma'),  
    path('eliminarPlataforma/<int:id>/', views.eliminarPlataforma, name='eliminarPlataforma'),  
    path('editarPlataforma/<int:id>/', views.editarPlataforma, name='editarPlataforma'),  
    path('procesarEdicionPlataforma/<int:id>/', views.procesarEdicionPlataforma, name='procesarEdicionPlataforma'),  
]
