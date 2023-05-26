# Python Waypoints

This program provides a very easy way to input many waypoints to ROS2 Navigation2 robot atonomous driving.

The waypoints are stored in a small text file in your home folder. "Python Waypoints" reads these data lines and feeds them to the navigation stack in order to direct the robot. This method makes it easy to make changes in the route and save your work and return to it and run it another time.

This repository was tested with Ubuntu Jammy, ROS2 Humble, Linorobot2, and the Gazebo Playground world.

The supplied sample data file works with this software stack and that world. It will work with any world, as long as the world is of sufficient size.

The data file should be composed of X and Y coordinates, in float numbers. (Having a decimal and at least one number right of the decimal.) The third number on each line is the rotation of the final robot pose in degrees, like in nautical or airplane travel. This is the pose the robot will rotate to at the end of driving to the specified point.

## Nautical Directions

North = 0, South = 180, East = 90, and West = 270 degrees. Separate each number on the line by one space. Each line should have three numbers. Don't include a blank line at the end of the data file; the last line should have data. Don't include other remarks or comments, simply numbers and spaces. Make the file with a simple text editor. Call the file "security_route_data.txt" and save it in your home folder. This file name can be changed in the program code, of course, if another name is desired.

The X, Y data information may be found from showing the topic of a "clicked point" or pose of the robot while driving, either in simulation or using the real robot.

A launch file is not needed for this program but one may be developed. All that is needed to run it is the line:

    ros2 run python_waypoints python_waypoints

Other command lines used (in additional terminals) testing this program in simulation:

    ros2 launch linorobot2_gazebo gazebo.launch.py
    ros2 launch nav2_bringup bringup_launch.py params_file:="/home/russ/Bags-Maps/nav2-4.yaml" use_sim_time:=true map:="/home/russ/playground45.yaml"
    ros2 launch linorobot2_viz navigation2.launch.py use_sim_time:=true map:="/home/russ/playground45.yaml"

## Installation

Copy this repo to a source folder under your Ros2 workspace and compile with "colcon build" Then source the setup.bash

The Nav2 software stack must be installed as well as the Ros2 stack for using this package. The Nav2 "simple commander" program is used by "Python Waypoints" to do the robot driving. Click the "initial robot position" button in Rviz to input the beginning pose.

It may be seen that my testing used a saved map for Nav2 and Rviz. This is preferable but not necessary. As long as the waypoints are not outside of the world, the world may be mapped by waypoint following, as long as the robot can reach each point. (The points are not covered by obstacles)

Thanks to Linorobot2 and Turtlebot4 tutorials, and of course, Ros2 and Navigation2!


