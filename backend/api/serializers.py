"""Serializers."""
from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Class."""

    class Meta:
        """Interior class."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
