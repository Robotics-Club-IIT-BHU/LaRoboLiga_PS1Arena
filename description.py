from gym_line_follower.helper import LaRoboLigaEnv
import time

if __name__ == "__main__":
    husky = LaRoboLigaEnv()

    print("get_full_path function--")
    print(husky.get_full_path.__doc__)

    print("reset function--")
    print(husky.reset.__doc__)

    print("set_velocity function--")
    print(husky.set_velocity.__doc__)

    print("get_position function--")
    print(husky.get_position.__doc__)
