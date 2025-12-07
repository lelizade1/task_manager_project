from abc import ABC, abstractmethod

class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data):
        pass

class SortByTitle(SortStrategy):
    def sort(self, data):
        return sorted(data, key=lambda x: x['title'].lower())

class SortByPriority(SortStrategy):
    def sort(self, data):
        prio_map = {"High": 1, "Medium": 2, "Low": 3}
        return sorted(data, key=lambda x: prio_map.get(x.get('priority', 'Low'), 4))