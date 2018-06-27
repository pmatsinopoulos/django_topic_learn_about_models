from django.db import models


class Blog(models.Model):
    class Meta:
        db_table = 'articles_blogs'

    name = models.CharField(max_length=1024)
    tagline = models.TextField()

    def save(self, *args, **kwargs):
        self._do_something()
        super(Blog, self).save(*args, **kwargs)
        self._do_something_else()

    def _do_something(self):
        print('I am doing something')

    def _do_something_else(self):
        print('I am doing something after real save')
