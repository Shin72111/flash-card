from rest_framework.viewsets import ModelViewSet

from .models import Topic
from .serializers import TopicSerializer


class TopicViewset(ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
