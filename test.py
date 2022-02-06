import numpy 
import gym_line_follower
import gym
import time
import pybullet as p 
import pybullet_data

if __name__=="__main__":
    env = gym.make("LineFollower-v0")
    _,path=env.reset()
    print(path)
    while True:
        # action= select random action from your action space
        env.step([1,-1])