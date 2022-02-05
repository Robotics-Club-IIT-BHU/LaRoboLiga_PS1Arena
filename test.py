import numpy 
import gym_line_follower
import gym
import time

if __name__=="__main__":
    env = gym.make("LineFollower-v0")
    env.reset()
    while True:
        # action= select random action from your action space
        env.step([0.1,0.1])
