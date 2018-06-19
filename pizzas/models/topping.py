from django.db import models


class Topping(models.Model):
    class Meta:
        db_table = 'pizzas_toppings'
