from django.contrib import admin
from .models import Producto, Carrusel, Curso, Modulo, Expres, Colegiatura
# Register your models here.

admin.site.register(Producto)
admin.site.register(Carrusel)
admin.site.register(Curso)
admin.site.register(Modulo)
admin.site.register(Expres)
admin.site.register(Colegiatura)

class Media:
    css = {
        'all': ('css/custom_ckeditor.css',)
    }
   