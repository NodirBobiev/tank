import pygame

def get_direction(angle: float) ->pygame.Vector2:
    return pygame.math.Vector2(1, 0).rotate(angle) 