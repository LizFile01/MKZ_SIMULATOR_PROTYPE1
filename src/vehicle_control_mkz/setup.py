import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'vehicle_control_mkz'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*launch.[pxy][yma]*')),
        (os.path.join('share', package_name), glob('config/*'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='user',
    maintainer_email='user@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'collect_waypoints = vehicle_control_mkz.collect_waypoints:main',
            'follow_waypoints = vehicle_control_mkz.follow_waypoints:main',
            'gazebo_twister = vehicle_control_mkz.gazebo_twister:main',
            'lat_control = vehicle_control_mkz.lat_control:main',
            'long_control = vehicle_control_mkz.long_control:main',
            'odompubtest = vehicle_control_mkz.odompubtest:main',
            'ros_callback = vehicle_control_mkz.ros_callback:main',
        ],
    },
)
