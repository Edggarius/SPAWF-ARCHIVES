from django.urls import path
from . import views

urlpatterns = [
   
    path('home/', views.home, name='home'),
    path('historia/', views.historia, name='historia'),
    path('contactos/', views.contactos, name='contactos' ),
]
