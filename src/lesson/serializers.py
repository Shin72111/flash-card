from rest_framework import serializers
from django.shortcuts import get_object_or_404

from .models import Lesson, Topic
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

    def create(self, validated_data):
        topic_id = self.context.get('view').kwargs.get('topic_id')
        topic = get_object_or_404(Topic, id=topic_id)
        lesson = Lesson(name=validated_data['name'], topic=topic)
        lesson.save()
        print(lesson.id)
        return lesson
