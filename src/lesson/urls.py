from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import LessonReadOnlyViewset
from card.views import CardInLessonViewset

router = DefaultRouter()
router.register('', LessonReadOnlyViewset)
router.register(
    prefix=r'(?P<lesson_id>.+)/cards',
    viewset=CardInLessonViewset,
    base_name='Card-in-lesson'
)

urlpatterns = [
    path('', include(router.urls)),
]
