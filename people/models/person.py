from django.db import models


class Person(models.Model):
    class Meta:
        db_table = 'people_people'

    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    shirt_size = models.CharField(max_length=1,
                                  choices=SHIRT_SIZES,
                                  default='S')

    def __unicode__(self):
        return "{} {}".format(self.first_name, self.last_name)


