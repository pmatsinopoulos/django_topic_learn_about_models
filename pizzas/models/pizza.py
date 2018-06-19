from django.db import models
from pizzas.models.topping import Topping


class Pizza(models.Model):
    class Meta:
        db_table = 'pizzas_pizzas'

    toppings = models.ManyToManyField(Topping)
