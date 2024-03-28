import core.entities
from logic import api
import pygame

# def parse_tank(t :core.entities.Tank)->api.Tank:
#     pass

def get_direction(angle: float) ->pygame.Vector2:
    return pygame.math.Vector2(1, 0).rotate(angle) 