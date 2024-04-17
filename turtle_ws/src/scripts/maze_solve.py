#!/usr/bin/env python3
import rclpy #run ros through python
from nav2_simple_commander.robot_navigator import BasicNavigator #for navigation throgh the simple commander api
from geometry_msgs.msg import PoseStamped #for setting pose
import tf_transformations #for transforming euler to quaternion


def create_pose(navigator: BasicNavigator,position_x,position_y,orientation_z):

    q_x, q_y, q_z, q_w = tf_transformations.quaternion_from_euler(0.0, 0.0, orientation_z)

    created_pose = PoseStamped()

    created_pose.header.frame_id = 'map'
    created_pose.header.stamp = navigator.get_clock().now().to_msg()
    
    created_pose.pose.position.x = position_x
    created_pose.pose.position.y = position_y
    created_pose.pose.position.z = 0.0
    created_pose.pose.orientation.x = q_x
    created_pose.pose.orientation.y = q_y
    created_pose.pose.orientation.z = q_z
    created_pose.pose.orientation.w = q_w

    return created_pose


def main():

    rclpy.init()
    nav = BasicNavigator()

    initial_pose=create_pose(nav,0.0,-3.0,0.0)
    nav.setInitialPose(initial_pose)


    nav.waitUntilNav2Active()

    goal_pose1=create_pose(nav,-3.0,-2.0,1.57)
   

    nav.goToPose(goal_pose1)

    

    while not nav.isTaskComplete():
        feedback=nav.getFeedback()

    print(nav.getResult())


    rclpy.shutdown()


def second():
    rclpy.init()
    nav = BasicNavigator()

    


    nav.waitUntilNav2Active()

    
    goal_pose2=create_pose(nav,0.0,0.0,1.57)
    
    nav.goToPose(goal_pose2)

    

    while not nav.isTaskComplete():
        feedback=nav.getFeedback()

    print(nav.getResult())


    rclpy.shutdown()


def third():
    rclpy.init()
    nav = BasicNavigator()

    


    nav.waitUntilNav2Active()


    goal_pose3=create_pose(nav,3.0,3.0,-1.57)

    nav.goToPose(goal_pose3)

    

    while not nav.isTaskComplete():
        feedback=nav.getFeedback()

    print(nav.getResult())


    rclpy.shutdown()

def fourth():
    rclpy.init()
    nav = BasicNavigator()

    


    nav.waitUntilNav2Active()


    goal_pose4=create_pose(nav,1.5,1.0,-1.57)

    nav.goToPose(goal_pose4)

    

    while not nav.isTaskComplete():
        feedback=nav.getFeedback()

    print(nav.getResult())


    rclpy.shutdown()

def fifth():
    rclpy.init()
    nav = BasicNavigator()

    


    nav.waitUntilNav2Active()


    goal_pose5=create_pose(nav,3.0,0.0,-1.57)

    nav.goToPose(goal_pose5)

    

    while not nav.isTaskComplete():
        feedback=nav.getFeedback()

    print(nav.getResult())


    rclpy.shutdown()

def sixth():
    rclpy.init()
    nav = BasicNavigator()

    


    nav.waitUntilNav2Active()


    goal_pose6=create_pose(nav,1.5,-2.0,-1.57)

    nav.goToPose(goal_pose6)

    

    while not nav.isTaskComplete():
        feedback=nav.getFeedback()

    print(nav.getResult())


    rclpy.shutdown()

def seventh():
    rclpy.init()
    nav = BasicNavigator()

    


    nav.waitUntilNav2Active()


    goal_pose7=create_pose(nav,3.0,-3.0,3.14)

    nav.goToPose(goal_pose7)

    

    while not nav.isTaskComplete():
        feedback=nav.getFeedback()

    print(nav.getResult())


    rclpy.shutdown()

if __name__ == '__main__':
    main()
    second()
    third()
    fourth()
    fifth()
    sixth()
    seventh()
