import unittest
import os
from envs.image_maze_env import ImageMazeEnv

class MazeEnvTest(unittest.TestCase):
    def test_maze_env_create_maze(self):
        env = ImageMazeEnv(os.path.join(os.getcwd(), 'gym_image_maze/tests/maze_config.json'))
        maze = env.maze
        self.assertEqual(maze.size, 36)
        self.assertEqual(maze.robot.size, 2)
        self.assertEqual(maze.robot.position, (5, 30))
        self.assertEqual(maze.goal, (5,5))
        self.assertEqual(len(maze.walls), 7) # Walls and 4 borders
        self.assertEqual(maze.walls[4].a, (0, 10))
        self.assertEqual(maze.walls[4].b, (8, 10))
        self.assertEqual(maze.walls[5].a, (20, 25))
        self.assertEqual(maze.walls[5].b, (20, 35))
        self.assertEqual(maze.walls[6].a, (15, 25))
        self.assertEqual(maze.walls[6].b, (25, 25))
        
    def test_maze_env_done(self):
        env = ImageMazeEnv(os.path.join(os.getcwd(), 'gym_image_maze/tests/blank_maze_config.json'))
        # 0: Left, 1: Right, 2: Up, 3: Down 
        env.step(0)
        env.step(0)
        env.step(0)
        self.assertFalse(env.done)
        env.step(2)
        env.step(2)
        self.assertFalse(env.done)
        env.step(2)
        print(env.maze.robot.position)
        self.assertTrue(env.done)