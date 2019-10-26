from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import TopicViewset
from lesson.views import LessonInTopicViewset

router = DefaultRouter()
router.register('', TopicViewset)
router.register(
    prefix=r'(?P<topic_id>.+)/lessons',
    viewset=LessonInTopicViewset,
    base_name='Lesson-in-topic'
)


urlpatterns = [
    path('', include(router.urls))
]
