from abc import ABC, abstractmethod
import uuid

class WorkItem(ABC):
    # ADDED uid=None here so we can pass a manual ID
    def __init__(self, title, uid=None, status="Todo"):
        if uid:
            self.__id = uid  # Use manual ID
        else:
            self.__id = str(uuid.uuid4())[:8]  # Auto-generate if empty
            
        self.title = title
        self.status = status

    @property
    def id(self):
        return self.__id

    @abstractmethod
    def get_details(self):
        pass