from django.db import models

from topic.models import Topic


class Lesson(models.Model):
    topic = models.ForeignKey(
        Topic,
        related_name='lessons',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=50)
