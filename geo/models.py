from django.db import models

# Create your models here.

class Measurement(models.Model):
    location=models.CharField('Origen', max_length=200, default='Obispe Lepe, Logroño')
    destination= models.CharField('Destino',max_length=200)
    distance= models.DecimalField(max_digits=10, decimal_places=2)
    created= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Distance from {self.location} to {self.destination} is {self.distance} km"