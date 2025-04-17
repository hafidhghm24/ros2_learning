from launch import LaunchDescription
from launch_ros.actions import Node
import os

def generate_launch_description():

    # 📂 Chemin absolu vers le fichier params.yaml
    config = os.path.join(
        os.path.dirname(__file__),  # Chemin du dossier où se trouve launch.py
        '..', 'params', 'params.yaml'  # On remonte d’un dossier et on va dans params/
    )

    talker_node = Node(
        package='advanced_hello',
        executable='talker',
        name='talker',
        output='screen',
        parameters=[config]  # 📎 On lie le fichier YAML ici !
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
