from rest_framework.routers import DefaultRouter
from .views import TaskViewSet
from .admin_views import RecalculateOverdueView
from django.urls import path

router = DefaultRouter()
router.register("tasks", TaskViewSet, basename="task")

urlpatterns = [
    path("tasks/recalculate_overdue/", RecalculateOverdueView.as_view()),
] + router.urls
