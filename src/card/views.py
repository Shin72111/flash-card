from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Card
from .serializers import CardSerializer


class CardReadOnlyViewset(ReadOnlyModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
