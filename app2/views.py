from django.shortcuts import render

# Create your views here.
def lista_elementos_view(request):
    lista_elementos = [
        {'id': 1, 'nombre': 'Escenario PS1', 'categoria': 'Paisajes', 'precio': 15000, 'imagen': 'images/foto1.jpg'},
        {'id': 2, 'nombre': 'Ciudad PS1', 'categoria': 'Ciudad', 'precio': 22000, 'imagen': 'images/foto2.jpg'},
        {'id': 3, 'nombre': 'Habitacion PS1', 'categoria': 'Personas', 'precio': 35000, 'imagen': 'images/foto3.jpg'},
        {'id': 4, 'nombre': 'Niebla PS1', 'categoria': 'Fauna', 'precio': 18000, 'imagen': 'images/foto4.jpg'},
    ]
    contexto = {
        'lista_elementos': lista_elementos
    }
    return render(request, 'app2/lista.html', contexto)