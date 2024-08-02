from django.db import models


# Create your models here.
class BusCompany(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Bus(models.Model):
    license_plate = models.CharField(max_length=20)
    bus_model = models.CharField(max_length=255)
    capacity = models.IntegerField()
    company = models.ForeignKey(BusCompany, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.license_plate
