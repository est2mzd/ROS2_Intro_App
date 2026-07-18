#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

#include "geometry_msgs/msg/twist.hpp"

#include "turtlesim/msg/pose.hpp"
#include <cmath>
#include <optional>

//---------------------------------------------------------------

class MinimalPublisher: public rclcpp::Node
{
private:
    rclcpp::Publisher<std_msgs::msg::String>::SharedPtr publisher_;
    rclcpp::TimerBase::SharedPtr timer_;
    int count_;

    void timer_callback()
    {
        auto message = std_msgs::msg::String();
        message.data = "Hello " + std::to_string(count_++);
        publisher_->publish(message);
        RCLCPP_INFO(this->get_logger(), "Pusblishing:'%s'", message.data.c_str());
    }

public:
    MinimalPublisher():Node("minimal_publisher"), count_(0)
    {
        publisher_ = this->create_publisher<std_msgs::msg::String>("chatter", 10);
        timer_ = this->create_wall_timer(
            std::chrono::seconds(1),
            std::bind(&MinimalPublisher::timer_callback, this)
        );
    }
};

//---------------------------------------------------------------

class TurtleController:public rclcpp::Node
{
private:
    rclcpp::Publisher<geometry_msgs::msg::Twist>::SharedPtr publisher_;
    rclcpp::TimerBase::SharedPtr timer_;

    void timer_callback()
    {
        auto msg = geometry_msgs::msg::Twist();
        msg.linear.x = 2.0;
        msg.angular.z = 1.0;
        publisher_->publish(msg);
        RCLCPP_INFO(this->get_logger(), "Pusblished: linear=%.1f, angular=%.1f", 
                    msg.linear.x, msg.angular.z);
    }

public:
    TurtleController():Node("tutle_controller")
    {
        publisher_ = this->create_publisher<geometry_msgs::msg::Twist>("/turtle1/cmd_vel", 10);
        timer_ = this->create_wall_timer(
            std::chrono::seconds(1),
            std::bind(&TurtleController::timer_callback, this)
        );
    }
};

//---------------------------------------------------------------

class SpiralPublisher: public rclcpp::Node
{
private:
    rclcpp::Publisher<geometry_msgs::msg::Twist>::SharedPtr publisher_;
    rclcpp::TimerBase::SharedPtr timer_;
    int count = 0;

    void timer_callback()
    {
        auto msg = geometry_msgs::msg::Twist();
        msg.linear.x = 2.0 + count * 0.05;
        msg.angular.z = 1.0;
        publisher_->publish(msg);
        RCLCPP_INFO(this->get_logger(), "Pusblished: linear=%.1f, angular=%.1f", 
                    msg.linear.x, msg.angular.z);

        count += 1;
    }

public:
    SpiralPublisher():Node("spiral_controller")
    {
        publisher_ = this->create_publisher<geometry_msgs::msg::Twist>("/turtle1/cmd_vel", 10);
        timer_ = this->create_wall_timer(
            std::chrono::seconds(1),
            std::bind(&SpiralPublisher::timer_callback, this)
        );
    }
};

//---------------------------------------------------------------

class EightFigureController: public rclcpp::Node
{
private:
    rclcpp::Publisher<geometry_msgs::msg::Twist>::SharedPtr publisher_;
    rclcpp::Subscription<turtlesim::msg::Pose>::SharedPtr subscriber_;
    rclcpp::TimerBase::SharedPtr timer_;
    int count = 0;
    float linear_speed = 1.0;
    float angular_speed = 2.0;
    float current_angular_z = angular_speed;
    std::optional<float> last_theta;
    float cumulative_angle = 0.0;

    void timer_callback()
    {
        auto msg = geometry_msgs::msg::Twist();
        msg.linear.x = linear_speed;
        msg.angular.z = current_angular_z;
        publisher_->publish(msg);
        RCLCPP_INFO(this->get_logger(), "Pusblished: linear=%.1f, angular=%.1f", 
                    msg.linear.x, msg.angular.z);

        count += 1;
    }

    void pose_callback(const turtlesim::msg::Pose::SharedPtr msg)
    {
        float theta = msg->theta;

        if (last_theta)
        {
            float delta = theta - *last_theta;
            delta = std::fmod(delta + M_PI, 2 * M_PI);
            if (delta < 0.0)
            {
                delta += 2 * M_PI;
            }
            delta -= M_PI;

            cumulative_angle += delta;

            if (std::fabs(cumulative_angle) > 2 * M_PI)
            {
                current_angular_z *= -1.0;
                cumulative_angle = 0.0;
                RCLCPP_INFO(this->get_logger(), "--> Change Direction !!");
            }
        }

        last_theta = theta;
    }

public:
    EightFigureController():Node("eight_figure_controller")
    {
        publisher_ = this->create_publisher<geometry_msgs::msg::Twist>("/turtle1/cmd_vel", 10);
        subscriber_ = this->create_subscription<turtlesim::msg::Pose>("turtle1/pose", 10,
            std::bind(&EightFigureController::pose_callback, this, std::placeholders::_1));
        timer_ = this->create_wall_timer(
            std::chrono::milliseconds(100),
            std::bind(&EightFigureController::timer_callback, this)
        );
    }
};



int main(int argc, char* argv[])
{
    int test_type = 4;
    rclcpp::init(argc, argv);

    if (test_type == 1)
    {
        rclcpp::spin(std::make_shared<MinimalPublisher>());
    }
    else if (test_type == 2)
    {
        rclcpp::spin(std::make_shared<TurtleController>());
    }
    else if (test_type == 3)
    {
        rclcpp::spin(std::make_shared<SpiralPublisher>());
    }    
    else if (test_type == 4)
    {
        rclcpp::spin(std::make_shared<EightFigureController>());
    }       
    else
    {
        rclcpp::spin(std::make_shared<MinimalPublisher>());
    }
        
    rclcpp::shutdown();
    return 0;
}