from rest_framework import viewsets

from todoapi.permissions import IsAdminOrReadOnly
from todo.models import Tasks
from .serializers import TasksSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer
    permission_classes = (IsAdminOrReadOnly, )