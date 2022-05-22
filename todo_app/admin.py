from re import T
from django.contrib import admin
from .models import Task, Imprint
# Register your models here.

admin.site.register(Task)
admin.site.register(Imprint)
