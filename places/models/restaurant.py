from django.db import models
from places.models import Place


class Restaurant(models.Model):
    class Meta:
        db_table = 'places_restaurants'

    place = models.OneToOneField(Place, on_delete=models.CASCADE, primary_key=True)
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __unicode__(self):
        return "{} the restaurant".format(self.place.name)

