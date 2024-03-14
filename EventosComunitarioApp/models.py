from django.db import models

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    fecha = models.DateField()
    ubicacion = models.CharField(max_length=100)
    descripcion = models.TextField()
    numero_asistentes = models.IntegerField(default=0)

    def __str__(self):
        return self.titulo


app_label = 'EventosComunitarioApp'