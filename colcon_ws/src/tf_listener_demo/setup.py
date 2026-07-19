from setuptools import setup

package_name = 'tf_listener_demo'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/tf_listener_demo']),
        ('share/tf_listener_demo', ['package.xml']),
        ('share/tf_listener_demo/launch', ['launch/tf_listener.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    entry_points={
        'console_scripts': [
            'tf_listener_node = tf_listener_demo.tf_listener_node:main',
        ],
    },
)
