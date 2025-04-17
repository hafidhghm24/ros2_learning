from launch import LaunchDescription
from launch_ros.actions import Node
import os

def generate_launch_description():
    config = os.path.join(
        os.path.dirname(__file__),
        '..', 'params', 'params.yaml'
    )

    talker_node = Node(
        package='advanced_hello',
        executable='talker',
        name='talker',
        output='screen',
        parameters=[config]
    )

    listener_node = Node(
        package='advanced_hello',
        executable='listener',
        name='listener',
        output='screen'
    )

    return LaunchDescription([
        talker_node,
        listener_node
    ])
