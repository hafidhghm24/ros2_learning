from setuptools import find_packages, setup

package_name = 'advanced_hello'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['advanced_hello/launch/launch.py']),
        ('share/' + package_name + '/params', ['advanced_hello/params/params.yaml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='hafidh',
    maintainer_email='hafidh@example.com',
    description='Talker/Listener ROS2 avec paramètres YAML',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = advanced_hello.talker:main',
            'listener = advanced_hello.listener:main'
        ],
    },
)
