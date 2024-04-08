from proto_gen import game_pb2
from client.objects.tank import TankT34
from client.objects.bullet import Bullet

def parse_proto_to_tank(proto_tank: game_pb2.Tank)->TankT34:
    result = TankT34()

    result.pos_x = proto_tank.pos_x
    result.pos_y = proto_tank.pos_y
    result.angle = proto_tank.angle

    return result


def parse_proto_to_bullet(proto_bullet: game_pb2.Bullet)->Bullet:
    result = Bullet()

    result.pos_x = proto_bullet.pos_x
    result.pos_y = proto_bullet.pos_y
    result.angle = proto_bullet.angle

    return result