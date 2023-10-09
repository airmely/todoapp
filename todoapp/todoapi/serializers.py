from rest_framework import serializers
from django.contrib.auth.models import User

from todo.models import Tasks



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']


class TasksSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Tasks
        fields = ['task', 'description', 'date_created', 'status', 'user']
