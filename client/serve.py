from proto_gen import game_pb2, game_pb2_grpc
from client.parse import parse_proto_to_bullet, parse_proto_to_tank
import grpc
import google.protobuf.empty_pb2
import uuid
import random
import pygame
import sys



def get_game_state(stub):
    # Assuming the server is running on localhost and listening on port 50051
  
    response = stub.GetState(google.protobuf.empty_pb2.Empty())
    # print("Game State Received:")
    # # Example output of tanks and bullets, updated to follow Python naming conventions
    # for tank in response.game_state.tanks:
    #     print(f"Tank at ({tank.pos_x}, {tank.pos_y}) with health {tank.health}")
    # for bullet in response.game_state.bullets:
    #     print(f"Bullet at ({bullet.pos_x}, {bullet.pos_y}) with damage {bullet.damage}")
    return response

def post_tank_event(stub, event):
    
    tank_id = "NULL"
    request = game_pb2.PostTankEventRequest(tank_id=tank_id, event=event)
    
    # print(f"Posting event for tank {tank_id}: Event {event}")
    stub.PostTankEvent(request)


def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = game_pb2_grpc.GameStub(channel) 

    # Initialize Pygame
    pygame.init()

    # Set up the screen
    WIDTH, HEIGHT = 1200, 900
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Simple Pygame App")

    # Set up colors
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)

    # Main loop
    running = True
    clock = pygame.time.Clock()

    events = {
        pygame.K_SPACE: game_pb2.TankEvent.SHOOT,
        pygame.K_UP: game_pb2.TankEvent.MOVE_FORWARD,
        pygame.K_DOWN: game_pb2.TankEvent.MOVE_BACKWARD,
        pygame.K_LEFT: game_pb2.TankEvent.ROTATE_LEFT,
        pygame.K_RIGHT: game_pb2.TankEvent.ROTATE_RIGHT,
    }

    while running:
        screen.fill(WHITE)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        for key in events.keys():
            if keys[key]:
                post_tank_event(stub, events[key])
        
        obj = []
        test = get_game_state(stub)

        for bullet in test.game_state.bullets:
            obj.append(parse_proto_to_bullet(bullet))
        for tank in test.game_state.tanks:
            obj.append(parse_proto_to_tank(tank))
        
        for o in obj:
            o.render(screen)
        # print(test)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(144)

    # Quit Pygame
    pygame.quit()
    channel.close()
    sys.exit()
