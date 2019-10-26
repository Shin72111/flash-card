from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from django.shortcuts import get_list_or_404, get_object_or_404

from .models import Card
from .serializers import CardSerializer, CardInLessonSerializer


class CardReadOnlyViewset(ReadOnlyModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class CardInLessonViewset(ModelViewSet):
    serializer_class = CardInLessonSerializer

    def get_queryset(self):
        lesson_id = self.kwargs['lesson_id']
        return get_list_or_404(Card, lesson_id=lesson_id)

    def get_object(self):
        lesson_id = self.kwargs['lesson_id']
        id = self.kwargs['pk']
        return get_object_or_404(Card, lesson_id=lesson_id, id=id)
