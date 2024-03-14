from django.shortcuts import render

def pagina_bienvenida(request):
    return render(request, 'paginas/bienvenida.html')
