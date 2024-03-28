from logic.controller.tank import Event as TankEvent
from proto_gen import game_pb2

def parse_tank_event(event)->TankEvent:
    if event == game_pb2.TankEvent.SHOOT:
        return TankEvent.SHOOT
    elif event == game_pb2.TankEvent.MOVE_FORWARD:
        return TankEvent.MOVE_FORWARD
    elif event == game_pb2.TankEvent.MOVE_BACKWARD:
        return TankEvent.MOVE_BACKWARD
    elif event == game_pb2.TankEvent.ROTATE_LEFT:
        return TankEvent.ROTATE_LEFT
    elif event == game_pb2.TankEvent.ROTATE_RIGHT:
        return TankEvent.ROTATE_RIGHT