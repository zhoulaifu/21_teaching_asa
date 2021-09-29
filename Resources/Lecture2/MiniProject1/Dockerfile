FROM ros:foxy
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
         && apt-get install -y  lcov afl++ emacs flex tree

#ros work dir
ENV ROS_WS /opt/ros_ws
RUN mkdir -p $ROS_WS



RUN cd $ROS_WS \
        &&  git clone -b $ROS_DISTRO --depth 1 https://github.com/ros2/geometry2 $ROS_WS/src/geometry2 \
        &&. /opt/ros/${ROS_DISTRO}/setup.sh \

WORKDIR $ROS_WS