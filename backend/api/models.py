"""Module containing the Task model."""
from django.db import models


class Task(models.Model):
    """Model representing a task."""

    title = models.CharField(verbose_name='Title', max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        """Return a string representation of the task."""
        return self.title
