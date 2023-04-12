# MKZ_SIMULATOR_PROTYPE1
Demo for MKZ ROS2 communication as of 4/5/23, Translation of MKZ waypoint controller from https://github.com/Kchour/MKZ_controller/tree/controllers/vehicle_controllers

INSTRUCTIONS FOR RUNNING: 
1) source ws
2) source Gazebo (. /usr/share/gazebo-11/setup.bash)
3) run odompubtest script (ros2 run vehicle_control_mkz odompubtest_mkz.py)
4) In another terminal, run Gazebo sim (ros2 launch dbw_gazebo_mkz Gazebo_mkz_initialize_launch.xml)
5) Run controllers>
- To test waypoint generation, run ros2 launch vehicle_control_mkz controllaunch.xml IS_CP:=TRUE and set file to /odom_waypoints.dat (in launch file)
- To run controller, run ros2 launch vehicle_control_mkz controllaunch.xml IS_CP:= FALSE DESIRED_SPEED:=(float desired simulation speed in m/s)

TODO: 
-Verify lat/long controllers are functioning correctly**
-Test with Joystick/keyboard
