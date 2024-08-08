from django.test import TestCase
from .models import TodoItem

# Create your tests here.

class TodoItemModelTest(TestCase):
    def test_todo_item_creation(self):
        todo = TodoItem.objects.create(task='Test Task')
        self.assertEqual(todo.task, 'Test Task')
        self.assertFalse(todo.completed)