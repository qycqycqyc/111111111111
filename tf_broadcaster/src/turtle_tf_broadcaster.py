#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''odom  ->  base_link '''
# import roslib
# roslib.load_manifest('tf_learn')
import rospy
import tf
# import turtlesim.msg
from nav_msgs.msg import Odometry
# def handle_turtle_pose(msg, turtlename):
#     br = tf.TransformBroadcaster()
#     br.sendTransform((msg.x, msg.y, 0),     #平移
#                       tf.transformations.quaternion_from_euler(0, 0, msg.theta),   #旋转（用四元数）
#                       rospy.Time.now(),   #rospy时间
#                       turtlename,         #子坐标系
#                       'world')            #父坐标系

def odom_tf_callback(Odometry):
    br = tf.TransformBroadcaster() #创建tf广播对象
    
    x_p = Odometry.pose.pose.position.x #位置
    y_p = Odometry.pose.pose.position.y
    z_p = Odometry.pose.pose.position.z


    x_o = Odometry.pose.pose.orientation.x #姿态
    y_o = Odometry.pose.pose.orientation.y
    z_o = Odometry.pose.pose.orientation.z
    w_o = Odometry.pose.pose.orientation.w
    br.sendTransform((x_p, y_p, 0),   #位移 
                     (x_o, y_o, z_o, w_o), #旋转(四元数)
                     rospy.Time.now(),
                     'base_link',  #子坐标系
                     'odom')      #父坐标系


if __name__ == '__main__':
    rospy.init_node('turtle_tf_broadcaster')
    rospy.Subscriber('/odom',Odometry, odom_tf_callback)
    # rospy.Subscriber('/odom_tdr',Odometry, odom_tf_callback)
    while not rospy.is_shutdown():
        br = tf.TransformBroadcaster()
        
    rospy.spin()
