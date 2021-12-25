from src.image_maze.maze import Maze
from src.image_maze.maze_game import MazeGame

if __name__=='__main__':
    maze = Maze.from_config('./configs/image_maze_v0.json')
    window = MazeGame(maze, 500, 500)
    window.run()