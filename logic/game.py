from logic.time.timer import Timer
from logic.api import Object
from typing import List

class Game:
    def __init__(self, timer: Timer):
        self.objects: List[Object] = []
        self.recent_objects: List[Object] = []
        self.timer = timer

    def start(self):
        self.timer.start()
    
    def add_recent_object(self, o: Object):
        self.recent_objects.append(o)

    def init_recent_objects(self):
        for o in self.recent_objects:
            o.init(game=self)

    def start_recent_objects(self):
        for o in self.recent_objects:
            o.start()
        self.age_recent_objects()
    
    def age_recent_objects(self):
        for o in self.recent_objects:
            self.objects.append(o)
        self.recent_objects = []

    def update(self):
        self.timer.tick()
        for o in self.objects:
            if not o.is_destroyed():
                o.update()
        
        self.remove_destroyeds()
    
    def remove_destroyeds(self):
        alive_objects = []
        for o in self.objects:
            if not o.is_destroyed():
                alive_objects.append(o)
        self.objects = alive_objects

    def print(self):
        for o in self.objects:
            print(o)
