from enum import Enum
from utilities import distance, add_tuple

class Action(Enum):
    Left    = (-1, 0)
    Right   = (1, 0)
    Up      = (0, -1)
    Down    = (0, 1)
    Stop    = (0, 0)
        
class Robot(object):
    def __init__(self, position, size):
        self.position = position
        self.size = size
        
    def move(self, action):
        self.position = add_tuple(self.position, action)

class Wall(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def length(self):
        return distance(self.a, self.b)