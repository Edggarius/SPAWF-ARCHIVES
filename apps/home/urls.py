from django.urls import path
from . import views

urlpatterns = [
   
    path('', views.historia, name='historia'),
     path('', views.home, name='home'),
]
