from django.shortcuts import render

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
def materiales(request):
    return render(request, 'home/materiales.html',{})
def producto(request):
    return render(request, 'home/producto.html',{})
