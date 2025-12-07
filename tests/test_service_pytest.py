import pytest
import sys
import os
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.services.task_service import TaskService
from src.repositories.task_repo import TaskRepository
from src.strategies.sorting import SortByPriority, SortByTitle

@pytest.fixture
def task_service():
    """
    Creates a TaskService connected to a TEMPORARY test file.
    Runs before every test function.
    """
    test_file = "data/pytest_temp.json"
    
    with open(test_file, 'w') as f:
        json.dump([], f)

    service = TaskService()
    service.repo = TaskRepository(filepath=test_file)

    yield service  

    if os.path.exists(test_file):
        os.remove(test_file)


def test_create_task(task_service):
    task_service.create_task("Learn Pytest", "High", uid="101")
    
    task = task_service.repo.get_by_id("101")
    assert task is not None
    assert task['title'] == "Learn Pytest"
    assert task['priority'] == "High"

def test_create_invalid_priority(task_service):
    with pytest.raises(ValueError) as excinfo:
        task_service.create_task("Bad Task", "SuperHigh")
    
    assert "Invalid Priority" in str(excinfo.value)

def test_create_subtask(task_service):
    task_service.create_task("Parent Task", "Medium", uid="P1")
    
    task_service.create_subtask("Child Task", parent_id="P1", uid="C1")
    
    child = task_service.repo.get_by_id("C1")
    assert child['parent_id'] == "P1"
    assert child['type'] == "SubTask"

def test_update_status(task_service):
    task_service.create_task("To Update", "Low", uid="500")
    
    success = task_service.update_task_status("500", "Done")
    assert success is True
    
    updated_task = task_service.repo.get_by_id("500")
    assert updated_task['status'] == "Done"

def test_delete_task(task_service):
    task_service.create_task("To Delete", "Low", uid="999")
    
    task_service.delete_task("999")
    
    deleted_task = task_service.repo.get_by_id("999")
    assert deleted_task is None

def test_strategy_sorting(task_service):
    task_service.create_task("Task A", "Low", uid="1")
    task_service.create_task("Task B", "High", uid="2")
    task_service.create_task("Task C", "Medium", uid="3")

    sorted_list = task_service.get_tasks(sort_strategy=SortByPriority())
    
    assert sorted_list[0]['title'] == "Task B"
    assert sorted_list[1]['title'] == "Task C"
    assert sorted_list[2]['title'] == "Task A"