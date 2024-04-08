from logic.api import Object
from logic.utils import get_direction
from logic.time.timer import Timer
from logic.game import Game
from dataclasses import dataclass

@dataclass
class Bullet(Object):
    posX : float
    posY : float
    angle: float
    velocity: float
    damage: float
    lifeSpan: float
    
    def __post_init__(self):
        Object.__init__(self)

    def init(self, game: Game):
        self.game = game
        self.life_timer = Timer()
    
    def start(self):
        self.life_timer.start()

    def update(self):
        if self.life_timer.get_elapsed_time() > self.lifeSpan:
            self.destroy()
            return
        dir = get_direction(self.angle) * self.velocity * self.game.timer.get_delta_time()
        self.posX += dir.x
        self.posY += dir.y
   