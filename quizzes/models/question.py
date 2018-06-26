from django.db import models


class Question(models.Model):
    class Meta:
        db_table = 'quizzes_questions'

    name = models.TextField()