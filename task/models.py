from django.db import models


class Task(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deadline_at = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField()
    tags = models.ManyToManyField(
        to="Tag",
        related_name="tasks",
    )


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)
