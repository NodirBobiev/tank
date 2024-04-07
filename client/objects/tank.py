import pygame

class TankT34:
    def __init__(self):
        self.pos_x = 0
        self.pos_y = 0
        self.angle = 0
        self.image = pygame.image.load("./images/T34_preview.png")
    
    def render(self, surface: pygame.Surface):
        img = pygame.transform.rotate(self.image, 90-self.angle)
        img_size = img.get_size()
        pos = (self.pos_x-img_size[0]/2, self.pos_y-img_size[1]/2)
        surface.blit(img, pos)
    
