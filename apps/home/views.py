from django.shortcuts import render
from .models import *
from .models import Carrusel
from .forms import FormularioContacto, FormularioPrueba
from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.http import HttpResponse


def home(request):
    carrusel = Carrusel.objects.all()
    context = {
        "carrusel": carrusel
    }
    return render(request, 'home/home.html',context)

def historia(request):
    return render(request, 'home/historia.html',{})

def contactos(request):
    formulario_contacto=FormularioContacto()

    if request.method=="POST":
        formulario_contacto=FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")

            email=EmailMessage("Mensaje de app Django",
            "El usuario con nombre {} con la dirección {} escribe lo siguiente:\n\n {}".format(nombre, email, contenido), 
            '',
            ["giovanicontreras1@gmail.com"], 
            reply_to=[email])            
            email.send()                                        
        else:
            print("Error")
    return render(request, 'home/contactos.html',{'miFormulario':formulario_contacto})

def servicios(request):
    return render(request, 'home/servicios.html',{})

def materiales(request):
    if 'q' in request.GET:
        q = request.GET['q']
        print(q)
        productos = Producto.objects.filter(nombre__icontains=q)
        context = {
         "products": productos,
         "valor": request.GET['q']
        }
    elif ('categoria' in request.GET) and (request.GET['categoria']!="Todos"):
        categoria = request.GET['categoria']
        print(categoria)
        productos = Producto.objects.filter(category=categoria)
        context = {
         "products": productos,
         "categoria": request.GET['categoria']
        }        
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
    colegiatura = Colegiatura.objects.get(id=1)
    formulario_contacto=FormularioContacto()
    if request.method=="POST":
        formulario_contacto=FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            curso_nombre= request.POST.get("curso")
            contenido=request.POST.get("contenido")

            email=EmailMessage("Mensaje de app Django",
            "Curso: {} \n\n El usuario con nombre {} con la dirección {} escribe lo siguiente:\n\n {}".format(curso_nombre, nombre, email, contenido), 
            '',
            ["giovanicontreras1@gmail.com"], 
            reply_to=[email])            
            email.send()                                        
        else:
            print("Error")
    context = {
        "modulos": mod,
        "curso": curso,
        "colegiatura": colegiatura,
        'miFormulario':formulario_contacto
    }
    return render(request, 'home/curso.html',context)

def express(request, express_id):
    expres = Expres.objects.get(id=express_id)
    formulario_contacto=FormularioContacto()
    if request.method=="POST":
        formulario_contacto=FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            curso_nombre= request.POST.get("curso")
            contenido=request.POST.get("contenido")

            email=EmailMessage("Mensaje de app Django",
            "Curso: {} \n\n El usuario con nombre {} con la dirección {} escribe lo siguiente:\n\n {}".format(curso_nombre, nombre, email, contenido), 
            '',
            ["giovanicontreras1@gmail.com"], 
            reply_to=[email])            
            email.send()                                        
        else:
            print("Error")    
    context = {
        "curso" : expres,
        'miFormulario':formulario_contacto
    }
    return render(request, 'home/cursosEx.html',context)

def prueba(request):
    formulario = FormularioPrueba()
    if request.method=="POST":
        print(request.POST)
        formulario=FormularioPrueba(request.POST, request.FILES)
        if formulario.is_valid():
            nombre = formulario.cleaned_data.get("nombre")
            imagen = formulario.cleaned_data.get("img")
            obj = Prueba.objects.create(
                            nombre = nombre,
                            imagen = imagen
                            )
            obj.save()
            print(obj)
        else:
            print("Error")
    context = {
        "formulario": formulario
    }
    return render(request, 'home/prueba.html',context)

def editar(request, prueba_id):
    prueba = Prueba.objects.get(id=prueba_id)
    formulario = FormularioPrueba(initial={'nombre':prueba.nombre, 'img':prueba.imagen})

    if request.method=="POST":
        print(request.POST)
        formulario=FormularioPrueba(request.POST, request.FILES)
        if formulario.is_valid():
            prueba.nombre = formulario.cleaned_data["nombre"]          
            prueba.imagen = formulario.cleaned_data["img"]          
            prueba.save()
            print(prueba)
        else:
            print("Error")    

    context={
        "formulario":formulario,
    }
    return render(request, 'home/editar.html',context)

