import gym
import gym_image_maze

if __name__=='__main__':
    env = gym.make('ImageMaze-v0')
    env.reset()
    for i in range(1000):
        env.render()
        env.step(env.action_space.sample())
    env.close()