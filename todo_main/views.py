from django.http import HttpResponse
from django.shortcuts import render
from todo.models import Task
from django.core.paginator import Paginator


def home(request):
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
    return render(request, "home.html", context)
