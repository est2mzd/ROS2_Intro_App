from setuptools import setup

package_name='rqt_console_demo'

setup(
 name=package_name,
 version='0.0.0',
 packages=[package_name],
 data_files=[
   ('share/ament_index/resource_index/packages',['resource/'+package_name]),
   ('share/'+package_name,['package.xml']),
   ('share/'+package_name+'/launch',['launch/emit_warning.launch.py']),
 ],
 install_requires=['setuptools'],
 zip_safe=True,
 entry_points={'console_scripts':['emit_logs = rqt_console_demo.emit_logs:main']},
)
