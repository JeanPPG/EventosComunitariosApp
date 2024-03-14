from django.shortcuts import render

def pagina_bienvenida(request):
    return render(request, 'paginas/bienvenida.html')

def calendario_eventos(request):
    # Lógica para mostrar el calendario de eventos
    return render(request, 'paginas/calendarios.html')