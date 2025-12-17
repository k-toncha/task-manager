from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from tasks.models import Task


class TaskAPITestCase(APITestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(username="user1")
        self.user2 = User.objects.create_user(username="user2")

        self.tasks_url = "/api/tasks/"

    def test_create_task_success(self):
        data = {
            "title": "Test task",
            "status": "todo",
        }

        response = self.client.post(
            self.tasks_url,
            data,
            format="json",
            HTTP_X_USER_ID=str(self.user1.id),
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)

        task = Task.objects.first()
        self.assertEqual(task.title, "Test task")
        self.assertEqual(task.owner, self.user1)


    def test_cannot_set_done_without_due_date(self):
        data = {
            "title": "Invalid task",
            "status": "done",
        }

        response = self.client.post(
            self.tasks_url,
            data,
            format="json",
            HTTP_X_USER_ID=str(self.user1.id),
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("due_date", response.data)

    def test_cannot_delete_someone_elses_task(self):
        task = Task.objects.create(
            title="User1 task",
            owner=self.user1,
            status="todo",
        )

        url = f"/api/tasks/{task.id}/"

        response = self.client.delete(
            url,
            HTTP_X_USER_ID=str(self.user2.id),
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(Task.objects.count(), 1)
