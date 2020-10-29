#!/usr/bin/env python

import rospy
# for visualization 
from nav_msgs.msg import Path
from geometry_msgs.msg import PoseWithCovarianceStamped, PoseStamped


class Path_PubSub():
    def __init__(self):
        rospy.init_node("path_pubsub")
        #Creating a path object. 
        self.path_ = Path()
        self.path_sub_ = rospy.Subscriber("amcl_pose",PoseWithCovarianceStamped,self.path_cb)
        # self.path_sub_ = rospy.Subscriber("/map/robot_pose",PoseWithCovarianceStamped,self.path_cb)
        self.path_pub_ = rospy.Publisher('path',Path,queue_size=5)

    def path_cb(self,msg):
        path_pose = PoseStamped()
        path_pose.header = msg.header
        path_pose.pose = msg.pose.pose
        self.path_.header = msg.header
        self.path_.poses.append(path_pose)
        self.path_pub_.publish(self.path_)
        

if __name__ == '__main__':
    try:
        Path_PubSub()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass

        

# def path_publisher():
#     pub = rospy.Publisher('chatter', String, queue_size=10)
#     rospy.init_node('talker', anonymous=True)
#     rate = rospy.Rate(10) # 10hz
#     while not rospy.is_shutdown():
#         hello_str = "hello world %s" % rospy.get_time()
#         rospy.loginfo(hello_str)
#         pub.publish(hello_str)
#         rate.sleep()

