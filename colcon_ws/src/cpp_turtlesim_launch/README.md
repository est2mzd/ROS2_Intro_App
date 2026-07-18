# cpp_turtlesim_launch

C++ パッケージ構成（ament_cmake）で作成された、  
`turtlesim_node` を launch から起動するだけの最小サンプルです。

## ビルド方法

```
cd /root/colcon_ws/src
# このフォルダを配置

cd /root/colcon_ws
colcon build --packages-select cpp_turtlesim_launch
source install/setup.bash
```

## 実行方法

```
ros2 launch cpp_turtlesim_launch turtlesim_cpp_launch.py
```

turtlesim のウィンドウが起動します。
