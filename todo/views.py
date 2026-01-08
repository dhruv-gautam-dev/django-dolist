from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Task

# Create your views here.


def addTask(request):
    task = request.POST["task"]
    print("task is " + task)
    Task.objects.create(task=task)
    return redirect("home")


def markComplete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    # print("task is " + task)
    # Task.objects.update(is_completed=True)
    task.is_completed = True
    task.save()
    return redirect("home")
