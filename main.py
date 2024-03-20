from logic.game import Game
from logic.models import TankT34, Bullet
import pygame

def run(g: Game):
    # Initialize Pygame
    pygame.init()

    # Screen dimensions
    screen_width, screen_height = 1000, 800
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Top-Down Tank Game')

    # Colors
    background_color = (255, 255, 255) 

    running = True
    FPS = 30
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        deltatime = pygame.time.Clock().tick(FPS)/1000    
        print(f"{deltatime=}")
        g.update(deltatime)

        # Fill the screen with the background color
        screen.fill(background_color)

        # Draw the tank
        g.render(screen)

        # Update the display
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()

def on_shoot(g : Game):

    def append_to_g(b:Bullet):
        g.objects = [b] + g.objects
    
    return append_to_g

if __name__=="__main__":
    g = Game()

    t1 = TankT34(posX=100, posY=100, angle=90, velocity=100, bulletDamage=20, bulletVelocity=500, shootCooldown=1000)
    t1.on_shoot = on_shoot(g)
    t2 = TankT34(posX=500, posY=500, angle=120, velocity=100, bulletDamage=20, bulletVelocity=500, shootCooldown=1000)

    g.objects.append(t1)
    g.objects.append(t2)

    run(g)