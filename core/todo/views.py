from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Task


class TaskListView(ListView):
    model = Task
    template_name = "todo/task_list.html"
    context_object_name = "tasks"


class TaskCreateView(CreateView):
    model = Task
    template_name = "todo/task_form.html"
    fields = ["title"]
    success_url = reverse_lazy("todo:task_list")


class TaskUpdateView(UpdateView):
    model = Task
    template_name = "todo/task_update.html"
    fields = ["completed"]
    success_url = reverse_lazy("todo:task_list")
