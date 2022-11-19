from django.shortcuts import render
from .models import Producto
from .models import Carrusel

def home(request):
    carrusel = Carrusel.objects.all()
    context = {
        "carrusel": carrusel
    }
    return render(request, 'home/home.html',context)




def historia(request):
    return render(request, 'home/historia.html',{})

def contactos(request):
    return render(request, 'home/contactos.html',{})

def servicios(request):
    return render(request, 'home/servicios.html',{})

def cursos(request):
    return render(request, 'home/cursos.html',{})

def curso(request):
    return render(request, 'home/curso.html',{})

def curso2(request):
    return render(request, 'home/curso2.html',{})

def curso3(request):
    return render(request, 'home/curso3.html',{})

def curso4(request):
    return render(request, 'home/curso4.html',{})

def curso5(request):
    return render(request, 'home/curso5.html',{})

def contactos(request):
    return render(request, 'home/contactos.html',{})

def materiales(request):
    productos = Producto.objects.all()
    # page = request.GET.get('page')
    # paginator = Paginator(products, 2)  Control-K + Control-C   // Descomentar Ctrl-k + Ctrl-u
    # products = paginator.get_page(page)
    context = {
        "products": productos
    }

    return render(request, 'home/materiales.html',context)


def producto(request):
    
    return render(request, 'home/producto.html',{})
