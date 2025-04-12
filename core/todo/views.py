from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Task


class TaskListView(LoginRequiredMixin, ListView):
    """
    View that displays a list of tasks for authenticated users.
    """

    model = Task
    template_name = "todo/task_list.html"
    context_object_name = "tasks"


class TaskCreateView(LoginRequiredMixin, CreateView):
    """
    View that provides a form to create a new task for authenticated users.
    """

    model = Task
    template_name = "todo/task_form.html"
    fields = ["title"]
    success_url = reverse_lazy("todo:task_list")


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    """
    View that provides a form to update an existing task for authenticated users.
    """

    model = Task
    template_name = "todo/task_update.html"
    fields = ["completed"]
    success_url = reverse_lazy("todo:task_list")


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    """
    View that handles the deletion of a task for authenticated users.
    """

    model = Task
    success_url = reverse_lazy("todo:task_list")
