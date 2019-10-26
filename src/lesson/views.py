from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from django.shortcuts import get_object_or_404, get_list_or_404

from .models import Lesson
from .serializers import LessonSerializer, LessonInTopicSerializer


class LessonReadOnlyViewset(ReadOnlyModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonInTopicViewset(ModelViewSet):
    serializer_class = LessonInTopicSerializer

    def get_queryset(self):
        topic_id = self.kwargs['topic_id']
        return get_list_or_404(Lesson, topic_id=topic_id)

    def get_object(self):
        topic_id = self.kwargs['topic_id']
        id = self.kwargs['pk']
        return get_object_or_404(Lesson, topic_id=topic_id, id=id)
