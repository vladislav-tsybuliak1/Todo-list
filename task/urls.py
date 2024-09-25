from django.urls import path

from task.views import (
    index,
    TaskCreateView,
    TaskUpdateView,
)


urlpatterns = [
    path("", index, name="index"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
]

app_name = "task"
