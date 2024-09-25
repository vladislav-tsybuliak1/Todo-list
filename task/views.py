from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from task.models import Task


def index(request: HttpRequest) -> HttpResponse:
    tasks = Task.objects.all()
    context = {
        "tasks": tasks
    }
    return render(request, "task/index.html", context=context)
