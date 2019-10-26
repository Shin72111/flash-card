from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import TopicViewset

router = DefaultRouter()
router.register('', TopicViewset)


urlpatterns = [
    path('', include(router.urls))
]
