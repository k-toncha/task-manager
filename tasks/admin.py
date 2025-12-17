from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "status", "owner", "is_overdue", "due_date")
    list_filter = ("status", "is_overdue")
