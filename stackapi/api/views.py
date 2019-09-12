from rest_framework import viewsets

from .serializer import QuestionSerializer
from stackapi.models import Question

class QuestionAPI(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
