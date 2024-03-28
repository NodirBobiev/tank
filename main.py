from logic.game import Game
from logic.tank.model import TankT34
from logic.bullet.model import Bullet
from logic.controller.tank import TankController, random_event
import asyncio
import pygame
import sys
from server.game import serve

async def run(event_queue:asyncio.Queue):
    g = Game()
    t1 = TankT34(posX=500, posY=500, angle=90, velocity=100, bulletDamage=20, bulletVelocity=500, shootCooldown=1000)
    t1.on_shoot = on_shoot(g)
    
    controller = TankController(t1)

    # t2 = TankT34(posX=500, posY=500, angle=120, velocity=100, bulletDamage=20, bulletVelocity=500, shootCooldown=1000)

    g.objects.append(t1)
    
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
        while not event_queue.empty():
            event = await event_queue.get()
            print(f"--- :{event}")
            controller.execute_event(event)
        
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

        await asyncio.sleep(0)

    # Quit Pygame
    pygame.quit()

def on_shoot(g : Game):

    def append_to_g(b:Bullet):
        g.objects = [b] + g.objects
    
    return append_to_g


async def main():
    event_queue = asyncio.Queue()
    
    game_server = asyncio.create_task(serve(event_queue))

    game_driver = asyncio.create_task(run(event_queue))

    await asyncio.gather(game_driver, game_server)


if __name__ == "__main__":
    asyncio.run(main())


