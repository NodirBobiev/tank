from logic.game import Game
from logic.tank.model import TankT34
from logic.bullet.model import Bullet
from logic.controller.tank import TankController
from logic.time.timer import Timer
from logic.utils import object_intersect
import asyncio


async def run(shutdown: asyncio.Event, event_queue:asyncio.Queue, game_core: Game, game_timer: Timer):
    # t1 = TankT34(
    #     posX=300, 
    #     posY=700, 
    #     velocity=100, 
    #     angle=0, 
    #     health=100,
    #     bulletDamage=20, 
    #     bulletVelocity=500, 
    #     shootCooldown=3
    # )

    # t2 = TankT34(
    #     posX=700, 
    #     posY=700, 
    #     velocity=100, 
    #     angle=90, 
    #     health=20,
    #     bulletDamage=20, 
    #     bulletVelocity=500, 
    #     shootCooldown=3
    # )
    
    # controller = TankController(t1)

    # game_core.add_recent_object(t1)
    # game_core.add_recent_object(t2)

    FPS = 30
    game_core.start()

    while not shutdown.is_set():
        game_core.init_recent_objects()
        game_core.start_recent_objects()
        while not event_queue.empty():
            tank_id, event = await event_queue.get()
            # print(f"--- :{event}")
            for o in game_core.objects:
                if isinstance(o, TankT34) and o.tank_id == tank_id:
                    o.controller.execute_event(event)
        
        # print(f"objects: {len(game_core.objects)}")
        # print("******* before await: {:.6f}".format(game_timer.get_real_delta_time()))
        
        # objs = game_core.objects
        # for i in range(len(objs)):
        #     for j in range(i + 1, len(objs)):
        #         if (object_intersect(objs[i], objs[j])):
        #             print(i, j)
        #             print(objs[i].posX, objs[i].posY)
        #             print(objs[j].posX, objs[j].posY)
        #             print("INTERSECT: ", type(objs[i]), " AND ", type(objs[j]))

        await asyncio.sleep(1 / FPS - game_timer.get_real_delta_time())
        # print("======= after await: {:.6f}".format(game_timer.get_real_delta_time()))

        game_core.update()
        # g.print()
