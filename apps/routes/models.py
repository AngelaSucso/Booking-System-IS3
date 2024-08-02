from django.db import models

from apps.buses.models import Bus


# Create your models here.
class Route(models.Model):
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    distance = models.FloatField()
    duration = models.FloatField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.origin} to {self.destination}"


class Schedule(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Route: {self.route}, Departure: {self.departure_time}"
