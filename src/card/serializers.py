from rest_framework import serializers

from .models import Card


class CardSerializer(serializers.ModelSerializer):
    topic = serializers.IntegerField(source='lesson.topic.id', read_only=True)
    topic_name = serializers.CharField(
        source='lesson.topic.name', read_only=True)
    lesson_name = serializers.CharField(source='lesson.name', read_only=True)

    class Meta:
        model = Card
        fields = [
            'id',
            'topic',
            'topic_name',
            'lesson',
            'lesson_name',
            'key',
            'value'
        ]
