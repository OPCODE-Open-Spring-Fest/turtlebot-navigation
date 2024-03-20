# Project Tour

*  > Navigate to turtle_ws --> src, the src is the folder in which all the changes are to be done its file structure is defined.

### Project File Structure

```
src
├── turtlebot3_fake_node
│   ├── CHANGELOG.rst
│   ├── CMakeLists.txt
│   ├── include
│   │   └── turtlebot3_fake_node
│   │       └── turtlebot3_fake_node.hpp
│   ├── launch
│   │   ├── rviz2.launch.py
│   │   └── turtlebot3_fake_node.launch.py
│   ├── package.xml
│   ├── param
│   │   ├── burger.yaml
│   │   ├── waffle_pi.yaml
│   │   └── waffle.yaml
│   └── src
│       └── turtlebot3_fake_node.cpp
├── turtlebot3_gazebo
│   ├── CHANGELOG.rst
│   ├── CMakeLists.txt
│   ├── include
│   │   └── turtlebot3_gazebo
│   │       └── turtlebot3_drive.hpp
│   ├── launch
│   │   ├── empty_world.launch.py
│   │   ├── maze.launch.py
│   │   ├── robot_state_publisher.launch.py
│   │   ├── spawn_turtlebot3.launch.py
│   │   ├── turtlebot3_dqn_stage1.launch.py
│   │   ├── turtlebot3_dqn_stage2.launch.py
│   │   ├── turtlebot3_dqn_stage3.launch.py
│   │   ├── turtlebot3_dqn_stage4.launch.py
│   │   ├── turtlebot3_house.launch.py
│   │   └── turtlebot3_world.launch.py
│   ├── models
│   │   ├── turtlebot3_burger
│   │   │   ├── model-1_4.sdf
│   │   │   ├── model.config
│   │   │   └── model.sdf
│   │   ├── turtlebot3_common
│   │   │   ├── meshes
│   │   │   │   ├── burger_base.dae
│   │   │   │   ├── lds.dae
│   │   │   │   ├── r200.dae
│   │   │   │   ├── tire.dae
│   │   │   │   ├── waffle_base.dae
│   │   │   │   └── waffle_pi_base.dae
│   │   │   └── model.config
│   │   ├── turtlebot3_dqn_world
│   │   │   ├── goal_box
│   │   │   │   ├── model.config
│   │   │   │   └── model.sdf
│   │   │   ├── inner_walls
│   │   │   │   ├── model.config
│   │   │   │   └── model.sdf
│   │   │   ├── model.config
│   │   │   ├── model.sdf
│   │   │   ├── obstacle1
│   │   │   │   ├── model.config
│   │   │   │   └── model.sdf
│   │   │   ├── obstacle2
│   │   │   │   ├── model.config
│   │   │   │   └── model.sdf
│   │   │   ├── obstacle_plugin
│   │   │   │   ├── CMakeLists.txt
│   │   │   │   ├── obstacle1.cc
│   │   │   │   ├── obstacle2.cc
│   │   │   │   └── obstacles.cc
│   │   │   └── obstacles
│   │   │       ├── model.config
│   │   │       └── model.sdf
│   │   ├── turtlebot3_house
│   │   │   ├── model.config
│   │   │   └── model.sdf
│   │   ├── turtlebot3_waffle
│   │   │   ├── model-1_4.sdf
│   │   │   ├── model.config
│   │   │   └── model.sdf
│   │   ├── turtlebot3_waffle_pi
│   │   │   ├── model-1_4_.sdf
│   │   │   ├── model.config
│   │   │   └── model.sdf
│   │   └── turtlebot3_world
│   │       ├── meshes
│   │       │   ├── hexagon.dae
│   │       │   └── wall.dae
│   │       ├── model-1_4.sdf
│   │       ├── model.config
│   │       └── model.sdf
│   ├── package.xml
│   ├── rviz
│   │   └── tb3_gazebo.rviz
│   ├── src
│   │   └── turtlebot3_drive.cpp
│   ├── urdf
│   │   ├── common_properties.urdf
│   │   ├── turtlebot3_burger.urdf
│   │   ├── turtlebot3_waffle_pi.urdf
│   │   └── turtlebot3_waffle.urdf
│   └── worlds
│       ├── empty_world.world
│       ├── maze.world
│       ├── turtlebot3_dqn_stage1.world
│       ├── turtlebot3_dqn_stage2.world
│       ├── turtlebot3_dqn_stage3.world
│       ├── turtlebot3_dqn_stage4.world
│       ├── turtlebot3_house.world
│       └── turtlebot3_world.world
├── turtlebot3_simulations
│   ├── CHANGELOG.rst
│   ├── CMakeLists.txt
│   └── package.xml
└── turtlebot3_simulations_ci.repos
```

*  > Go through launch folder for a better understanding of turtlebot3_gazebo --> launch and worlds already available
```
├── empty_world.launch.py
├── maze.launch.py
├── robot_state_publisher.launch.py
├── spawn_turtlebot3.launch.py
├── turtlebot3_dqn_stage1.launch.py
├── turtlebot3_dqn_stage2.launch.py
├── turtlebot3_dqn_stage3.launch.py
├── turtlebot3_dqn_stage4.launch.py
├── turtlebot3_house.launch.py
└── turtlebot3_world.launch.py

```
*  > All the dependencies can be found in package.xml file present in each folder in src if you face any issue in setup please take a look at those
*  > Existing function:-Can Navigate through a maze world made using rViz.
*  
