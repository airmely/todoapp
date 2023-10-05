from rest_framework import serializers

from todo.models import Tasks


class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ['task', 'description', 'date_created', 'status']
