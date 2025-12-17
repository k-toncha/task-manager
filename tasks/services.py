from django.utils.timezone import now
from .models import Task


def recalculate_overdue_tasks():
    Task.objects.filter(
        due_date__lt=now()
    ).exclude(
        status=Task.Status.DONE
    ).update(is_overdue=True)
