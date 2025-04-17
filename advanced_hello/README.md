## 1. Création d’un package ROS2 Python
- Création du dossier advanced_hello

- Fichiers essentiels ajoutés : setup.py, package.xml, __init__.py

- Package structuré selon les bonnes pratiques ROS2

## 2. Création d’un publisher talker.py
- Envoie un message "Bonjour" sur le topic chatter

- Fréquence de publication configurable

- Lit les paramètres depuis un fichier YAML (plus de valeur codée en dur)

## 3. Création d’un subscriber listener.py
- Écoute le topic chatter

- Affiche le message reçu dans le terminal

- Utilise une fonction de callback automatique

## 4. Mise en place d’un fichier launch.py avancé
- Lance automatiquement talker + listener

- Utilise un fichier .yaml pour passer des paramètres

- Fichier propre, structuré avec Node() et LaunchDescription

## 5. Création d’un fichier params.yaml
- Paramètre frequency : modifie la vitesse d’envoi du message

- Autres paramètres personnalisables : robot_name, debug_mode

- YAML bien lié au launch.py et utilisé dans talker.py

## 📦 Arborescence du package

```bash
advanced_hello/
├── package.xml
├── setup.py
├── advanced_hello/
│   ├── talker.py
│   ├── listener.py
│   ├── launch/
│   │   └── launch.py
│   └── params/
│       └── params.yaml
