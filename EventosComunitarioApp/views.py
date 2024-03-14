from django.shortcuts import render

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
