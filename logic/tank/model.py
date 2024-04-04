from logic.tank.common import Tank
from logic.bullet.model import Bullet
from dataclasses import dataclass
from logic.utils import get_direction
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
        
    def __post_init__(self):
        Object.__init__(self)

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

    def reflect_deltas(self):
        # for performance efficiency check if there is something to multiply
        if self.deltaAngle != 0:
            self.angle += self.deltaAngle * self.game.timer.get_delta_time()
        if self.deltaVelocity != 0:
            dir = get_direction(self.angle) * self.deltaVelocity * self.game.timer.get_delta_time()
            self.posX += dir.x
            self.posY += dir.y

    def reset_deltas(self):
        self.deltaAngle = 0
        self.deltaVelocity = 0

    def shoot(self):
        print(f"tank shoot: {self.shoot_timer.get_elapsed_time()}")
        if self.shoot_timer.get_elapsed_time() < self.shootCooldown:
            return
        
        self.shoot_timer.start()
        b = Bullet(
            posX=self.posX, 
            posY=self.posY, 
            angle=self.angle, 
            velocity=self.bulletVelocity, 
            damage=self.bulletDamage,
            lifeSpan=100
        )
        self.game.add_recent_object(b)
