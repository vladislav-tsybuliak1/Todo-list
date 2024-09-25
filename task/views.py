from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from task.models import Task


def index(request: HttpRequest) -> HttpResponse:
    tasks = Task.objects.prefetch_related("tags")
    context = {
        "tasks": tasks
    }
    return render(request, "task/index.html", context=context)


class TaskCreateView(generic.CreateView):
    model = Task
    fields = ("content", "deadline_at", "tags")
    success_url = reverse_lazy("task:index")
