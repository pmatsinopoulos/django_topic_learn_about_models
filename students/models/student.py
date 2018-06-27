from django.db import models
from students.models import CommonInfo


class Student(CommonInfo):
    home_group = models.CharField(max_length=5)

    class Meta(CommonInfo.Meta):
        db_table = 'students_students'
