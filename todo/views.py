from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Task
from django.core.paginator import Paginator

# Create your views here.


def todoHome(request):
    tasks = Task.objects.filter(is_completed=False).order_by("-updated_at")
    completed_tasks = Task.objects.filter(is_completed=True).order_by("-updated_at")
    unCompleted_tasks = Task.objects.filter(is_completed=False).order_by("-updated_at")

    paginator = Paginator(tasks, 5)
    page = request.GET.get("pg")
    tasks = paginator.get_page(page)
    # print("tasksnumberis" tas)

    context = {
        "tasks": tasks,
        "completed_tasks": completed_tasks,
        "unCompleted_tasks": unCompleted_tasks,
    }
    return render(request, "todoHome.html", context)


def addTask(request):
    task = request.POST["task"]
    print("task is " + task)
    Task.objects.create(task=task)
    return redirect("todoHome")


def markComplete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    # print("task is " + task)
    # Task.objects.update(is_completed=True)
    task.is_completed = True
    task.save()
    return redirect("todoHome")


def markUnComplete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    # print("task is " + task)
    # Task.objects.update(is_completed=True)
    task.is_completed = False
    task.save()
    return redirect("todoHome")


def edit(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == "POST":
        editedTask = request.POST["task"]
        task.task = editedTask
        task.save()
        return redirect("todoHome")
    else:
        context = {"task": task}
        # print("task is " + task)
        # Task.objects.update(is_completed=True)
        # task.is_completed = False
        # task.save()
        return render(request, "editTask.html", context)


def deleteTask(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    # print("task is " + task)
    # Task.objects.update(is_completed=True)
    return redirect("todoHome")
