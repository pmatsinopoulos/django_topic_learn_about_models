from django.db import models


class Reporter(models.Model):
    class Meta:
        db_table = 'articles_reporters'

    first_name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=False)
    email = models.EmailField(max_length=255)

    def __unicode__(self):
        return u"%s %s" % (self.first_name, self.last_name)

