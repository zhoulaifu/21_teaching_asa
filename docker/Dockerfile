FROM ubuntu:18.04
ARG DEBIAN_FRONTEND=noninteractive
\
RUN apt-get update \
         && apt-get install -y  lcov afl++ emacs 


ENV MOUNT /mnt/local
RUN mkdir -p $MOUNT
WORKDIR $MOUNT
