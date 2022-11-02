from django.urls import path
from . import views

urlpatterns = [
   
    path('home/', views.home, name='home'),
    path('historia/', views.historia, name='historia'),
    path('servicios/', views.servicios, name='servicios'),
    path('contactos/', views.contactos, name='contactos'),
    path('cursos/', views.cursos, name='cursos'),
    path('curso/', views.curso, name='curso'),
    path('curso2/', views.curso2, name='curso2'),
    path('curso3/', views.curso3, name='curso3'),
    path('curso4/', views.curso4, name='curso4'),
    path('curso5/', views.curso5, name='curso5'),

    
]
