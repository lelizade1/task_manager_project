import unittest
import sys
import os
import shutil

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.services.task_service import TaskService
from src.strategies.sorting import SortByPriority

class TestSprint2(unittest.TestCase):
    
    def setUp(self):
        self.service = TaskService()
        self.service.repo.filepath = "data/test_tasks.json"
        with open("data/test_tasks.json", 'w') as f:
            f.write("[]")

    def tearDown(self):
        if os.path.exists("data/test_tasks.json"):
            os.remove("data/test_tasks.json")

    def test_full_crud(self):
        self.service.create_task("Test Task", "High", uid="100")
        tasks = self.service.get_tasks()
        self.assertEqual(len(tasks), 1)
        
        self.service.update_task_status("100", "Done")
        updated = self.service.repo.get_by_id("100")
        self.assertEqual(updated['status'], "Done")
        
        self.service.delete_task("100")
        tasks = self.service.get_tasks()
        self.assertEqual(len(tasks), 0)

    def test_strategy_sorting(self):
        self.service.create_task("Task A", "Low", uid="1")
        self.service.create_task("Task B", "High", uid="2")
        self.service.create_task("Task C", "Medium", uid="3")

        strategy = SortByPriority()
        sorted_tasks = self.service.get_tasks(sort_strategy=strategy)

        self.assertEqual(sorted_tasks[0]['title'], "Task B")
        self.assertEqual(sorted_tasks[1]['title'], "Task C")
        self.assertEqual(sorted_tasks[2]['title'], "Task A")

if __name__ == '__main__':
    unittest.main()