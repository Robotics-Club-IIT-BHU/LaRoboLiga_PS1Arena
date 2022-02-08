import numpy 
import gym_line_follower
import gym
import time
import pybullet as p 
import pybullet_data

class LaRoboLigaEnv(gym.Env):
    def __init__(self):
        self.env = gym.make("LineFollower-v0")
        _,self.path=self.env.reset()

    def get_full_path(self):
        return self.path

    def reset(self):
        _,self.path=self.env.reset()

    def set_velocity(self,array):
        obs,reward,done,info=self.env.step(array)
        return info,done