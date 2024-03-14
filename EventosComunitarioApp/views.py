from .models import Evento
from django.shortcuts import render, redirect, get_object_or_404, reverse

from .models import Evento


def pagina_bienvenida(request):
    return render(request, 'paginas/bienvenida.html')

def calendario_eventos(request):
    eventos = Evento.objects.all()

    eventos_fullcalendar = []
    for evento in eventos:
        evento_dict = {
            'title': evento.titulo,
            'start': evento.fecha.isoformat(),
            'url': reverse('detalle_evento', args=[evento.id]),  # Usar reverse para generar la URL
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
    evento = get_object_or_404(Evento, pk=evento_id)
    evento.numero_asistentes += 1
    evento.save()
    return redirect('detalle_evento', evento_id=evento_id)
