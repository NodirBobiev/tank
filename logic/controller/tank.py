from enum import Enum
from logic.api import Command
from logic.tank.common import Tank
from typing import Mapping
import random

class Event(Enum):
    SHOOT = 1
    MOVE_FORWARD = 2
    MOVE_BACKWARD = 3
    ROTATE_LEFT = 4
    ROTATE_RIGHT = 5

class MoveForwardCommand(Command):
    def __init__(self, tank: Tank):
        self.tank = tank
    
    def execute(self):
        self.tank.move_forward()

class MoveBackwardCommand(Command):
    def __init__(self, tank: Tank):
        self.tank = tank
    
    def execute(self):
        self.tank.move_backward()

class RotateLeftCommand(Command):
    def __init__(self, tank: Tank):
        self.tank = tank
    
    def execute(self):
        self.tank.rotate_left()

class RotateRightCommand(Command):
    def __init__(self, tank: Tank):
        self.tank = tank
    
    def execute(self):
        self.tank.rotate_right()

class ShootCommand(Command):
    def __init__(self, tank: Tank):
        self.tank = tank
    
    def execute(self):
        self.tank.shoot()


class TankController:
    def __init__(self, tank):
        self.events: Mapping[Event, Command] = {
            Event.MOVE_FORWARD: MoveForwardCommand(tank), 
            Event.MOVE_BACKWARD: MoveBackwardCommand(tank),
            Event.ROTATE_RIGHT: RotateRightCommand(tank),
            Event.ROTATE_LEFT: RotateLeftCommand(tank),
            Event.SHOOT: ShootCommand(tank),
        }
    
    def execute_event(self, event: Event):
        if event not in self.events:
            return
        cmd = self.events[event]
        cmd.execute()

def random_event()->Event:
    events = [Event.SHOOT, Event.MOVE_FORWARD, Event.MOVE_BACKWARD, Event.ROTATE_LEFT, Event.ROTATE_RIGHT]
    return random.choice(events)

