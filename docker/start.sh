#!/bin/bash

source ./common.sh

xhost +SI:localuser:root

docker run \
  -itd \
  --net=host \
  --env DISPLAY=$DISPLAY \
  --env WAYLAND_DISPLAY=$WAYLAND_DISPLAY \
  --env XDG_RUNTIME_DIR=$XDG_RUNTIME_DIR \
  --env QT_X11_NO_MITSHM=1 \
  --volume /tmp/.X11-unix:/tmp/.X11-unix \
  --volume ${PARENT_DIR}:/workspace \
  --gpus all \
  --name $CONTAINER_NAME \
  --shm-size=8G \
  $IMAGE_NAME