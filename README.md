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

## create a 2d map by gazebo_ros_2Dmap_plugin
Check out the plugin in your catkin_ws and build it with catkin_make. To include the plugin, add the following line in between the <world> </world> tags of your Gazebo world file:
```
<plugin name='gazebo_occupancy_map' filename='libgazebo_2Dmap_plugin.so'>
    <map_resolution>0.1</map_resolution> <!-- in meters, optional, default 0.1 -->
    <map_height>0.3</map_height>         <!-- in meters, optional, default 0.3 -->
    <map_size_x>10</map_size_x>          <!-- in meters, optional, default 10 -->
    <map_size_y>10</map_size_y>          <!-- in meters, optional, default 10 -->
    <init_robot_x>0</init_robot_x>          <!-- x coordinate in meters, optional, default 0 -->
    <init_robot_y>0</init_robot_y>          <!-- y coordinate in meters, optional, default 0 -->
</plugin>
```

To generate the map, call the /gazebo_2Dmap_plugin/generate_map ros service:
```
rosservice call /gazebo_2Dmap_plugin/generate_map
```

The generated map is published on the /map2d ros topic.
You can use the map_saver node from the map_server package inside ros navigation to save your generated map to a .pgm and .yaml file:
```
rosrun map_server map_saver -f <mapname> /map:=/map2d
```