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
    
    def __init__(self, config_file, time_limit):
        self.config_file = config_file
        self.time_limit = time_limit
        self.timestep = 0
        self.done = False
        
        self.maze = ImageMazeEnv.create_maze(config_file)
        self.action_space = spaces.Discrete(len(self.ALL_ACTIONS))
        low = np.zeros((self.maze.size, self.maze.size), dtype=np.uint8)
        high = np.ones((self.maze.size, self.maze.size), dtype=np.uint8) * 255
        self.observation_space = spaces.Box(low, high)
        self.renderer = None
        
    def step(self, action):
        action = self.ALL_ACTIONS[action]
        self.timestep += 1
        
        current_dist_to_goal = self.maze.dist_to_goal()
        self.maze.move_robot(action)
        new_dist_to_goal = self.maze.dist_to_goal()
        self.done = self.maze.is_robot_reach_goal() or (self.timestep == self.time_limit)
        
        is_collide = False if action == Action.Stop else current_dist_to_goal == new_dist_to_goal
        
        reward = 0.
        if self.maze.is_robot_reach_goal():
            reward = Reward.Goal
        elif is_collide:
            reward = Reward.Collide
        elif action == Action.Stop:
            reward = Reward.Same
        elif new_dist_to_goal < current_dist_to_goal:
            reward = Reward.Closer
        else:
            reward = Reward.Further
        
        return self.maze.to_image(), reward.value, self.done, {}
    
    def reset(self):
        self.maze = ImageMazeEnv.create_maze(self.config_file)
        self.done = False
        self.timestep = 0 
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
    
def get_config_path():
    dir_path = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(dir_path, 'configs')
    return config_path

class ImageMazeV0(ImageMazeEnv):
    def __init__(self):
        config_file = 'image_maze_v0.json'
        super().__init__(config_file=os.path.join(get_config_path(), config_file), time_limit=100)
        
class ImageMazeV1(ImageMazeEnv):
    def __init__(self):
        config_file = 'image_maze_v1.json'
        super().__init__(config_file=os.path.join(get_config_path(), config_file), time_limit=100)