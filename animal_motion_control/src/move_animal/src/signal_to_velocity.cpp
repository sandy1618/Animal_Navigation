#include <ros/ros.h>
#include <light_signal_msg/light_signal.h>
#include <geometry_msgs/Twist.h>

light_signal_msg::light_signal cmd_sig;
geometry_msgs::Twist cmd_vel {};
ros::Publisher cmd_pub_ ;

void convertCallback(const light_signal_msg::light_signal& cmd_sig){
     if(cmd_sig.left){
         cmd_vel.angular.z = 0.1;
         cmd_vel.linear.x = 0;

    }
     if(cmd_sig.right){
         cmd_vel.angular.z = -0.1;
         cmd_vel.linear.x = 0;

    }
     if(cmd_sig.forward){
          cmd_vel.angular.z = 0;
         cmd_vel.linear.x = 0.1;

    }
     if(cmd_sig.stop){
         cmd_vel.angular.z = 0;
         cmd_vel.linear.x = 0;

    }
    if(cmd_sig.sound){

    }

    cmd_pub_.publish(cmd_vel);

}
void initialize(geometry_msgs::Twist& cmd_vel){
    cmd_vel.linear.x = 0;
    cmd_vel.angular.z = 0;
}
int main(int argc,char** argv ){

    ros::init(argc,argv, "signal_to_velocty");

    // Initialize command signals
    initialize(cmd_vel);

    ros::NodeHandle n;
    ros::Subscriber sig_sub_ = n.subscribe("cmd_sig",1,convertCallback);

    cmd_pub_ = n.advertise<geometry_msgs::Twist>("cmd_vel",1);
    

    // cmd_pub_.publish(cmd_vel);
    
    ros::spin();


    return 0;
    
}