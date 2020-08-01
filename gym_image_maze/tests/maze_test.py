import unittest
from envs.maze import Maze
from envs.models import Wall

class MazeTest(unittest.TestCase):
    def test_maze_init(self):
        maze = Maze(size=84, robot_pos=(10, 70), robot_size=2, goal_pos=(10,10))
        self.assertEqual(maze.size, 84)
        self.assertEqual(maze.robot.position, (10, 70))
        self.assertEqual(maze.robot.size, 2)
        self.assertEqual(maze.goal, (10, 10))
        
    def test_maze_init_add_borders(self):
        maze = Maze(size=10, robot_pos=(3, 5), robot_size=2, goal_pos=(2,2))
        self.assertEqual(len(maze.walls), 4)
        self.assertEqual(maze.walls[0].a, (0,0))
        self.assertEqual(maze.walls[0].b, (9,0))
        self.assertEqual(maze.walls[1].a, (0,0))
        self.assertEqual(maze.walls[1].b, (0,9))
        self.assertEqual(maze.walls[2].a, (0,9))
        self.assertEqual(maze.walls[2].b, (9,9))
        self.assertEqual(maze.walls[3].a, (9,9))
        self.assertEqual(maze.walls[3].b, (9,0))
        
    def test_maze_init_add_walls(self):
        walls = [
            Wall((0,4), (3,4)), 
            Wall((7,0), (7,3))
        ]
        maze = Maze(size=10, robot_pos=(3, 7), robot_size=2, goal_pos=(2,2), walls=walls)
        self.assertEqual(len(maze.walls), 6)
        self.assertEqual(maze.walls[4].a, (0,4))
        self.assertEqual(maze.walls[4].b, (3,4))
        self.assertEqual(maze.walls[5].a, (7,0))
        self.assertEqual(maze.walls[5].b, (7,3))
        