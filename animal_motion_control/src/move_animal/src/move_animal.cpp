#include <iostream>
#include <move_animal/move_animal.h>

ros::Publisher pub_sig_;

void printCallback(const nav_msgs::OccupancyGrid::ConstPtr &msg)
{
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
void printCallback2(const nav_msgs::OccupancyGrid &msg)
{
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

void getGoalPos(const geometry_msgs::PoseStamped &msg)
{
    auto frame_id_ = msg.header.frame_id;
    auto pose_ = msg.pose;
    goal.x = pose_.position.x; // here next is the goal, but later
    goal.y = pose_.position.y;

    next = goal; // for first algorithm, goal is same as next position.
    ROS_INFO_STREAM("Goal : "
                    << "Position x,y :"
                    << " " << goal.x << " , " << goal.y);
    pub_sig_.publish(cmd_sig);
}

void getRobotPoseAMCL(const geometry_msgs::PoseWithCovarianceStamped &msg)
{
    // ROS_INFO_STREAM("Seq: " << msg.header.seq);
    auto frame_id_ = msg.header.frame_id;
    auto pose_ = msg.pose.pose;
    now.x = pose_.position.x;
    now.y = pose_.position.y;
    now.az = tf2::getYaw(pose_.orientation);

    //tf2:;getYaw(pose.orientation)
    ROS_INFO_STREAM("Robot"
                    << "Position x,y :"
                    << " " << now.x << " , " << now.y);
    ROS_INFO_STREAM("Robot"
                    << "Yaw Angle :"
                    << " " << now.az * R2D);

    setNowError();

    computeSignalCommands();
}

void setNowError()
{
    nError.x = (next.x - now.x);
    nError.y = (next.y - now.y);
    // if these two variables are null, the tangent doesn't exist
    // plus, the angle error is irrelevant because we have arrived at our destination

    // if these two variables are null, the tangent doesn't exist
    // plus, the angle error is irrelevant because we have arrived at our destination

    if (nError.y == 0 & nError.x == 0)
    {
        ref_angle = now.az;
    }
    else
    {
        ref_angle = std::atan2(nError.y, nError.x);
    }

    distance = std::sqrt(nError.x * nError.x + nError.y * nError.y);
    nError.az = ref_angle - now.az;
    // make sure that we chose the smallest angle, so that the robot takes the shortest turn
    if (nError.az > 180 * D2R)
    {
        nError.az -= 360 * D2R;
    }
    if (nError.az < -180 * D2R)
    {
        nError.az += 360 * D2R;
    }
    ROS_INFO_STREAM("Euclidean Distance" << distance);
    ROS_INFO_STREAM("Goal Angle" << ref_angle * R2D);
    ROS_INFO_STREAM("Current Angle" << now.az * R2D);
    ROS_INFO_STREAM("Angle difference Angle" << nError.az * R2D);
}

void computeSignalCommands()
{
    if (distance < 0.05)
    {
        ROS_INFO("goal_reached");
        setZeroSignal();
    }
    else
    {
        if (fabs(nError.az) > 10 * D2R)
        {

            setRot();
        }
        else
        {

            setVel();
        }
    }

    pub_sig_.publish(cmd_sig);
}

void setZeroSignal()
{
    cmd_sig.left = 0;
    cmd_sig.right = 0;
    cmd_sig.forward = 0;
    cmd_sig.stop = 0;
    cmd_sig.sound = 0;
}

void setRot()
{

    if (nError.az > 0)
    { // IF DIFFE IS +VE, move left.
        cmd_sig.left = 1;
        cmd_sig.right = 0;
        cmd_sig.forward = 0;
        cmd_sig.stop = 0;
        cmd_sig.sound = 0;
    }
    else
    {
        cmd_sig.left = 0;
        cmd_sig.right = 1;
        cmd_sig.forward = 0;
        cmd_sig.stop = 0;
        cmd_sig.sound = 0;
    }
}

void setVel()
{
    cmd_sig.left = 0;
    cmd_sig.right = 0;
    cmd_sig.forward = 1;
    cmd_sig.stop = 0;
    cmd_sig.sound = 0;
}

void initialize(light_signal_msg::light_signal &cmd_sig)
{
    cmd_sig.left = 0;
    cmd_sig.right = 0;
    cmd_sig.forward = 0;
    cmd_sig.stop = 0;
    cmd_sig.sound = 0;
}
int main(int argc, char **argv)
{

    ros::init(argc, argv, "move_animal");

    // ros::NodeHandle n;

    // ros::Subscriber occupancy_grid_ = n.subscribe("map",10,printCallback2);

    // Initialize command signals
    initialize(cmd_sig);

    // separate node handle for having the namespace scope move_base_simple
    ros::NodeHandle simple_nh("move_base_simple");
    ros::Subscriber goal_sub_ = simple_nh.subscribe("goal", 1, getGoalPos);

    // Robot's Position and Orientation estimations.
    // subscribe to topics (to get odometry information, we need to get a handle to the topic in the global namespace)
    ros::NodeHandle gn;
    ros::Subscriber amcl_sub_ = gn.subscribe("amcl_pose", 1, getRobotPoseAMCL);

    // Publishing signal commands
    ros::NodeHandle pub;
    pub_sig_ = pub.advertise<light_signal_msg::light_signal>("cmd_sig", 1);

    // ros::rate(10);
    pub_sig_.publish(cmd_sig);

    ros::spin();

    return 0;
}
