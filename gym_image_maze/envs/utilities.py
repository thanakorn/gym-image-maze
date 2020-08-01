import math

def add_tuple(t1, t2):
    return tuple(map(lambda a, b: a + b, t1, t2))

def distance(a, b):
    ax, ay = a
    bx, by = b
    return math.sqrt((ax - bx)**2 + (ay - by)**2)