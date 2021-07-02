from django.db import models
from django.db.models.deletion import CASCADE

class Site(models.Model):
    nombre = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Sitio'
        verbose_name_plural = "Sitios"

    def __str__(self):
        return f"{self.nombre}"

class Dispositivo(models.Model):
    sitio = models.ForeignKey(Site, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Dispositivo'
        verbose_name_plural = "Dispositivos"

    def __str__(self):
        return f"{self.nombre}"

class Medicion(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
    date = models.DateTimeField()
    temperatura = models.CharField(verbose_name="Temperatura", max_length=4, null=True)
    humedad = models.CharField(verbose_name="Humedad", max_length=4, null=True)
    presion = models.CharField(verbose_name="Presion", max_length=8, null=True)
    
    class Meta:
        verbose_name = 'Medición'
        verbose_name_plural = "Mediciones"

    def __str__(self):
        return f"Medición tomada {self.date}"




    