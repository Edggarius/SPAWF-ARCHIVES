from django.db import models
from ckeditor.fields import RichTextField

CATEGORY_CHOICES = (('',''),('Robótica','Robótica'), ('Herramientas','Herramientas'), ('Cables, accesorios e insumos','Cables, accesorios e insumos'))
# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = RichTextField()
    precio = models.PositiveIntegerField(null=False)
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

class Curso(models.Model):
    titulo = models.CharField(max_length=100)
    imagen = models.FileField(null=False, upload_to=f'static/img/cursos', default=None)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    descripcion = RichTextField()
    

    def __str__(self):
        return self.titulo

class Modulo(models.Model):
    modulo = models.CharField(max_length=100)
    descripcion = RichTextField()
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT, null=True)
    imagen = models.FileField(null=False, upload_to=f'static/img/modulos', default=None)
    
    def __str__(self):
        return self.modulo
    
class Expres(models.Model):
    nombre = models.CharField(max_length=100) 
    descripcion = RichTextField()
    costo = models.PositiveIntegerField(null=False)
    inicio = models.DateField()
    hora = models.TimeField()
    fin = models.DateField()
    imagen = models.FileField(null=False, upload_to=f'static/img/expres', default=None)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
       return self.nombre

class Colegiatura(models.Model):
    nombre = models.CharField(max_length=100)
    semanal = models.DateField()
    sabatino = models.DateField()
    inscripcion = models.PositiveIntegerField(null=False)
    colegiatura = models.PositiveIntegerField(null=False)
    pronto = models.PositiveIntegerField(null=False)
    def __str__(self):  
        return self.nombre
    