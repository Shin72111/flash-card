from rest_framework.viewsets import ModelViewSet

from .models import Topic
from .serializer import TopicSerializer


class TopicViewset(ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
