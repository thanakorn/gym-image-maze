import math
from models import Point

def distance(a: Point, b: Point):
    return math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)