import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, LogInfo
from launch.launch_description_sources import PythonLaunchDescriptionSource, FrontendLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument('camera_value', default_value='0', description='Camera value'),
        DeclareLaunchArgument('use_vision', default_value='False', description='Use vision'),
        DeclareLaunchArgument('model', default_value='mkz', description='Vehicle model'),

        IncludeLaunchDescription(
            FrontendLaunchDescriptionSource(
                os.path.join(get_package_share_directory('dataspeed_dbw_gazebo'),
                    'launch', 'dataspeed_dbw_gazebo.launch.xml')),
            launch_arguments={
                'use_camera_control': 'true',
                'world_name': '$(find-pkg-share dbw_gazebo_mkz)/worlds/test_track.world',
                'sim_param_file': '$(find-pkg-share dbw_gazebo_mkz)/yaml/single_vehicle_test_track.yaml',
                'headless': 'false',
                'pause': 'false'
            }.items()
        ),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(get_package_share_directory('dbw_gazebo_mkz'),
                        'launch', 'generic_dbw.launch.py')),
            launch_arguments={
                'vehicle_name': 'vehicle',
                'vehicle_type': LaunchConfiguration('model')
            }.items()
        ),

        Node(
            package='vehicle_control_mkz',
            executable='gazebo_twister',
            name='vehicle_initialize'
        )
    ])
