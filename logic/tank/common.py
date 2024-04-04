from abc import ABC, abstractmethod
from logic.api import Object

class Tank(Object):
    @abstractmethod
    def move_forward():
        pass
    
    @abstractmethod
    def move_backward():
        pass
    
    @abstractmethod
    def rotate_left():
        pass
    
    @abstractmethod
    def rotate_right():
        pass
    
    @abstractmethod
    def shoot():
        pass
