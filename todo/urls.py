from django.urls import path
from . import views

urlpatterns = [
    path("", views.todoHome, name="todoHome"),
    path("addTask/", views.addTask, name="addTask"),
    path("markComplete/<int:pk>", views.markComplete, name="markComplete"),
    path("markUnComplete/<int:pk>", views.markUnComplete, name="markUnComplete"),
    path("edit/<int:pk>", views.edit, name="edit"),
    path("deleteTask/<int:pk>", views.deleteTask, name="deleteTask"),
]
