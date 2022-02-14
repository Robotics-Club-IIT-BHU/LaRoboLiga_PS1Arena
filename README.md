<p align="center">
  <img src="https://user-images.githubusercontent.com/78701055/153015710-c1be76dd-5cd1-47fc-976f-d687d16584f1.jpeg" alt="ROBOTICS CLUB IIT BHU">
<h1 align="center">~ PS1 ARENA ~</h1>
</p>
La Robo Liga is a Robot-Control and Image-Processing based Robotics Competition being organized by the Robotics Club, IIT (BHU), Varanasi so that we can learn about image processing, simulating robots and can also control them with help of algorithms and come out of pandemic blues. 

This repo holds the first problem statement of event and its arena. The Arena is in the form of an OpenAI gym and runs on python libraries like `Pybullet` and `OpenCV`.

You can learn its installation from <a href="https://www.youtube.com/watch?v=YrbAudk7ipE">here</a>


<p align="center">
  
  <img width="45%" src="https://user-images.githubusercontent.com/78701055/153232739-e7645871-6fae-4fdb-8b83-d01b6f3c070f.png" alt="Loading arena">
  <img width="49.5%" src="https://i.imgur.com/ZRJN3gu.gif" alt="Loading arena">
</p>
<hr>



## Installation

We recommend you to go through the pybullet and OpenCV installation video before moving forward to setup the project. 

### STEP 1: Clone  repository using this command:
```bash
git clone https://github.com/Robotics-Club-IIT-BHU/FreshersEvent_PS1Arena.git
```


### STEP 2: Change your current directory to the env's root.
```bash
cd LaRoboLiga_PS1Arena/gym-line-follower-env/
```


### STEP 3: Install environment using command.
```bash
pip install -e .
```


#### Test your setup by running solution.py file.
#### There is also a description.py file, running which will introduce you to the env functions, arguments they need and their return types.
<hr>

## Objective

The goal of this round is to make the robot car follow the line given in the arena by controlling the motors of the robot car. The movement of the robot has to be entirely autonomous. If the car comes back to its initial position after completing one lap of the track, the objective of the PS will be achieved. You may refer to this [workshop](https://youtu.be/RkHvUSGgw6Q) for insights into robot controls. 

## Using the Arena

1. Run the test.py file. If you see the bot moving with forward velocity, Voila! Your installation is complete.

2. In test.py, you'll see a working loop. You'll have to write the code to control the robot within this working loop. 

3. There are several functions in [helper.py](https://github.com/Robotics-Club-IIT-BHU/FreshersEvent_PS1Arena/blob/main/gym-line-follower-env/gym_line_follower/helper.py) for you to navigate the arena. Their names and use cases are as follows: 

   - `husky.get_full_path()` 
     This function will return an array of the path. Each element of this array will have the x and y coordinates of the path at the 0th and 1st index. 
   - `husky.reset()` 
     Once this function is run, the present arena will be replaced with another with a new random path and the husky initilized to one of the points in this path. 
   - `husky.setvelocity([v, v])`
     Use this function to manipulate the velocity of the husky wheels. This function takes an array of two values. The value at 0th index will be the velocity of the front and rear left motors while the value at 1st indext will be the velocity of the front and rear right motors. 
   - `husky.getposition()`
     This function will return the x & y coordinates and the yaw angle of the robot. 

   You may look into the file to explore the working of these function and to add or remove functions of your own.
   

## Sample Use of Arena

 <p align="center">
  <img width="100%" src="https://i.imgur.com/yLoWS3F.gif" alt="Loading arena">
</p>

Note: this Arena is only for reference. The track is randomized and changes every time `husky.reset()` is run. 

## Made and maintained by 

|<img src="https://avatars.githubusercontent.com/u/78701055?v=4" alt="drawing" width="150"/> | <img src="https://avatars.githubusercontent.com/u/74451989?v=4" alt="drawing" width="150"/> | 
|--|--|
|[Ankur Agarwal](https://github.com/Ankur-Agrawal-ece20) |[Pratik Mishra](https://github.com/DolceParadise) |
