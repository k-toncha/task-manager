from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
        read_only_fields = (
            "id",
            "owner",
            "created_at",
            "updated_at",
            "is_overdue",
        )

    def validate(self, attrs):
        status = attrs.get("status", self.instance.status if self.instance else None)
        due_date = attrs.get("due_date", self.instance.due_date if self.instance else None)

        if status == Task.Status.DONE and not due_date:
            raise serializers.ValidationError(
                {"due_date": "due_date обязателен при статусе 'done'"}
            )

        return attrs
