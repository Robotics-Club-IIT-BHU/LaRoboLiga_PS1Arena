import numpy
import gym_line_follower
import gym
import time
import pybullet as p
import pybullet_data


class LaRoboLigaEnv(gym.Env):
    def __init__(self,descr_mode=False):
        if descr_mode:
            return
        self.env = gym.make("LineFollower-v0")
        _, self.path = self.env.reset()

    def get_full_path(self):
        """
        Function Description: 
            Returns the full path of the environment

        Arguments: 
            None

        Returns: 
            path: list of tuples containing the coordinates of the path

        NOTE: The path is returned in the format [(x1, y1), (x2, y2), ...]
        """
        return self.path

    def reset(self):
        """
        Function Description: 
            Resets the path and the husky to the starting position

        Arguments: 
            None

        Returns: 
            None

        NOTE: A new path is generated every time the environment is reset
        """
        _, self.path = self.env.reset()

    def set_velocity(self, array):
        """
        Function Description: 
            Sets the velocity of the husky

        Arguments: 
            array: array of length 2 
                array[0] = linear velocity of left front and rear motors
                array[1] = linear velocity of right front and rear motors

        Returns: 
            None

        """
        self.observation, self.reward, self.done, self.info = self.env.step(
            array)

    def get_position(self):
        """
        Function Description: 
            Returns the current position of the husky in the environment

        Arguments: 
            None

        Returns: 
            pos: dictionary containing the position of the husky
                pos['x'] = x coordinate of the husky
                pos['y'] = y coordinate of the husky
                pos['yaw'] = yaw of the husky

        """
        position = self.info
        return position
