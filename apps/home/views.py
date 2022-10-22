from django.shortcuts import render

def home(request):
    return render(request, 'home/home.html',{})
# Create your views here.
def historia(request):
    return render(request, 'historia/historia.html',{})