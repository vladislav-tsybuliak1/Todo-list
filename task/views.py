from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic

from task.forms import TaskForm
from task.models import Task, Tag


def index(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        task_id = request.POST.get("task_id")
        task = get_object_or_404(Task, id=task_id)
        if task.is_completed:
            task.is_completed = False
        else:
            task.is_completed = True
        task.save()
        return redirect("task:index")
    tasks = Task.objects.prefetch_related("tags")
    context = {
        "tasks": tasks
    }
    return render(request, "task/index.html", context=context)


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("task:index")


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
