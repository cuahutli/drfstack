from django.urls import path, include
from rest_framework import routers
from .views import QuestionAPI

router = routers.DefaultRouter()
router.register("questions", QuestionAPI)
urlpatterns = [
    path('', include(router.urls)),
]
