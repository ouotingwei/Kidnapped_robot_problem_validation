The Turtlebot3 packages installation on ROS noetic

References: https://www.ncnynl.com/archives/201702/1398.html

Environment: Ubuntu 20.04 / ROS noetic

Installation Dependencies:
```
sudo apt-get install ros-noetic-turtlebot3-teleop
sudo apt-get install ros-noetic-turtlebot3-description
sudo apt-get install ros-noetic-turtlebot3-msgs
```

## test:
```
export TURTLEBOT3_MODEL=burger
roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch
```

use another terminal:
```
export TURTLEBOT3_MODEL=burger
roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch
```
## create a new map
    use another terminal:
    ```
    rosrun tf static_transform_publisher 0.20 0 0 0 0 0 base_footprint scan 50
    ```
    gmapping:
    '''
    roslaunch gmapping_ros slam_gmapping.launch
    '''

    save the map:
    ```
    rosrun map_server map_saver -f "MAP_NAME"
    ```
## launch amcl
```
roslaunch turtlebot3_navigation amcl.launch 
```