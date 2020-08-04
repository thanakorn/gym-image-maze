from gym.envs.registration import register

register(
    id='ImageMaze-v0',
    entry_point='gym_image_maze.envs:ImageMazeV0',
)