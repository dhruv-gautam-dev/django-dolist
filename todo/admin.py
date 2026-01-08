from django.contrib import admin
from .models import Task


# below is to show the extra column in task table in admin panel
class TaskAdmin(admin.ModelAdmin):
    list_display = ("task", "is_completed", "created_at", "updated_at")
    search_fields = ("task",)


# Register your models here.
admin.site.register(Task, TaskAdmin)


# first we have creted a model inmodels.py
# second we have register the model in admin.py
# third we have to make migrations and migrate to create the table in database
