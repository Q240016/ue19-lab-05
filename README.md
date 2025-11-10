# UE19 Lab 05 - Application JokesAPI

Ce projet est une application Python simple qui utilise la librairie `requests` pour interroger l'API publique [JokesAPI](https://v2.jokeapi.dev/) et afficher une blague aléatoire dans la console.

## Prérequis

- Python 3
- Docker (optionnel, pour l'exécution conteneurisée)

## Installation et exécution locale

1. Clonez ce repository.
2. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
Construisez l'image Docker : Cette commande lit le Dockerfile et crée une image locale nommée app.

docker build -t app .

Lancez le conteneur : Cette commande exécute l'image app-activite. L'option --rm nettoie et supprime le conteneur après son exécution.

docker run --rm app

Une idée d'activité devrait alors s'afficher dans votre terminal.
