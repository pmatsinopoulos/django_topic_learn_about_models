from django.db import models
from .question import Question


class Answer(models.Model):
    class Meta:
        db_table = 'quizzes_answers'
        order_with_respect_to = 'question'

    answer_text = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)