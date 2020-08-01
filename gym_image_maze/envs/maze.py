from models import Robot, Wall, Action
from typing import List
import cv2 as cv
import numpy as np

SIZE = (84,84)
BALCK = (0,0,0)

class Maze(object):
    def __init__(self, size, robot_pos, robot_size, goal_pos, walls: List[Wall]):
        self.size = size
        self.robot = Robot(robot_pos, robot_size)
        self.goal = goal_pos
        self.walls = walls
        # Add borders
        height, width = SIZE
        walls.append(Wall((0, 0), (width - 1, 0)))
        walls.append(Wall((0, 0), (0, height - 1)))
        walls.append(Wall((0, height - 1), (height - 1, width - 1)))
        walls.append(Wall((0, height - 1), (height - 1, width - 1)))
        walls.append(Wall((width - 1, height - 1), (width - 1,0)))
        
        
    def to_image(self, size):
        img = np.ones((self.size, self.size), dtype=np.uint8) * 255
        cv.circle(img, (self.robot.position), self.robot.size, BALCK, -1)
        cv.circle(img, (self.goal), 1, BALCK, -1)
        for wall in self.walls:
            cv.line(img, wall.a, wall.b, BALCK)
        img = cv.resize(img, (size, size), interpolation=cv.INTER_NEAREST)
        return img