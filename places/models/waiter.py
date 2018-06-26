from django.db import models
from places.models import Restaurant


class Waiter(models.Model):
    class Meta:
        db_table = 'places_waiters'

    restaurant = models.OneToOneField(Restaurant, on_delete=models.SET_NULL, primary_key=False, null=True)
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return "Waiter {} working at {}".format(self.name, self.restaurant)
