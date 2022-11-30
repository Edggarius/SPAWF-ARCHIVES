from django.contrib import admin
from .models import Producto, Carrusel, Curso, Modulo, Expres
# Register your models here.

admin.site.register(Producto)
admin.site.register(Carrusel)
admin.site.register(Curso)
admin.site.register(Modulo)
admin.site.register(Expres)

class Media:
    css = {
        'all': ('css/custom_ckeditor.css',)
    }
   