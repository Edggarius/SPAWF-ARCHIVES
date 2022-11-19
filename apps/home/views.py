from django.shortcuts import render
from .models import Producto

def home(request):
    return render(request, 'home/home.html',{})

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

