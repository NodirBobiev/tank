from dataclasses import dataclass

@dataclass
class Tank:
    posX: float = 0
    posY: float = 0
    velocity: float = 0
    angle: float = 0
    health: float = 0
    bulletDamage: float = 0
    bulletVelocity: float = 0
    shootCooldown: float = 0
    lastShootTime: float = 0

if __name__=="__main__":
    t = Tank()

    print(t)
