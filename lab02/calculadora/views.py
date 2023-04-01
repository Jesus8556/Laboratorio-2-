from django.shortcuts import render

# Create your views here.
def index(request):
    context ={
        'titulo': "Bienvenido a mi calculadora",
    }
    return render(request, 'calculadora/calculadora.html',context)
def enviar(request):
    n1 = float(request.POST['numero1'] )
    n2 = float(request.POST['numero2'] )
    operacion = request.POST['operacion']
    if operacion == 'sumar':
        resultado = n1+n2
        simbolo = "+"
    elif operacion == 'restar':
        resultado = n1-n2
        simbolo = "-"
    elif operacion == 'multiplicar':
        resultado = n1*n2
        simbolo = "*"
    elif operacion == 'dividir':
        resultado = n1/n2
        simbolo = "/"
    context={
        'nombreoperacion' : request.POST['operacion'],
        'titulo' : "Respuesta",
        'numero1' : request.POST['numero1'],
        'simbolo' : simbolo,
        'numero2' : request.POST['numero2'],
        'respuesta' : resultado,
    }
    return render(request, 'calculadora/respuesta.html',context)
