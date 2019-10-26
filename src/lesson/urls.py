from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import LessonReadOnlyViewset

router = DefaultRouter()
router.register('', LessonReadOnlyViewset)

urlpatterns = [
    path('', include(router.urls)),
]
