from django.shortcuts import render
from .models import Evento
from django.shortcuts import render, redirect
def pagina_bienvenida(request):
    return render(request, 'paginas/bienvenida.html')

def calendario_eventos(request):
    # Obtener todos los eventos de la base de datos
    eventos = Evento.objects.all()

    # Convertir los eventos en un formato adecuado para FullCalendar
    eventos_fullcalendar = []
    for evento in eventos:
        evento_dict = {
            'title': evento.titulo,
            'start': evento.fecha.isoformat(),  # Formato ISO 8601 para la fecha
            'url': f'/detalle_evento/{evento.id}/',  # URL para redireccionar al detalle del evento
        }
        eventos_fullcalendar.append(evento_dict)

    return render(request, 'paginas/calendarios.html', {'eventos_fullcalendar': eventos_fullcalendar})

def registro_eventos(request):
    if request.method == 'POST':
        titulo = request.POST.get('event-title')
        fecha = request.POST.get('event-date')
        ubicacion = request.POST.get('event-location')
        descripcion = request.POST.get('event-description')

        evento = Evento.objects.create(
            titulo=titulo,
            fecha=fecha,
            ubicacion=ubicacion,
            descripcion=descripcion
        )

        return redirect('detalle_evento', evento_id=evento.id)
    else:
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

def registrar_asistencia(request, evento_id):
    evento = Evento.objects.get(pk=evento_id)
    # Lógica para registrar la asistencia aquí
    return redirect('paginas/detalle_evento', evento_id=evento_id)
