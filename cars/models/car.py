from django.db import models
from cars.models.manufacturer import Manufacturer


class Car(models.Model):
    class Meta:
        db_table = 'cars_cars'

    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
