from abc import ABC, abstractmethod
import pygame

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class Object(ABC):
    @abstractmethod
    def update(self, deltatime: float):
        pass

    @abstractmethod
    def render(self, surface: pygame.Surface):
        pass



