"""Module containing tests for the API app."""

from http import HTTPStatus
from api import models
from django.test import Client, TestCase


class TaskiAPITestCase(TestCase):
    """Test case for the Task API."""

    def setUp(self):
        """Set up the test environment."""
        self.guest_client = Client()

    def test_list_exists(self):
        """Test the availability of the task list."""
        response = self.guest_client.get('/api/tasks/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_task_creation(self):
        """Test task creation."""
        data = {'title': 'Test', 'description': 'Test'}
        response = self.guest_client.post('/api/tasks/', data=data)
        self.assertEqual(response.status_code, HTTPStatus.CREATED)
        self.assertTrue(models.Task.objects.filter(title='Test').exists())
