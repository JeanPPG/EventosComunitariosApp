from django.shortcuts import render
from .models import Evento

def pagina_bienvenida(request):
    return render(request, 'paginas/bienvenida.html')

def calendario_eventos(request):
    # Lógica para mostrar el calendario de eventos
    return render(request, 'paginas/calendarios.html')

from django.shortcuts import render

def registro_eventos(request):
    if request.method == 'POST':
        # Procesar el formulario enviado
        # Guardar los datos del evento en la base de datos
        # Redireccionar a la página de éxito o mostrar un mensaje de éxito
        pass
    else:
        # Renderizar el formulario vacío
        return render(request, 'paginas/registro_evento.html')

def buscar_eventos(request):
    eventos = None
    query = request.GET.get('q')
    if query:
        eventos = Evento.objects.filter(Q(titulo__icontains=query) | Q(fecha__icontains=query) | Q(ubicacion__icontains=query))
    return render(request, 'paginas/buscar_eventos.html', {'eventos': eventos, 'query': query})

def detalle_evento(request, evento_id):
    evento = Evento.objects.get(pk=evento_id)
    return render(request, 'paginas/detalle_evento.html', {'evento': evento})
