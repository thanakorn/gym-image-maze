import gym
import json
import numpy as np
import os

from gym import error, spaces, utils
from gym.utils import seeding
from envs.models import *
from envs.maze import Maze

class ImageMazeEnv(gym.Env):
    
    metadata = {
        "render.modes": ["human", "rgb_array"],
    }
    
    ALL_ACTIONS = [Action.Left, Action.Right, Action.Up, Action.Down, Action.Stop]
    
    def __init__(self, config_file):
        self.maze = ImageMazeEnv.create_maze(config_file)
        self.action_space = spaces.Discrete(len(self.ALL_ACTIONS))
        low = np.zeros((self.maze.size, self.maze.size), dtype=np.uint8)
        high = np.ones((self.maze.size, self.maze.size), dtype=np.uint8) * 255
        self.observation_space = spaces.Box(low, high)
        
        self.seed()
        self.reset()
        
    def step(self, action):
        pass
    
    def reset(self):
        pass
    
    def render(self, mode='human'):
        pass
    
    def close(self):
        pass
    
    @classmethod
    def create_maze(cls, config_file):
        maze_config = json.load(open(config_file))
        maze_size = maze_config['size']
        robot_pos = maze_config['robot']['x'], maze_config['robot']['y']
        robot_size = maze_config['robot']['size']
        goal_pos = maze_config['goal']['x'], maze_config['goal']['y']
        walls = [Wall((config['ax'], config['ay']), (config['bx'], config['by'])) for config in maze_config['walls']]
        maze = Maze(maze_size, robot_pos, robot_size, goal_pos, walls)
        return maze