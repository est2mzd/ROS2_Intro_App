from setuptools import setup

package_name = 'tf_broadcaster_demo'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/tf_broadcaster_demo']),
        ('share/tf_broadcaster_demo', ['package.xml']),
        ('share/tf_broadcaster_demo/launch', ['launch/dyn_tf.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    entry_points={
        'console_scripts': [
            'dyn_tf_broadcaster = tf_broadcaster_demo.dyn_tf_broadcaster:main',
        ],
    },
)
