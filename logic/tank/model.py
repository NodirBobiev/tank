from logic.tank.common import Tank
from logic.bullet.model import Bullet
from core import entities
from dataclasses import dataclass
import pygame 
from logic.utils import get_direction

@dataclass
class TankT34(Tank, entities.Tank):
    image: pygame.Surface = pygame.image.load("/home/cyrus/tank/images/T34_preview.png")

    def __init__(self, *args, **kwargs):
        entities.Tank.__init__(self, *args, **kwargs)
        self.deltaVelocity = 0
        self.deltaAngle = 0

    def move_forward(self):
        self.deltaVelocity = self.velocity

    def move_backward(self):
        self.deltaVelocity = -self.velocity

    def rotate_left(self):
        self.deltaAngle = -90

    def rotate_right(self):
        self.deltaAngle = 90

    def update(self, deltatime: float):
        self.reflect_deltas(deltatime)
        self.reset_deltas()

    def reflect_deltas(self, deltatime: float):
        self.angle += self.deltaAngle * deltatime
        dir = get_direction(self.angle) * self.deltaVelocity * deltatime
        self.posX += dir.x
        self.posY += dir.y

    def reset_deltas(self):
        self.deltaAngle = 0
        self.deltaVelocity = 0

    def render(self, surface: pygame.Surface):
        img = pygame.transform.rotate(self.image, 90-self.angle)
        img_size = img.get_size()
        pos = (self.posX-img_size[0]/2, self.posY-img_size[1]/2)
        surface.blit(img, pos)

    def on_shoot(self, b: Bullet):
        pass

    def shoot(self):
        curTime = pygame.time.get_ticks()
        if curTime- self.lastShootTime < self.shootCooldown:
            return
        self.lastShootTime = curTime
        b = Bullet(self.posX, self.posY, self.angle, self.bulletVelocity, self.bulletDamage)
        self.on_shoot(b)
