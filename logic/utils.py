import core
from logic import api
import pygame
from math import sin, cos, pi, radians
from itertools import combinations

def parse_tank(t :core.entities.Tank)->api.Tank:
    pass

def get_direction(angle: float) ->pygame.Vector2:
    return pygame.math.Vector2(1, 0).rotate(angle)

def rotate_coordinate_clockwise(angle: float, coord: tuple, origin: tuple = (0, 0)):
    x, y = coord
    ox, oy = origin
    x -= ox
    y -= oy
    angle = radians(angle)
    return ((x * cos(angle) + y * sin(angle) + ox), (- x * sin(angle) + y * cos(angle) + oy))

def line_intersect(l1_start: tuple, l1_end: tuple, l2_start: tuple, l2_end: tuple):

    x1, y1 = l1_start
    x2, y2 = l1_end
    x3, y3 = l2_start
    x4, y4 = l2_end

    # Check if none of the lines are of length 0
    if ((x1 == x2 and y1 == y2) or (x3 == x4 and y3 == y4)):
        return False

    denominator = ((y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1))

    # Lines are parallel
    if (denominator == 0):
        return False

    ua = ((x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)) / denominator
    ub = ((x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)) / denominator

    # is the intersection along the segments
    if (ua < 0 or ua > 1 or ub < 0 or ub > 1):
        return False

    # # Return a object with the x and y coordinates of the intersection
    # x = x1 + ua * (x2 - x1)
    # y = y1 + ua * (y2 - y1)

    return True

def get_vertices(pos: tuple, width: float, height: float):
    x, y = pos
    vertices = [
        (x - width / 2, y - height / 2), # top left vertex
        (x + width / 2, y - height / 2), # top right vertex
        (x - width / 2, y + height / 2), # bottom left vertex
        (x + width / 2, y + height / 2) # bottome right vertex
    ]
    return vertices

def inside(point: tuple, vs: list):
    x, y = point
    lines = [(0, 1), (0, 2), (1, 3), (2, 3)]
    
    inside = False
    for i, j in lines:
        xi, yi = vs[i][0], vs[i][1]
        xj, yj = vs[j][0], vs[j][1]

        intersect = ((yi > y) != (yj > y)) and (x < (xj - xi) * (y - yi) / (yj - yi) + xi)

        if (intersect):
            inside = not inside
    
    return inside

def object_intersect(obj1, obj2):
    pos1 = (obj1.posX, obj1.posY)
    pos2 = (obj2.posX, obj2.posY)
    ver1 = get_vertices(pos1, obj1.width, obj1.height)
    ver2 = get_vertices(pos2, obj2.width, obj2.height)
    
    for i in range(4): # rotate vertices
        ver1[i] = rotate_coordinate_clockwise(obj1.angle, ver1[i], pos1)
        ver2[i] = rotate_coordinate_clockwise(obj2.angle, ver2[i], pos2)
    
    for i in range(4):
        if (inside(ver1[i], ver2)):
            return True
    
    return False
    