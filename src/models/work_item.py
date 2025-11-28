from abc import ABC, abstractmethod
import uuid

class WorkItem(ABC):

    def __init__(self, title, uid=None, status="Todo"):
        if uid:
            self.__id = uid  
        else:
            self.__id = str(uuid.uuid4())[:8] 
            
        self.title = title
        self.status = status

    @property
    def id(self):
        return self.__id

    @abstractmethod
    def get_details(self):
        pass