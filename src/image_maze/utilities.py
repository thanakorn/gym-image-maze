import math
import cv2 as cv
import numpy as np

def map_tuple(f, t1, t2):
    return tuple(map(lambda a, b: f(a, b), t1, t2))

def distance(a, b):
    ax, ay = a
    bx, by = b
    return math.sqrt((ax - bx)**2 + (ay - by)**2)

def dist_from_point_to_line(point, line_start, line_end):
    px, py = point
    ax, ay = line_start
    bx, by = line_end
    line_length = distance(line_start, line_end)
    r = ((px - ax) * (bx - ax) + (py - ay) * (by - ay)) / (line_length ** 2)
    closest_point_in_line = ax + (r * (bx - ax)), ay + (r * (by - ay))
    
    if r >= 0. and r <= 1.: # closest point is on the line
        return distance(point, closest_point_in_line)
    else:                  # closest point is not on the line
        return min(distance(point, line_start), distance(point, line_end))

def to_maze_image(maze, img_size):
    BALCK = (0,0,0)
    img = np.ones((maze.size, maze.size), dtype=np.uint8) * 255
    cv.circle(img, (maze.robot.position), maze.robot.size, BALCK, -1)
    cv.circle(img, (maze.goal), 1, BALCK, -1)
    for wall in maze.walls:
        cv.line(img, wall.a, wall.b, BALCK)
    if img_size is not None:
        img = cv.resize(img, img_size, interpolation=cv.INTER_NEAREST)
    return img