from django.urls import path
from . import views

urlpatterns = [
   
    path('', views.home, name='home'),
    path('historia/', views.historia, name='historia'),
    path('servicios/', views.servicios, name='servicios'),
    path('contactos/', views.contactos, name='contactos'),
    path('cursos/', views.cursos, name='cursos'),
    path('express/<int:express_id>', views.express, name='express'),
    path('materiales/', views.materiales, name='materiales'),
    path('producto/<int:producto_id>', views.producto, name='producto'),
    path('curso/<int:curso_id>', views.curso, name='curso'),
    
]
