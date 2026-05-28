from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect

from to_do.models import Task



def tasks(request):
    tasks = Task.objects.all()
    return render(request, "articles/index.html", {"tasks": tasks})

def task(request, id):
    task = get_object_or_404(Task, id=id)
    return render(request, "articles/task_view.html", {"task": task})


def task_create_view(request):
    if request.method == 'GET':
        return render(request, 'articles/task_create.html')
    elif request.method == 'POST':
        Task.objects.create(
            description=request.POST.get("description"),
            detail_description=request.POST.get("detail_description"),
            status=request.POST.get("status", "new"),
            due_date=request.POST.get("due_date") or None,
        )
        return redirect("/tasks")

def task_delete_view(request, id):
    Task.objects.filter(id=id).delete()
    return redirect("/tasks")
