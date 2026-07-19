# marker_demo_pkg (ROS 2 Jazzy)

Minimal demo for **visualization_msgs/Marker** and **MarkerArray**.
- `/visualization_marker`: red sphere (1 Hz)
- `/visualization_marker_array`: LINE_STRIP path + TEXT label (2 Hz)

## Build & Run

```bash
mkdir -p ~/marker_demo_ws/src
cd ~/marker_demo_ws/src
# unzip this package here so that ./src/marker_demo_pkg exists
cd ~/marker_demo_ws
colcon build --symlink_install
# (typo fixed below)
```
```bash
colcon build --symlink-install
source install/setup.bash

# Start publishers
ros2 launch marker_demo_pkg show_marker.launch.py

# RViz (recommended config)
rviz2 -d ~/marker_demo_ws/install/marker_demo_pkg/share/marker_demo_pkg/rviz/marker_view.rviz
```

## Notes
- Fixed Frame is set to `base_link` in RViz.
- Ensure **color.a > 0** (alpha) to make markers visible.
- Set `lifetime=0` for persistent markers.
