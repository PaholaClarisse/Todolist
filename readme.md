## Todolist API – Gestionnaire de tâches avec FastAPI
## Description

Ce projet est une API REST développée avec FastAPI permettant de gérer une liste de tâches (Todolist).
Elle permet de créer, lire, modifier et supprimer des tâches, avec des fonctionnalités supplémentaires comme la pagination et le filtrage.

## Fonctionnalités
1. Créer une tâche
2. Lister toutes les tâches
3. Afficher une tâche spécifique
4. Pagination des tâches
5. Filtrer les tâches (faites / non faites)
6. Filtrer par date
7. Modifier une tâche (par ID ou titre)
8. Supprimer une tâche (par ID ou titre)

## Technologies utilisées
. Python3
. FastAPI 
. Pydantic (validation des données)

## Installation
Cloner le projet :
. git clone https://github.com/PaholaClarisse/todolist-fastapi.git
. cd todolist-fastapi

## Créer un environnement virtuel :
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

## Installer les dépendances :
pip install fastapi uvicorn
▶️ Lancer l’application
uvicorn main:app --reload
🌐 Accès à l’API
API : http://127.0.0.1:8000
Documentation interactive (Swagger) :
👉 http://127.0.0.1:8000/docs

## Modèle de données
{
  "Id": 1,
  "title": "Faire les courses",
  "description": "Acheter du lait",
  "status": false,
  "date": "2026-03-21T10:00:00"
}

## Endpoints principaux
🔹 Accueil
GET /
🔹 Créer une tâche
POST /task
🔹 Lister toutes les tâches
GET /tasks
🔹 Pagination
GET /task/pagination?debut=0&limit=5
🔹 Obtenir une tâche par ID
GET /task{task_id}
🔹 Supprimer une tâche par ID
DELETE /task{task_id}
🔹 Modifier une tâche par ID
PUT /task{task_id}
🔹Supprimer une tâche par titre
DELETE /task{task_title}
🔹Modifier une tâche par titre
PUT /task{task_title}