from copy import deepcopy
from geometry_msgs.msg import PoseStamped
from nav2_simple_commander.robot_navigator import BasicNavigator, TaskResult
import rclpy
import math
"""
Basic security route patrol demo. In this demonstration, the expectation
is that there are security cameras mounted on the robots recording or being
watched live by security staff.
From Ros2_learners repo
This version uses a text file to input waypoints. Robot heading is in degrees
North = 0, E = 90, S = 180, W = 270, matching nautical.
Simply put in x and y positions and rotation, separated by one space, on each line.
Line 38 has data file name in home folder. Position data must be float. Rotation is integer.
Do not end data file with blank line
"""
def lineToData(line):
    """Converts a raw line list into an
       appropriate data format."""
    return (float(line[0]), float(line[1]), int(line[2]))

def readData(fileName):
    """Generic data reading function:
       reads lines in a text file and
       splits them into lists."""
    data = []
    with open(fileName) as f:
        for line in f.readlines():
            data.append(lineToData(line.split()))
    return data  
#pairs = readData('upper_playground_data.txt')
#for x, y in pairs:
#    print("pose position.", x)
#    print("Pose position.", y)
def main():
    rclpy.init()
    navigator = BasicNavigator()
    triples = readData('security_route_data.txt')  
    # Security route, read in from text file
    # Set robot's initial pose in Rviz
    # Wait for navigation to fully activate
    navigator.waitUntilNav2Active()
    # Do security route once
    
    while rclpy.ok():
        # Send our route
        poses = []
        pose = PoseStamped()
        pose.header.frame_id = 'map'
        pose.header.stamp = navigator.get_clock().now().to_msg()
        for x, y, rotation in triples:
            rotrot = 360 - rotation
            # print(pairs)
            pose.pose.position.x = x
            pose.pose.position.y = y
            # Convert Z rotation to quaternion
            pose.pose.orientation.z = math.sin(math.radians(rotrot) / 2)
            pose.pose.orientation.w = math.cos(math.radians(rotrot) / 2)
            poses.append(deepcopy(pose))
            # print(pose)
            
        nav_start = navigator.get_clock().now()
        navigator.followWaypoints(poses)
        # Do something during our route (e.x. AI detection on camera images for anomalies)
        # Simply print number of waypoint for the demonstation
        i = 0
        while not navigator.isTaskComplete():
            i += 1
            feedback = navigator.getFeedback()
            if feedback and i % 5 == 0:
                print('Executing current waypoint: : {0}/{1: <5}'.format(
                    str(feedback.current_waypoint + 1), str(len(poses))), end='\r')

        # my_file.close()
        exit(0)

if __name__ == '__main__':
    main()
