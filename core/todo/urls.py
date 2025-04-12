from django.urls import path
from .views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView

app_name = "todo"

urlpatterns = [
    path("", TaskListView.as_view(), name="task_list"),
    path("new/", TaskCreateView.as_view(), name="task_create"),
    path("update/<pk>/", TaskUpdateView.as_view(), name="task_update"),
    path("delete/<pk>/", TaskDeleteView.as_view(), name="task_delete"),
]
