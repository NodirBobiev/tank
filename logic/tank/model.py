from logic.tank.common import Tank
from logic.bullet.model import Bullet
from logic.controller.tank import TankController
from dataclasses import dataclass
from logic.utils import get_direction, object_intersect, rotate_coordinate_clockwise
from logic.time.timer import Timer
from logic.game import Game
from logic.api import Object

@dataclass
class TankT34(Tank, Object):
    posX: float
    posY: float
    velocity: float
    angle: float
    health: float
    bulletDamage: float
    bulletVelocity: float
    shootCooldown: float
    tank_id: str
        
    def __post_init__(self):
        Object.__init__(self)
        self.width = 74
        self.height = 152
        self.controller = TankController(self)

    def init(self, game: Game):
        self.game = game
        self.shoot_timer = Timer()
        self.deltaVelocity = 0
        self.deltaAngle = 0

    def start(self):
        self.shoot_timer.start()

    def move_forward(self):
        self.deltaVelocity = self.velocity

    def move_backward(self):
        self.deltaVelocity = -self.velocity

    def rotate_left(self):
        self.deltaAngle = -90

    def rotate_right(self):
        self.deltaAngle = 90

    def update(self):
        self.reflect_deltas()
        self.reset_deltas()
        self.handle_collision()

    def reflect_deltas(self):
        self.old_posX = self.posX
        self.old_posY = self.posY
        self.old_angle = self.angle
        # for performance efficiency check if there is something to multiply
        if self.deltaAngle != 0:
            self.angle += self.deltaAngle * self.game.timer.get_delta_time()
        if self.deltaVelocity != 0:
            dir = get_direction(self.angle) * self.deltaVelocity * self.game.timer.get_delta_time()
            self.posX += dir.x
            self.posY += dir.y


    def handle_collision(self):
        for o in self.game.objects:
            if (self != o and object_intersect(self, o)):
                if (isinstance(o, TankT34)):
                    self.posX = self.old_posX
                    self.posY = self.old_posY
                    self.angle = self.old_angle
                elif (isinstance(o, Bullet)):
                    self.health -= o.damage
                    o.destroy()
                    if (self.health <= 0):
                        self.destroy()

    def reset_deltas(self):
        self.deltaAngle = 0
        self.deltaVelocity = 0

    def shoot(self):
        # print(f"tank shoot: {self.shoot_timer.get_elapsed_time()}")
        if self.shoot_timer.get_elapsed_time() < self.shootCooldown or not self.alive:
            return
        
        self.shoot_timer.start()
        bX, bY = rotate_coordinate_clockwise(-self.angle, (self.posX + 90, self.posY), (self.posX, self.posY))
        b = Bullet(
            posX=bX, 
            posY=bY, 
            angle=self.angle, 
            velocity=self.bulletVelocity, 
            damage=self.bulletDamage,
            lifeSpan=5
        )
        self.game.add_recent_object(b)
