from django.urls import path
from . import views

urlpatterns = [
    path("addTask/", views.addTask, name="addTask"),
    path("markComplete/<int:pk>", views.markComplete, name="markComplete"),
    path("markUnComplete/<int:pk>", views.markUnComplete, name="markUnComplete"),
]
