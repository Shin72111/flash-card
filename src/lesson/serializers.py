from rest_framework import serializers

from .models import Lesson
from card.serializers import CardInLessonSerializer


class LessonSerializer(serializers.ModelSerializer):
    topic_name = serializers.CharField(source='topic.name', read_only=True)
    cards = CardInLessonSerializer(many=True, read_only=True)

    class Meta:
        model = Lesson
        fields = ['id', 'topic', 'topic_name', 'name', 'cards']


class LessonInTopicSerializer(serializers.ModelSerializer):
    cards = CardInLessonSerializer(many=True, read_only=True)

    class Meta:
        model = Lesson
        fields = ['id', 'name', 'cards']
