from django.db import models

from lesson.models import Lesson


class Card(models.Model):
    lesson = models.ForeignKey(
        Lesson,
        related_name='cards',
        on_delete=models.CASCADE
    )
    key = models.CharField(max_length=128)
    value = models.CharField(max_length=256)
