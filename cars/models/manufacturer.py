from django.db import models


class Manufacturer(models.Model):
    class Meta:
        db_table = 'cars_manufacturers'


