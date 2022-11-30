from django.shortcuts import render
from .models import *
from .models import Carrusel

def home(request):
    carrusel = Carrusel.objects.all()
    context = {
        "carrusel": carrusel
    }
    return render(request, 'home/home.html',context)

def historia(request):
    return render(request, 'home/historia.html',{})

def cursosEx(request):
    return render(request, 'home/cursosEX.html',{})

def contactos(request):
    return render(request, 'home/contactos.html',{})

def servicios(request):
    return render(request, 'home/servicios.html',{})

def contactos(request):
    return render(request, 'home/contactos.html',{})

# def index(request):
#     if 'q' in request.GET:
#         q = request.GET['q']
#         data = Data.objects.filter(last_name__icontains=q)
#         multiple_q = Q(Q(first_name__icontains=q) | Q(last_name__icontains=q))
#         data = Data.objects.filter(multiple_q)
#     else:
#         data = Data.objects.all()
#     context = {
#         'data': data
#     }
#     return render(request, 'dashboard/index.html', context)


def materiales(request):
    if 'q' in request.GET:
        q = request.GET['q']
        productos = Producto.objects.filter(nombre__icontains=q)
    elif 'categoria' in request.GET:
        categoria = request.GET['categoria']
        print(categoria)
        productos = Producto.objects.filter(category=categoria)
    else:
        productos = Producto.objects.all()
    context = {
         "products": productos
    }
    return render(request, 'home/materiales.html',context)


def producto(request, producto_id):
    try:
        producto = Producto.objects.get(id=producto_id)
        context = {
            "producto": producto
        }
        return render(request,'home/producto.html',context)
    except Producto.DoesNotExist:
            raise Http404('Product Not found')

def cursos(request):
    cursos = Curso.objects.all()
    cursos_express = Expres.objects.all()
    context = {
        "cursos" : cursos,
        "cursos_express" : cursos_express
    }
    return render(request, 'home/cursos.html',context)

def curso(request, curso_id):
    mod = Modulo.objects.filter(curso_id=curso_id)    
    curso = Curso.objects.get(id=curso_id)
    
    context = {
        "modulos": mod,
        "curso": curso
    }
    return render(request, 'home/curso.html',context)

def express(request, express_id):
    expres = Expres.objects.get(id=express_id)
    context = {
        "curso" : expres
    }
    return render(request, 'home/cursosEx.html',context)