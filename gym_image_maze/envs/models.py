from enum import Enum

class Action(Enum):
    Left    = (-1, 0)
    Right   = (1, 0)
    Up      = (0, -1)
    Down    = (0, 1)
    
class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
class Robot(object):
    def __init__(self, position, radius):
        self.position = position
        self.radius = radius
        
    def move(self, action):
        dx, dy = action
        self.position.x += dx * (self.radius * 2)
        self.position.y += dy * (self.radius * 2)

class Wall(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def length(self):
        return math.sqrt((self.a.x - self.b.x)**2 + (self.a.y - self.b.y)**2)