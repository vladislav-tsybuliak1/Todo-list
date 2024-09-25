from django.db import models


class Task(models.Model):
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline_at = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField()
    tags = models.ManyToManyField(
        to="Tag",
        related_name="tasks",
    )

    def __str__(self) -> str:
        return self.content

class Tag(models.Model):
    name = models.CharField(max_length=23, unique=True)

    def __str__(self) -> str:
        return self.name
