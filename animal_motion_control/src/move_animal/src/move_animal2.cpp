#include <iostream>
#include <move_animal/move_animal2.h>


void printCallback(const nav_msgs::OccupancyGrid::ConstPtr& msg){
  std_msgs::Header header = msg->header;
  nav_msgs::MapMetaData info = msg->info;
  auto data = msg->data;
  ROS_INFO("Got map %d %d", info.width, info.height);
//    for (unsigned int x = 0; x < info.width; x++)
//     for (unsigned int y = 0; y < info.height; y++)
//       if (data(x,y) == -1)
//         Ngray++;
//         ROS_INFO("Number of gray cells is: %e", Ngray);publish(*newGrid);
}
void printCallback2(const nav_msgs::OccupancyGrid& msg){
  auto header = msg.header;
  auto info = msg.info;
  auto data = msg.data;
  ROS_INFO("Got map %d %d", info.width, info.height);
//   ROS_INFO(data);
//    for (unsigned int x = 0; x < info.width; x++)
//     for (unsigned int y = 0; y < info.height; y++)
//       if (data(x,y) == -1)
//         Ngray++;
//         ROS_INFO("Number of gray cells is: %e", Ngray);publish(*newGrid);
}

void MoveAnimal::getGoalPos (const geometry_msgs::PoseStamped::ConstPtr& msg) {
    // auto frame_id_ = msg->header.frame_id;
    // auto pose_ = msg->pose;
    // this->goal.x = pose_.position.x; // here next is the goal, but later 
    // this->goal.y = pose_.position.y;
    ROS_INFO("getGoalPos called.");
    // ROS_INFO_STREAM(frame_id_);
    // ROS_INFO_STREAM("Goal : "<< "Position x,y :" << " " << this->goal.x << " , " << this->goal.y );
    
}

void MoveAnimal::getRobotPoseAMCL(const geometry_msgs::PoseWithCovarianceStamped::ConstPtr& msg)
{
    // ROS_INFO_STREAM("Seq: " << msg.header.seq);
    // auto frame_id_ = msg->header.frame_id;
    // auto pose_ = msg.pose.pose;
    // this->now.x = pose_.position.x ;
    // this->now.y = pose_.position.y ;
    // this->now.az = tf2::getYaw(pose_.orientation);
    ROS_INFO("getRobotPose called.");
    //tf2:;getYaw(pose.orientation)
    // ROS_INFO_STREAM(frame_id_);
    // ROS_INFO_STREAM("Robot"<< "Position x,y :" << " " <<this->now.x << " , " << this->now.y );
    // ROS_INFO_STREAM("Robot"<< "Yaw Angle :" << " " << now.az*R2D );
   

}
// local fucntions 
void goalPosCallback(const geometry_msgs::PoseStamped& msg){
    
}


MoveAnimal::MoveAnimal(): 
    now(NULL),
    next(NULL),
    nError(NULL),
    goal(NULL),
    distance(NULL),
    ref_angle(NULL),
    cmd_sig(NULL) {

    // ros::NodeHandle n;
    ROS_INFO("Started MoveAnimal Constructor");
    // ros::Subscriber occupancy_grid_ = n.subscribe("map",10,printCallback2);

  

    // separate node handle for having the namespace scope move_base_simple
    ros::NodeHandle simple_nh("move_base_simple");
    ros::Subscriber goal_sub_ = simple_nh.subscribe("goal", 1, &MoveAnimal::getGoalPos,this);
    if (goal_sub_)
    {
      ROS_INFO("Success Subscribed to goal");
    }

    // Robot's Position and Orientation estimations. 
    // subscribe to topics (to get odometry information, we need to get a handle to the topic in the global namespace)
    ros::NodeHandle gn;
    ros::Subscriber amcl_sub_ = gn.subscribe("amcl_pose", 100,&MoveAnimal::getRobotPoseAMCL,this);
     if (amcl_sub_)
    {
      ROS_INFO("Success Subscribed to amcl");
    }
    // Publishing signal commands 
    ros::NodeHandle pub;
    // ros::Publisher pub_sig_ = pub.advertise<light_signal_msg::light_signal>("cmd_sig",10);


}

MoveAnimal::~MoveAnimal(){};

int main(int argc, char** argv){
    ros::init(argc,argv, "move_animal");

    // creating move_animal object
    MoveAnimal move_human;

    ros::spin();

    return (0);

}


