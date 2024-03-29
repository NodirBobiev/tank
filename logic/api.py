from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class Object:
    def __init__(self):
        self.alive = True

    def init(self, *args, **kwargs):
        pass
    
    def start(self):
        pass

    def update(self):
        pass

    def destroy(self):
        self.alive = False

    def is_destroyed(self)->bool:
        return not self.alive
