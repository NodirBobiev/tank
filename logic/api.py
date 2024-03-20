from abc import ABC, abstractmethod
import pygame


class Object(ABC):
    @abstractmethod
    def update(self, deltatime: float):
        pass

    @abstractmethod
    def render(self, surface: pygame.Surface):
        pass


class Tank(Object):
    @abstractmethod
    def shoot():
        pass