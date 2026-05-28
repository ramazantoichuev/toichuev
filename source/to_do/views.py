from django.http import HttpResponseRedirect
from django.shortcuts import render

from to_do.models import Task



def tasks(request):
    tasks = Task.objects.all()
    return render(request, "index.html", {"tasks": tasks})

def task(request):
    id = request.GET.get('id')
    if id:
        try:
            task = Task.objects.get(id=int(id))
            return render(request, "task_view.html", {"task": task})
        except Task.DoesNotExist:
            return HttpResponseRedirect("/tasks")
    return HttpResponseRedirect("/tasks")

def task_create_view(request):
    if request.method == 'GET':
        return render(request, 'task_create.html')
    elif request.method == 'POST':
        Task.objects.create(
            description=request.POST.get("description"),
            detail_description=request.POST.get("detail_description"),
            status=request.POST.get("status", "new"),
            due_date=request.POST.get("due_date") or None,
        )
        return HttpResponseRedirect("/tasks")

def task_delete_view(request, id):
    Task.objects.filter(id=id).delete()
    return HttpResponseRedirect("/tasks")
