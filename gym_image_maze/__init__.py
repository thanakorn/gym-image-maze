from gym.envs.registration import register

register(
    id='image-maze-v0',
    entry_point='gym_image_maze.envs:ImageMaze',
)