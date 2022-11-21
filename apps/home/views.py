from django.shortcuts import render
from .models import Producto
from .models import Carrusel
from .models import Expre

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
    expres = Expre.objects.all()
    context = {
        "express" : expres
    }
    return render(request, 'home/cursos.html',context)

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

#def express(request, express_id):
 #   try:
  ##     context = {
    #        "express": express
     #   }
      #  return render(request, 'home/express.html',context)
  #  except Expre.DoesNotExist:
   #     raise Http404('Product Not found')
def express(request):
    expres = Expre.objects.all()
    context = {
        "express" : expres
    }
    return render(request, 'home/express.html',context)