import json
import os
from src.utils.logger import setup_logger

logger = setup_logger()

class TaskRepository:
    def __init__(self, filepath="data/tasks.json"):
        self.filepath = filepath

    def _read_file(self):
        if not os.path.exists(self.filepath):
            return []
        try:
            with open(self.filepath, 'r') as f:
                content = f.read()
                return json.loads(content) if content else []
        except json.JSONDecodeError:
            logger.error("Failed to decode JSON. Returning empty list.")
            return []

    def _write_file(self, data):
        try:
            with open(self.filepath, 'w') as f:
                json.dump(data, f, indent=4)
        except IOError as e:
            logger.error(f"File I/O Error: {e}")
            raise e

    def save(self, item_dict):
        data = self._read_file()
        data.append(item_dict)
        self._write_file(data)

    def get_all(self):
        return self._read_file()

    def get_by_id(self, item_id):
        data = self._read_file()
        for item in data:
            if item['id'] == item_id:
                return item
        return None

    def update(self, item_id, updates):
        data = self._read_file()
        found = False
        for item in data:
            if item['id'] == item_id:
                item.update(updates) 
                found = True
                break
        
        if found:
            self._write_file(data)
        return found

    def delete(self, item_id):
        data = self._read_file()
        initial_count = len(data)
        new_data = [i for i in data if i['id'] != item_id]
        
        if len(new_data) < initial_count:
            self._write_file(new_data)
            return True
        return False