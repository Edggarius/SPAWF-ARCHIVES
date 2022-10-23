from django.urls import path
from . import views

urlpatterns = [
   
    path('', views.home, name='home'),
    path('historia/', views.historia, name='historia'),
    path('servicios/', views.servicios, name='servicios'),
]
