import math
import operator

def map_tuple(f, t1, t2):
    return tuple(map(lambda a, b: f(a, b), t1, t2))

def distance(a, b):
    ax, ay = a
    bx, by = b
    return math.sqrt((ax - bx)**2 + (ay - by)**2)

def dist_from_point_to_line(point, line_start, line_end):
    return 0.0