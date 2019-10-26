from rest_framework import serializers

from .models import Lesson


class LessonSerializer(serializers.ModelSerializer):
    topic_name = serializers.CharField(source='topic.name', read_only=True)

    class Meta:
        model = Lesson
        fields = ['id', 'topic', 'topic_name', 'name']
