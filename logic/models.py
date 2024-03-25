from logic.api import Object, Tank
from core import entities
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
    creationTime: float
    rect: pygame.Rect

    def __post_init__(self):
        self.image = pygame.Surface = pygame.image.load("./images/bullet5.png")
        self.mask = pygame.mask.from_surface(self.image.convert_alpha())
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def update(self, deltatime: float):
        
        dir = get_direction(self.angle) * self.velocity * deltatime
        
        self.posX += dir.x
        self.posY += dir.y

        
        if ((pygame.time.get_ticks() - self.creationTime) / 1000 > 5):
            return False
        
        return True


    def render(self, surface: pygame.Surface):
        img = pygame.transform.rotate(self.image, 270-self.angle)
        img_size = img.get_size()
        pos = (self.posX-img_size[0]/2, self.posY-img_size[1]/2)
        surface.blit(img, pos)


@dataclass
class TankT34(Tank, entities.Tank):
    image: pygame.Surface = pygame.image.load("./images/T34_preview.png")

    def __post_init__(self):
        self.mask = pygame.mask.from_surface(self.image.convert_alpha())
        self.width = self.image.get_width() #77
        self.height = self.image.get_height() #148

    def update(self, deltatime: float):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.angle -= 90 * deltatime
        if keys[pygame.K_RIGHT]:
            self.angle += 90 * deltatime

        currentVelocity = 0
        if keys[pygame.K_UP]:
            currentVelocity = self.velocity
        if keys[pygame.K_DOWN]:
            currentVelocity = -self.velocity
        
        if keys[pygame.K_SPACE]:
            self.shoot()
        
        dir = get_direction(self.angle) * currentVelocity * deltatime
        self.posX += dir.x
        self.posY += dir.y

        return True

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
        b = Bullet(self.posX, self.posY+0.5, self.angle, self.bulletVelocity, self.bulletDamage, curTime, (self.posX, self.posY, 6, 6))
        self.on_shoot(b)
