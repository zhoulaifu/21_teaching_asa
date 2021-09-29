FROM ros:foxy
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
         && apt-get install -y  lcov afl++ emacs flex

#ros work dir
ENV ROS_WS /opt/ros_ws
ENV TEEX /opt/teex
#WORKDIR $ROS_WS
RUN mkdir -p $ROS_WS
RUN mkdir -p $TEEX


RUN cd $ROS_WS \
        &&  git clone -b $ROS_DISTRO --depth 1 https://github.com/ros2/geometry2 $ROS_WS/src/geometry2 \
        &&. /opt/ros/${ROS_DISTRO}/setup.sh \
#        && VERBOSE=1 CXX="afl-g++" CXXFLAGS="--coverage -g -fsanitize=address,undefined -fsanitize-undefined-trap-on-error" c#olcon build --event-handlers console_direct+