from django.db import models

from people.models.musician import Musician


class Album(models.Model):
    class Meta:
        db_table = 'people_albums'

    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stats = models.IntegerField()

