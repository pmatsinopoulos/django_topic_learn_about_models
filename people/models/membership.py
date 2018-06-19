from django.db import models
from people.models import Person
from people.models import Group


class Membership(models.Model):
    class Meta:
        db_table = 'people_group_people'

    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField(auto_now_add=True)
    invite_reason = models.CharField(max_length=255)
