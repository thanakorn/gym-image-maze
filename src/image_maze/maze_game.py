import pyglet
import numpy as np
import ctypes
import cv2 as cv
from pyglet.window import Window, key
from pyglet.image import ImageData
from pyglet.gl import glClearColor
from src.image_maze.maze import Maze
from src.image_maze.models import Action

class MazeGame(Window):
    def __init__(self, maze: Maze, height: int, width: int):
        display = pyglet.canvas.get_display()
        screen = display.get_screens()[0]
        config = screen.get_best_config()
        context = config.create_context(None)
        super().__init__(width=width, height=height, config=config, context=context)

        self.maze = maze
        self.width = width
        self.height = height
        self.alive = True

    def on_draw(self):
        self.render()

    def on_key_press(self, symbol, modifiers):
        if symbol == key.MOTION_UP:
            self.maze.move_robot(Action.Up)
        elif symbol == key.MOTION_RIGHT:
            self.maze.move_robot(Action.Right)
        elif symbol == key.MOTION_LEFT:
            self.maze.move_robot(Action.Left)
        elif symbol == key.MOTION_DOWN:
            self.maze.move_robot(Action.Down)

    def render(self):
        self.clear()
        glClearColor(1,1,1,1)
        img = self.maze_to_image()
        img = np.ascontiguousarray(img[::-1, :])
        img_c_array = img.ctypes.data_as(ctypes.POINTER(ctypes.c_float * img.size))
        img_data = ImageData(img.shape[0], img.shape[1], 'L', img_c_array)
        img_data.blit(0, 0)
        self.flip()

    def run(self):
        while self.alive:
            self.render()
            event = self.dispatch_events()
            # Check exit condition
            if self.maze.is_robot_reach_goal():
                self.alive = False

        self.close()

    def maze_to_image(self):
        BLACK = (0,0,0)
        img = np.ones((self.maze.size, self.maze.size), dtype=np.uint8) * 255
        cv.circle(img, (self.maze.robot.position), self.maze.robot.size, BLACK, -1)
        cv.circle(img, (self.maze.goal), 1, BLACK, -1)
        for wall in self.maze.walls:
            cv.line(img, wall.a, wall.b, BLACK)
        img = cv.resize(img, (self.height, self.width), interpolation=cv.INTER_NEAREST)
        return img