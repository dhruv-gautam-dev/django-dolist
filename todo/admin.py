from django.contrib import admin
from .models import Task

# Register your models here.
admin.site.register(Task)


# first we have creted a model inmodels.py
# second we have register the model in admin.py
# third we have to make migrations and migrate to create the table in database
