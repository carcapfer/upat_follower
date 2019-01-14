#include "path_follower/path_generator.h"
#include <ros/ros.h>

#include <gtest/gtest.h>
#include <thread>

// terminal: catkin build --verbose --catkin-make-args run_tests | sed -n '/\[==========\]/,/\[==========\]/p'

class MyTestSuite : public ::testing::Test {
   public:
    MyTestSuite() {
    }
    ~MyTestSuite() {}
};

TEST_F(MyTestSuite, interp1) {
    PathGenerator generator;
    std::vector<double> list_pose_x, list_pose_y, list_pose_z;
    list_pose_x = {5.0, 5.0, 5.0, 5.0, 10.0, 10.0, 10.0, 15.0, 15.0, 15.0, 20.0, 20.0, 20.0};
    list_pose_y = {5.0, 10.0, 10.0, 5.0, 5.0, 5.0, 10.0, 10.0, 10.0, 5.0, 5.0, 5.0, 10.0};
    list_pose_z = {10.01, 10.0, 5.0, 5.0, 5.0, 10.0, 10.0, 10.0, 5.0, 5.0, 5.0, 10.0, 10.0};
    int interp1_final_size = 1000;
    nav_msgs::Path path_interp1 = generator.createPathInterp1(list_pose_x, list_pose_y, list_pose_z, list_pose_x.size(), interp1_final_size);
    EXPECT_EQ(path_interp1.poses.size(), interp1_final_size);
}

int main(int argc, char** argv) {
    ros::init(argc, argv, "TestNode");
    ros::NodeHandle nh;

    testing::InitGoogleTest(&argc, argv);

    std::thread t([] {while(ros::ok()) ros::spin(); });

    auto res = RUN_ALL_TESTS();

    ros::shutdown();

    return res;
}