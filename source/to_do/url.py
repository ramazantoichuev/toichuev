from django.urls import path
from to_do.views import tasks, task_create_view, task, task_delete_view

urlpatterns = [
path("", tasks, name="tasks"),
    path("tasks/", tasks, name="tasks"),
    path("task/create/", task_create_view, name="create"),
    path("task/<int:id>/", task, name="detail"),
    path("task/delete/<int:id>/", task_delete_view, name="delete"),
]