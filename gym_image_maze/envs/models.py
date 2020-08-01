from enum import Enum
from envs.utilities import distance, map_tuple
from operator import *

class Action(Enum):
    Left    = (-1, 0)
    Right   = (1, 0)
    Up      = (0, -1)
    Down    = (0, 1)
    Stop    = (0, 0)
    
class Reward(Enum):
    Closer  = 1
    Further = -1
    Goal    = 1000
        
class Robot(object):
    def __init__(self, position, size):
        self.position = position
        self.size = size
        
    def move(self, action):
        d = map_tuple(mul, (self.size, self.size), action.value)
        self.position = map_tuple(add, self.position, d)

class Wall(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def length(self):
        return distance(self.a, self.b)