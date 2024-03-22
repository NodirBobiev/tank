from proto_gen import game_pb2, game_pb2_grpc
from concurrent import futures
import grpc
import time
import random
import google.protobuf.empty_pb2

def create_game_state_reply():
    # Create an instance of GameState
    game_state = game_pb2.GameState()
    
    # Add a tank to the game state, updated variable names to follow naming conventions
    tank = game_state.tanks.add()
    tank.pos_x = 100.0
    tank.pos_y = 200.0
    tank.velocity = 1.5
    tank.angle = 90.0
    tank.health = 100.0
    tank.bullet_damage = 25.0
    tank.bullet_velocity = 3.0
    tank.shoot_cooldown = 2.0
    tank.last_shoot_time = 0.0
    
    # Add a bullet to the game state, updated variable names to follow naming conventions
    bullet = game_state.bullets.add()
    bullet.pos_x = 150.0
    bullet.pos_y = 250.0
    bullet.angle = 45.0
    bullet.velocity = 3.0
    bullet.damage = 25.0
    
    # Create GetStateReply and assign the game_state
    get_state_reply = game_pb2.GetStateReply()
    get_state_reply.game_state.CopyFrom(game_state)
    
    return get_state_reply

def create_random_game_state():
    # Function to create a random GameState
    game_state = game_pb2.GameState()

    # Randomly add tanks and bullets
    for _ in range(random.randint(1, 5)):  # Example: 1 to 5 tanks
        tank = game_state.tanks.add()
        tank.pos_x = random.random() * 100
        tank.pos_y = random.random() * 100
        # Set other tank fields as needed...

    for _ in range(random.randint(1, 10)):  # Example: 1 to 10 bullets
        bullet = game_state.bullets.add()
        bullet.pos_x = random.random() * 100
        bullet.pos_y = random.random() * 100
        # Set other bullet fields as needed...

    return game_state

def extract_address(context):
    peer_info = context.peer()
    return peer_info

class GameServicer(game_pb2_grpc.GameServicer):
    def GetState(self, request, context):
        print(f"Here we go again! client address={extract_address(context)}")
        return create_game_state_reply()
    
    def GetStateStream(self, request, context):
        while True:
            print(f"Sof dunyora jugiyo giriftay client address={extract_address(context)}")
            # Send random game states to the client
            yield create_random_game_state()
            time.sleep(1)  # Adjus
    
    def PostTankEvent(self, request, context):
        tank_id = request.tank_id
        event = request.event

        # Example action handling based on the event
        if event == game_pb2.TankEvent.SHOOT:
            print(f"Tank {tank_id} performed SHOOT")
        elif event == game_pb2.TankEvent.MOVE_FORWARD:
            print(f"Tank {tank_id} performed MOVE_FORWARD")
        elif event == game_pb2.TankEvent.MOVE_BACKWARD:
            print(f"Tank {tank_id} performed MOVE_BACKWARD")
        elif event == game_pb2.TankEvent.ROTATE_LEFT:
            print(f"Tank {tank_id} performed ROTATE_LEFT")
        elif event == game_pb2.TankEvent.ROTATE_RIGHT:
            print(f"Tank {tank_id} performed ROTATE_RIGHT")

        return google.protobuf.empty_pb2.Empty()
    

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    game_pb2_grpc.add_GameServicer_to_server(GameServicer(), server)

    server.add_insecure_port('[::]:50051')  # Listen on port 50051
    server.start()
    print("Server started, listening on port 50051.")
    server.wait_for_termination()


if __name__ == '__main__':
    serve()