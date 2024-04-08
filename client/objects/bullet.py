import pygame

class Bullet:
    posX : float
    posY : float
    angle: float
    velocity: float
    damage: float
    creationTime: float
    rect: pygame.Rect

    def __init__(self):
        self.pos_x = 0
        self.pos_y = 0
        self.angle = 0
        self.image = pygame.image.load("./images/bullet5.png")
    
    def render(self, surface: pygame.Surface):
        img = pygame.transform.rotate(self.image, 270-self.angle)
        img_size = img.get_size()
        pos = (self.pos_x-img_size[0]/2, self.pos_y-img_size[1]/2)
        surface.blit(img, pos)