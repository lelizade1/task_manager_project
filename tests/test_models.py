import unittest
import sys
import os

# Path fix for testing
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.models.factory import WorkItemFactory
from src.models.task import Task

class TestTaskProject(unittest.TestCase):
    
    def test_factory_creates_task(self):
        """Test if Factory creates a Task correctly."""
        task = WorkItemFactory.create_item("task", title="Test Task", priority="High")
        
        self.assertIsInstance(task, Task)
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.priority, "High")
        self.assertEqual(task.status, "Todo")

    def test_encapsulation(self):
        """Test if ID is generated and accessible."""
        task = WorkItemFactory.create_item("task", title="Encapsulation Check")
        self.assertTrue(len(task.id) > 0)

if __name__ == '__main__':
    unittest.main()