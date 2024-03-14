from django.db import models

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateField()
    hora = models.TimeField()
    ubicacion = models.CharField(max_length=200)

    def __str__(self):
        return self.titulo
