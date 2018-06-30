from django.db import models
from .person import Person


class Group(models.Model):
    class Meta:
        db_table = 'people_groups'

    name = models.CharField(max_length=255)
    members = models.ManyToManyField(Person, through='Membership')

    def __unicode__(self):
        return self.name
