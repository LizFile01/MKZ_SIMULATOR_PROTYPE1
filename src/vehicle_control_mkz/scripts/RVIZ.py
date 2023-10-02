#!/usr/bin/env python3

from nav_msgs.msg import Path
import os
import numpy as np 
from std_msgs.msg import Header
from geometry_msgs.msg import TwistStamped, PoseStamped
import rclpy
from rclpy.node import Node
from lat_control import LatController
from dbw_ford_msgs.msg import SteeringCmd

from vehicle_control_mkz.msg import A9

class RVIZ_Plugin(Node):
    def __init__(self,rate=50):
        super().__init__('RVIZ')
        self.rate = rate
        self.timer = self.create_timer(1/self.rate, self.publish)
        #Global var for RVIZ path
        self.RVIZ_Path = Path()
        self.PoseStampedMsg = PoseStamped()
        #Publish msg 
        self.publisher_RVIZ1 = self.create_publisher(Path, '/vehicle/desired_rviz_path', 1)

        #Subscribe to lat_control to get path array: 
        self.pub_flag = 0
        self.Steercb = self.create_subscription(SteeringCmd,'/vehicle/steering_cmd',self.steer_cb,1)



    def steer_cb(self,msg):
        #calling path array once feedback is heard from latcontrol
        LC = LatController()
        self.path_array = LC.RVIZ_Path()
        #Get desired RVIZ path 
        self.Waypoint_plotter_rviz()

    
    def Waypoint_plotter_rviz(self):
            for i in range(len(self.path_array) - 1):
                self.header = Header()
                self.RVIZ_Path.header.frame_id = "world"
                self.PoseStampedMsg.pose.position.x = float(self.path_array[i][0])
                self.PoseStampedMsg.pose.position.y = float(self.path_array[i][1])
                self.PoseStampedMsg.header.frame_id = "world"
                self.RVIZ_Path.poses.append(self.PoseStampedMsg)
            self.pub_flag = 1 

          
    def publish(self):
        if self.pub_flag == 1:
            self.publisher_RVIZ1.publish(self.RVIZ_Path)

def main(args=None):
    rclpy.init(args=args)
    rviz = RVIZ_Plugin()
    rclpy.spin(rviz)
    rviz.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
