from django.urls import path
from to_do.views import tasks, task_create_view, task, task_delete_view

urlpatterns = [
path("", tasks),
    path("tasks/", tasks),
    path("task/create/", task_create_view),
    path("task/", task),
    path("tasks/delete/<int:id>/", task_delete_view)
]