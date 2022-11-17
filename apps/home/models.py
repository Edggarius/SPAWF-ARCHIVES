from django.db import models

STATUS_CHOICES = (('Disponible','Disponible'), ('No Disponible','No Disponible'))
# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    stock = models.IntegerField(null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='Disponible')
    imagen = models.FileField(null=False, upload_to=f'static/img/productos', default=None)
   # category = models.CharField(max_length=100)

   #img
        #Productos
