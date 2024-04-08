from logic.controller.tank import Event as TankEvent
from logic.tank.model import TankT34
from logic.bullet.model import Bullet
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

def parse_tank_to_proto(tank: TankT34)->game_pb2.Tank:
    proto_result = game_pb2.Tank()

    proto_result.pos_x = tank.posX
    proto_result.pos_y = tank.posY
    proto_result.velocity = tank.velocity
    proto_result.angle = tank.angle
    proto_result.health = tank.health
    proto_result.bullet_damage = tank.bulletDamage
    proto_result.bullet_velocity = tank.bulletVelocity
    proto_result.shoot_cooldown = tank.shootCooldown

    return proto_result

def parse_bullet_to_proto(bullet: Bullet)->game_pb2.Bullet:
    proto_result = game_pb2.Bullet()
    
    proto_result.pos_x = bullet.posX
    proto_result.pos_y = bullet.posY
    proto_result.velocity = bullet.velocity
    proto_result.angle = bullet.angle
    proto_result.damage = bullet.damage

    return proto_result