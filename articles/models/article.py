from django.db import models

from articles.models.reporter import Reporter


class Article(models.Model):
    class Meta:
        db_table = 'articles_articles'
        ordering = ('headline',)

    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.headline
