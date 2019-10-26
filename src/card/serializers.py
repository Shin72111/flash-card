from rest_framework import serializers
from django.shortcuts import get_object_or_404

from .models import Card, Lesson


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


class CardInLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['id', 'key', 'value']

    def create(self, validated_data):
        lesson_id = self.context.get('view').kwargs.get('lesson_id')
        lesson = get_object_or_404(Lesson, id=lesson_id)
        card = Card(
            key=validated_data['key'],
            value=validated_data['value'],
            lesson=lesson
        )
        card.save()
        return card
