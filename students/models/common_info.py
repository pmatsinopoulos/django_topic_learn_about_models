from django.db import models


class CommonInfo(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    