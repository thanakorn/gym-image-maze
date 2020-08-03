import gym
import json
import numpy as np
import os

from gym import error, spaces, utils
from gym.utils import seeding
from envs.models import *
from envs.maze import Maze
from envs.renderer import Renderer

SCREEN_SIZE = 300

class ImageMazeEnv(gym.Env):
    
    metadata = {
        "render.modes": ["human", "rgb_array"],
    }
    
    ALL_ACTIONS = [Action.Left, Action.Right, Action.Up, Action.Down, Action.Stop]
    
    def __init__(self, config_file):
        self.config_file = config_file
        self.done = False
        self.maze = ImageMazeEnv.create_maze(config_file)
        self.action_space = spaces.Discrete(len(self.ALL_ACTIONS))
        low = np.zeros((self.maze.size, self.maze.size), dtype=np.uint8)
        high = np.ones((self.maze.size, self.maze.size), dtype=np.uint8) * 255
        self.observation_space = spaces.Box(low, high)
        self.renderer = None
        
    def step(self, action):
        self.maze.move_robot(self.ALL_ACTIONS[action])
        # TODO: Add reward
        reward = 0
        # TODO: Determine whether the game is done
        done = False
        return self.maze.to_image(), reward, {}
    
    def reset(self):
        self.maze = ImageMazeEnv.create_maze(self.config_file)
        self.done = False
        return self.maze.to_image()
    
    def render(self, mode='human'):
        if self.renderer is None:
            self.renderer = Renderer(SCREEN_SIZE, SCREEN_SIZE)
        self.renderer.render(self.maze.to_image(SCREEN_SIZE))
    
    def close(self):
        self.renderer.close()
    
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