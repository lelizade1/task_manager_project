from src.models.task import Task, SubTask

class WorkItemFactory:
    @staticmethod
    def create_item(item_type, title, **kwargs):
        if item_type.lower() == "task":
            return Task(title, **kwargs)
        elif item_type.lower() == "subtask":
            return SubTask(title, **kwargs)
        else:
            raise ValueError(f"Unknown item type: {item_type}")