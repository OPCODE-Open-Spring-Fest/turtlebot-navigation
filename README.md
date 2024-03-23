# TurtleBot Navigation
  A turtlebot which is a differential drive bot equipped with LiDAR, wheel encoders and imu to collect information of surrounding. This bot can be used to navigate autonomously through a given area once map is made of that world.

  In Gazebo different types of worlds can be made to navigate and simulate autonoumous navigation.

## Prerequisites:

- Ubuntu v22.04
  - Download here
    - [Ubuntu 22.04 LTS](https://ubuntu.com/download/desktop)
    - [ROS Humble](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html)
    - [Node js v18+](https://www.digitalocean.com/community/tutorials/how-to-install-node-js-on-ubuntu-20-04#option-3-installing-node-using-the-node-version-manager)

## Setup for local system

- Clone this repo in your system
  - `git clone https://github.com/OPCODE-Open-Spring-Fest/DevHub.git`
- Navigate to the project directory
  - `cd turtlebot-navigation/`
- Now install the node modules
  - `npm install`
- Navigate to ros workspace directory turtle_ws
    - `cd turtle_ws/`
- Now build the workspace using the following command
  - `colcon build`
  - Please check all the depencies written in "<depend>package_name</depend>" in package.xml file present in src->turtlebot3_fake_node, src->turtlebot3_gazebo and src->simulations. If anyone of them is not installed they can cause error while setup.


## Learning Resources

- Navigation Stack
  - [Nav2 Stack](https://navigation.ros.org/getting_started/index.html)
- Mapping
  - [SLAM](https://navigation.ros.org/tutorials/docs/navigation2_with_slam.html)
- Go to .github --> Contributor_Guide --> Project_Tour for more information in this project
- You can ask your doubts in the discord server OSF in the discuss-hub channel
  

