from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from .services import recalculate_overdue_tasks


class RecalculateOverdueView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        recalculate_overdue_tasks()
        return Response({"status": "ok"})
