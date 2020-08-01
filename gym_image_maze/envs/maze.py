import cv2 as cv
import numpy as np

from typing import List
from envs.models import Robot, Wall, Action, Reward
from envs.utilities import distance, map_tuple, dist_from_point_to_line

BALCK = (0,0,0)

class Maze(object):
    def __init__(self, size, robot_pos, robot_size, goal_pos, walls: List[Wall] = []):
        self.size = size
        self.robot = Robot(robot_pos, robot_size)
        self.goal = goal_pos
        # Add borders
        height, width = (size, size)
        self.walls = [
            Wall((0, 0), (width - 1, 0)),
            Wall((0, 0), (0, height - 1)),
            Wall((0, height - 1), (height - 1, width - 1)),
            Wall((width - 1, height - 1), (width - 1,0))
        ]
        self.walls.extend(walls)
        
    def move_robot(action: Action):
        new_pos = add_tuple(new_pos, action)
        if not self.collide(new_pos):
            self.robot.move(action)
        
    def to_image(self, size):
        img = np.ones((self.size, self.size), dtype=np.uint8) * 255
        cv.circle(img, (self.robot.position), self.robot.size, BALCK, -1)
        cv.circle(img, (self.goal), 1, BALCK, -1)
        for wall in self.walls:
            cv.line(img, wall.a, wall.b, BALCK)
        img = cv.resize(img, (size, size), interpolation=cv.INTER_NEAREST)
        return img
    
    def collide(self, pos):
        # for wall in self.walls:
        #     if dist_from_point_to_line(pos, wall.a, wall.b) < self.robot.size:
        #         return True
        # return False
        return False