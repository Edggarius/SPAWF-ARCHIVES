from django.shortcuts import render

def home(request):
    return render(request, 'home/home.html',{})

def historia(request):
    return render(request, 'home/historia.html',{})

def servicios(request):
    return render(request, 'home/servicios.html',{})
def materiales(request):
    return render(request, 'home/materiales.html',{})
def producto(request):
    return render(request, 'home/producto.html',{})