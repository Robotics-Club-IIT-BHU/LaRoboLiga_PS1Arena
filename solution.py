from gym_line_follower.helper import LaRoboLigaEnv
import math
if __name__ == "__main__":
    husky = LaRoboLigaEnv()
    velocity = 0.1  # Velocity
    while True:
        husky.set_velocity([velocity, velocity])
