from django.db import models

CATEGORY_CHOICES = (('',''),('Robótica','Robótica'), ('Herramientas','Herramientas'), ('Cables, accesorios e insumos','Cables, accesorios e insumos'))
# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    stock = models.PositiveIntegerField(null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default=None)
    imagen = models.FileField(null=False, upload_to=f'static/img/productos', default=None)

    
    def __str__(self):
        return self.nombre
    



   #img
        #Productos


img_path = 'static/img'
class Carrusel(models.Model):
 image = models.ImageField(upload_to=f'{img_path}Carrusel')
 def __str__(self):
    return self.image.name