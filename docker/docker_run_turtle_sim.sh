# コンテナ内の root が X11 にアクセスできるようにする
xhost +SI:localuser:root

docker run -it --rm --net=host \
  --env DISPLAY=$DISPLAY \
  --env WAYLAND_DISPLAY=$WAYLAND_DISPLAY \
  --env XDG_RUNTIME_DIR=$XDG_RUNTIME_DIR \
  --env QT_X11_NO_MITSHM=1 \
  --volume /tmp/.X11-unix:/tmp/.X11-unix \
  --gpus all \
  --name turtle_sim \
  osrf/ros:jazzy-desktop

# コンテナ内の root が X11 にアクセスできないようにする
# xhost -SI:localuser:root  