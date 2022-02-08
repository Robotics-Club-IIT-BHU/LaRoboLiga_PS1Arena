from gym_line_follower.helper import LaRoboLigaEnv

if __name__=="__main__":
    Ps1Bot=LaRoboLigaEnv()
    while True:
        Ps1Bot.set_velocity([0.1,0.1])