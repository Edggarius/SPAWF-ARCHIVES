from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
   
    path('', views.home, name='home'),
    path('historia/', views.historia, name='historia'),
    path('prueba/', views.prueba, name='prueba'),
    path('servicios/', views.servicios, name='servicios'),
    path('contactos/', views.contactos, name='contactos'),
    path('cursos/', views.cursos, name='cursos'),
    path('express/<int:express_id>', views.express, name='express'),
    path('materiales/', views.materiales, name='materiales'),

    path('editar/<int:prueba_id>', views.editar, name='editar'),


    path('producto/<int:producto_id>', views.producto, name='producto'),
    path('curso/<int:curso_id>', views.curso, name='curso'),

    path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),


    
]
