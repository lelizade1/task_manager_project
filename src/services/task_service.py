from src.repositories.task_repo import TaskRepository
from src.models.factory import WorkItemFactory
from src.utils.logger import setup_logger

logger = setup_logger()

class TaskService:
    def __init__(self):
        self.repo = TaskRepository()
        self.VALID_PRIORITIES = ["High", "Medium", "Low"]

    def create_task(self, title, priority, uid=None):
        if not title:
            raise ValueError("Title cannot be empty.")
        
        clean_priority = priority.strip().capitalize()
        
        if clean_priority not in self.VALID_PRIORITIES:
            raise ValueError(f"Invalid Priority: '{priority}'. Must be High, Medium, or Low.")

        if uid and self.repo.get_by_id(uid):
            raise ValueError(f"ID '{uid}' already exists.")

        task = WorkItemFactory.create_item("task", title=title, priority=clean_priority, uid=uid)
        
        task_dict = {
            "id": task.id,
            "title": task.title,
            "status": task.status,
            "priority": task.priority,
            "type": "Task"
        }
        
        self.repo.save(task_dict)
        logger.info(f"Service: Created Task '{title}'")

    def create_subtask(self, title, parent_id, uid=None):
        if not title:
            raise ValueError("Title cannot be empty.")
        
        if not self.repo.get_by_id(parent_id):
            raise ValueError(f"Parent Task ID '{parent_id}' does not exist.")

        sub = WorkItemFactory.create_item("subtask", title=title, parent_id=parent_id, uid=uid)
        
        sub_dict = {
            "id": sub.id,
            "title": sub.title,
            "status": sub.status,
            "parent_id": sub.parent_id,
            "type": "SubTask"
        }
        
        self.repo.save(sub_dict)
        logger.info(f"Service: Created SubTask '{title}' linked to {parent_id}")

    def get_tasks(self, sort_strategy=None):
        tasks = self.repo.get_all()
        if sort_strategy:
            return sort_strategy.sort(tasks)
        return tasks

    def update_task_status(self, task_id, new_status):
        if not self.repo.get_by_id(task_id):
            raise ValueError("Task ID not found.")
        success = self.repo.update(task_id, {"status": new_status})
        if success:
            logger.info(f"Service: Updated status of {task_id} to {new_status}")
        return success

    def delete_task(self, task_id):
        success = self.repo.delete(task_id)
        if success:
            logger.info(f"Service: Deleted task {task_id}")
        else:
            raise ValueError("Task ID not found.")