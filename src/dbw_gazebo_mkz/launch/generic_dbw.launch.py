from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, LogInfo
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch.conditions import IfCondition

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument('vehicle_name', default_value='vehicle', description='Vehicle name'),
        DeclareLaunchArgument('vehicle_type', default_value='mkz', description='Vehicle type'),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(['$(find-pkg-share dbw_ford_can)/launch/dbw.launch.py']),
            condition=IfCondition("$(var vehicle_type)=='mkz' or $(var vehicle_type)=='fusion' or $(var vehicle_type)=='mondeo'"),
            launch_arguments={
                'live': 'false',
                'load_urdf': 'false',
                'can_ns': 'can_bus_dbw',
                'vehicle_ns': LaunchConfiguration('vehicle_name'),
                'ackermann_wheelbase': '2.85',
                'steering_ratio': '14.8'
            }.items()
        ),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(['$(find-pkg-share dbw_ford_can)/launch/dbw.launch.py']),
            condition=IfCondition("$(var vehicle_type)=='f150'"),
            launch_arguments={
                'live': 'false',
                'load_urdf': 'false',
                'can_ns': 'can_bus_dbw',
                'vehicle_ns': LaunchConfiguration('vehicle_name'),
                'ackermann_wheelbase': '3.67',
                'steering_ratio': '18.0'
            }.items()
        ),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(['$(find-pkg-share dbw_fca_can)/launch/dbw.launch.py']),
            condition=IfCondition("$(var vehicle_type)=='jeep'"),
            launch_arguments={
                'live': 'false',
                'load_urdf': 'false',
                'can_ns': 'can_bus_dbw',
                'vehicle_ns': LaunchConfiguration('vehicle_name'),
                'ackermann_wheelbase': '2.91',
                'steering_ratio': '15.15'
            }.items()
        ),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(['$(find-pkg-share dbw_fca_can)/launch/dbw.launch.py']),
            condition=IfCondition("$(var vehicle_type)=='pacifica'"),
            launch_arguments={
                'live': 'false',
                'load_urdf': 'false',
                'can_ns': 'can_bus_dbw',
                'vehicle_ns': LaunchConfiguration('vehicle_name'),
                'ackermann_wheelbase': '3.08',
                'steering_ratio': '16.2'
            }.items()
        )
    ])
