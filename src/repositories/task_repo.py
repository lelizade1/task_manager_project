import json
import os

class TaskRepository:
    def __init__(self, filepath="data/tasks.json"):
        self.filepath = filepath

    def save(self, work_item):
        data = self.get_all_raw()
        
        item_dict = {
            "id": work_item.id,
            "title": work_item.title,
            "status": work_item.status,
            "type": work_item.__class__.__name__
        }

        if hasattr(work_item, 'priority'):
            item_dict["priority"] = work_item.priority
        if hasattr(work_item, 'parent_id'):
            item_dict["parent_id"] = work_item.parent_id

        data.append(item_dict)

        with open(self.filepath, 'w') as f:
            json.dump(data, f, indent=4)

    def get_all_raw(self):
        if not os.path.exists(self.filepath):
            return []
        try:
            with open(self.filepath, 'r') as f:
                content = f.read()
                return json.loads(content) if content else []
        except json.JSONDecodeError:
            return []


    def task_exists(self, target_id):

        all_tasks = self.get_all_raw()
        for t in all_tasks:
            if t['id'] == target_id:
                return True
        return False