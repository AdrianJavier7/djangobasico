from django.shortcuts import render

# Create your views here.

def verHome(request):
    return render(request, 'home.html')

def verEstudios(request):
    return render(request, 'estudios.html')