from django.db import models


class Ox(models.Model):
    class Meta:
        db_table = 'animals_oxen'
        verbose_name_plural = 'oxen'
        ordering = ('horn_length',)

    horn_length = models.IntegerField()

