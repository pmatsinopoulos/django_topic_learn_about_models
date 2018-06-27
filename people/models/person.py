import datetime

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
    birth_date = models.DateField(null=False, blank=False)

    def __unicode__(self):
        return "{} {}".format(self.first_name, self.last_name)

    def baby_boomer_status(self):
        """
        Returns the person's baby-boomer status.
        :return:
        """
        if self.birth_date < datetime.date(1945, 8, 1):
            return "Pre-boomer"
        elif self.birth_date < datetime.date(1965, 1, 1):
            return "Baby boomer"
        else:
            return "Post-boomer"

    @property
    def full_name(self):
        """
        Returns the person's full name."
        :return:
        """
        return '%s %s' % (self.first_name, self.last_name)




