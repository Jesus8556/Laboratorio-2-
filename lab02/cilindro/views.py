from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'titulo' : "Calcular volumen del cilindro",
    }
    return render(request, 'cilindro/calcular.html',context)
def enviar(request):
    pi = 3.14159265359
    diametro = float(request.POST["diametro"])
    altura = float(request.POST["altura"])
    radio = diametro/2
    volumen = pi * (radio**2) * altura
    context ={
        'respuesta': volumen,
    }
    return render(request, 'cilindro/enviar.html',context)


