from django.shortcuts import render, HttpResponse

# Create your views here.
'''
Inicio home/
Historia about/
Servicios services/
Visitanos store/
Contacto contac/
Blog blog/
Sample sample/


def home(request):
    return HttpResponse('Inicio')

def about(request):
    return HttpResponse('Historia')

def services(request):
    return HttpResponse('Servicios')

def store(request):
    return HttpResponse('Visitanos')

def contac(request):
    return HttpResponse('Contacto')

def blog(request):
    return HttpResponse('Blog')

def sample(request):
    return HttpResponse('Sample')
    
'''

def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def store(request):
    return render(request, 'core/store.html')



