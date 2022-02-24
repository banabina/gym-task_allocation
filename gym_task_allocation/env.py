import gym
from gym import spaces

class TaskAllocationEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        pass

    def reset(self):
        pass

    def step(self, action):
        pass

    def render(self, mode='human', close=False):
        if close:
            return
        pass