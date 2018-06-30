from django.db import models


class Place(models.Model):
    class Meta:
        db_table = 'places_places'

    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __unicode__(self):
        return "{} @ {}".format(self.name, self.address)

