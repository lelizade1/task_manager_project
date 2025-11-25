from src.models.work_item import WorkItem

class Task(WorkItem):
    def __init__(self, title, priority="Medium", uid=None, status="Todo"):
        # Pass uid to parent class
        super().__init__(title, uid=uid, status=status)
        self.priority = priority

    def get_details(self):
        return f"[TASK] {self.title} | Priority: {self.priority} | ID: {self.id}"

class SubTask(WorkItem):
    def __init__(self, title, parent_id, uid=None, status="Todo"):
        # Pass uid to parent class
        super().__init__(title, uid=uid, status=status)
        self.parent_id = parent_id

    def get_details(self):
        return f"  -> [SUBTASK] {self.title} | Parent ID: {self.parent_id} | ID: {self.id}"