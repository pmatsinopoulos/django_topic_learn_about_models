from django.db import models


class Publication(models.Model):
    class Meta:
        db_table = 'articles_publications'
        ordering = ('title',)

    title = models.CharField(max_length=300)

    def __unicode__(self):
        return self.title

