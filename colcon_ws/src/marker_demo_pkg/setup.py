from setuptools import setup

package_name = 'marker_demo_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/show_marker.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='user',
    maintainer_email='user@example.com',
    description='Minimal ROS 2 Jazzy package demonstrating visualization_msgs/Marker and MarkerArray in RViz.',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [
            'simple_marker_pub = marker_demo_pkg.simple_marker_pub:main',
            'array_marker_pub = marker_demo_pkg.array_marker_pub:main',
        ],
    },
)
