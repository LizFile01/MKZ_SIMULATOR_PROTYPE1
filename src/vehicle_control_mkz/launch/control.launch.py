from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, GroupAction, LogInfo
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument('IS_CP', default_value='false', description='Collecting waypoints'),
        DeclareLaunchArgument('DESIRED_SPEED', default_value='3.0', description='Desired forward speed'),
        DeclareLaunchArgument('SIM', default_value='SIM', description='Real/sim'),
        DeclareLaunchArgument('WAYPOINTS_FILE', default_value='/odom_waypoints.dat', description='Waypoints file path'),

        GroupAction([
            Node(
                package='vehicle_control_mkz',
                executable='odompubtest_mkz.py',
                name='odom_publisher_node',
                parameters=[{'SIM': LaunchConfiguration('SIM')}]
            ),
            Node(
                package='vehicle_control_mkz',
                executable='follow_waypoints.py',
                name='waypoint_plot'
            ),
            Node(
                package='vehicle_control_mkz',
                executable='long_control.py',
                name='long_control_node',
                parameters=[{'DESIRED_SPEED': LaunchConfiguration('DESIRED_SPEED')}],
                output='screen'
            ),
            Node(
                package='vehicle_control_mkz',
                executable='lat_control.py',
                name='lat_control_node',
                parameters=[
                    {'DESIRED_SPEED': LaunchConfiguration('DESIRED_SPEED')},
                    {'WAYPOINTS_FILE': LaunchConfiguration('WAYPOINTS_FILE')}
                ],
                output='screen'
            )
        ], condition=LaunchConfiguration('IS_CP', '==', 'false')),

        GroupAction([
            Node(
                package='vehicle_control_mkz',
                executable='odompubtest_mkz.py',
                name='odom_publisher_node',
                parameters=[{'SIM': LaunchConfiguration('SIM')}]
            ),
            Node(
                package='vehicle_control_mkz',
                executable='collect_waypoints.py',
                name='waypoint_collection_node',
                parameters=[{'WAYPOINTS_FILE': LaunchConfiguration('WAYPOINTS_FILE')}],
                output='screen'
            )
        ], condition=LaunchConfiguration('IS_CP', '==', 'true'))
    ])
