from logic.api import Object
from dataclasses import dataclass
import pygame 
from logic.utils import get_direction

@dataclass
class Bullet(Object):
    posX : float
    posY : float
    angle: float
    velocity: float
    damage: float

    def update(self, deltatime: float):
        dir = get_direction(self.angle) * self.velocity * deltatime
        self.posX += dir.x
        self.posY += dir.y        

    def render(self, surface: pygame.Surface):
        pygame.draw.circle(surface, (100, 100, 0), (self.posX, self.posY), 3)