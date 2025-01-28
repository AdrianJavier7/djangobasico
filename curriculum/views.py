from django.shortcuts import render

# Vamos a tener las diferentes vistas y las vamos a renderizar

def verHome(request):
    return render(request, 'home.html')

def verEstudios(request):
    return render(request, 'estudios.html')

def verExperiencia(request):
    return render(request, 'experiencia.html')

def verHabilidades(request):
    return render(request, 'habilidades.html')

def verHobbies(request):
    return render(request, 'hobbies.html')

def verContacto(request):
    return render(request, 'contactos.html')