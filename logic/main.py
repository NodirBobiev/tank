from logic.game import Game
from logic.tank.model import TankT34
from logic.bullet.model import Bullet
from logic.controller.tank import TankController
from logic.time.timer import Timer
import asyncio


async def run(shutdown: asyncio.Event, event_queue:asyncio.Queue, game_core: Game, game_timer: Timer):
    t1 = TankT34(
        posX=500, 
        posY=500, 
        velocity=100, 
        angle=90, 
        health=100,
        bulletDamage=20, 
        bulletVelocity=500, 
        shootCooldown=0
    )
    
    controller = TankController(t1)

    game_core.add_recent_object(t1)

    FPS = 30
    game_core.start()

    while not shutdown.is_set():
        game_core.init_recent_objects()
        game_core.start_recent_objects()
        while not event_queue.empty():
            event = await event_queue.get()
            print(f"--- :{event}")
            controller.execute_event(event)
        
        print(f"objects: {len(game_core.objects)}")
        print("******* before await: {:.6f}".format(game_timer.get_real_delta_time()))
        await asyncio.sleep(1 / FPS - game_timer.get_real_delta_time())
        # print("======= after await: {:.6f}".format(game_timer.get_real_delta_time()))

        game_core.update()
        # g.print()
