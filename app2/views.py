from django.shortcuts import render

# Create your views here.
def lista_elementos_view(request):
    lista_elementos = [
        {'id': 1, 'nombre': 'Prueba de fotografia', 'categoria': 'Paisajes', 'precio': 15000},
        {'id': 2, 'nombre': 'Prueba de fotografia 2', 'categoria': 'Ciudad', 'precio': 22000},
        {'id': 3, 'nombre': 'Prueba de fotografia 3', 'categoria': 'Personas', 'precio': 35000},
        {'id': 4, 'nombre': 'Prueba de fotografia 4', 'categoria': 'Fauna', 'precio': 18000},
    ]
    contexto = {
        'lista_elementos': lista_elementos
    }
    return render(request, 'app2/lista.html', contexto)