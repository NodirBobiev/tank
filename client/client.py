from proto_gen import game_pb2, game_pb2_grpc
import grpc
import google.protobuf.empty_pb2
import uuid
import random

def get_game_state():
    # Assuming the server is running on localhost and listening on port 50051
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = game_pb2_grpc.GameStub(channel)
        response = stub.GetState(google.protobuf.empty_pb2.Empty())
        print("Game State Received:")
        # Example output of tanks and bullets, updated to follow Python naming conventions
        for tank in response.game_state.tanks:
            print(f"Tank at ({tank.pos_x}, {tank.pos_y}) with health {tank.health}")
        for bullet in response.game_state.bullets:
            print(f"Bullet at ({bullet.pos_x}, {bullet.pos_y}) with damage {bullet.damage}")
        return response

def get_game_state_stream():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = game_pb2_grpc.GameStub(channel)
        try:
            for game_state in stub.GetStateStream(google.protobuf.empty_pb2.Empty()):
                print("Streaming Game State Received:")
                for tank in game_state.tanks:
                    print(f"Tank at ({tank.pos_x}, {tank.pos_y}) with health {tank.health}")
                for bullet in game_state.bullets:
                    print(f"Bullet at ({bullet.pos_x}, {bullet.pos_y}) with damage {bullet.damage}")
        except grpc.RpcError as e:
            print(f"RPC error occurred: {e.code()} {e.details()}")


# Generate a list of UUIDs for tanks
tank_ids = [str(uuid.uuid1()) for _ in range(5)]  # Example: 5 tanks

# List of TankEvent enum values
tank_events = [
    game_pb2.TankEvent.SHOOT,
    game_pb2.TankEvent.MOVE_FORWARD,
    game_pb2.TankEvent.MOVE_BACKWARD,
    game_pb2.TankEvent.ROTATE_LEFT,
    game_pb2.TankEvent.ROTATE_RIGHT,
]

def post_tank_event():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = game_pb2_grpc.GameStub(channel)
        
        tank_id = random.choice(tank_ids)
        event = random.choice(tank_events)
        request = game_pb2.PostTankEventRequest(tank_id=tank_id, event=event)
        

        print(f"Posting event for tank {tank_id}: Event {event}")
        stub.PostTankEvent(request)

if __name__ == '__main__':
    get_game_state_stream()
    