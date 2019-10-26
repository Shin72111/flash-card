from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Lesson
from .serializers import LessonSerializer


class LessonReadOnlyViewset(ReadOnlyModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
