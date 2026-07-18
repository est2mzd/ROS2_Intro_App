from setuptools import setup

package_name = 'launch_basic'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name + '/launch', ['launch/sample_launch.py',  # launchファイルの登録
                                               'launch/multi_launch.py',
                                               'launch/param_launch.py',
                                               'launch/conditional_launch.py',
                                               'launch/sim_launch.py',
                                               'launch/teleop_launch.py',
                                               'launch/main_launch.py',
                                               'launch/namespace_launch.py',
    	                                       'launch/remap_launch.py']), 
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='user',
    maintainer_email='user@example.com',
    description='Launch basic package using ament_python',
    license='Apache-2.0',
)
