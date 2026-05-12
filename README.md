# RAG Events MVP - Projet 13 Data Engineer

## Présentation du projet

Ce projet est le MVP d’un système RAG dédié à la recommandation d’événements culturels.

Je suis parti d’un POC réalisé dans le projet 11, puis j’ai construit une version plus propre, plus structurée et plus proche d’un MVP exploitable.

L’objectif est de transformer une première preuve de concept IA en application backend documentée, conteneurisée et préparée pour un futur déploiement cloud.

## Objectifs

Ce projet me permet de démontrer ma capacité à construire une API FastAPI, intégrer un moteur de recherche vectoriel FAISS, générer des embeddings, connecter un LLM avec Mistral, gérer une mémoire conversationnelle simple, sécuriser la configuration avec un fichier .env, conteneuriser l’application avec Docker et préparer une architecture compatible avec AWS.

## Fonctionnalités principales

- API REST avec FastAPI
- Documentation automatique avec Swagger
- Ingestion de données JSON
- Génération d’embeddings
- Index vectoriel FAISS
- Recherche sémantique
- Réponse RAG avec sources
- Connexion Mistral
- Mémoire conversationnelle locale
- Logs applicatifs dans logs/app.log
- Configuration YAML et variables d’environnement
- Docker Compose pour l’exécution locale

## Architecture simplifiée

Utilisateur
   |
   v
FastAPI
   |
   +-- Ingestion JSON
   +-- Embeddings Sentence Transformers
   +-- Index vectoriel FAISS
   +-- Recherche des documents pertinents
   +-- Construction du prompt RAG
   +-- Appel API Mistral
   +-- Réponse avec sources

## Structure du projet

.
├── app
│   ├── core
│   ├── models
│   ├── services
│   └── main.py
├── config
│   ├── app.yaml
│   └── logging.yaml
├── data
│   └── raw
├── docker
│   └── Dockerfile
├── docs
├── logs
├── monitoring
├── notebooks
├── reports
├── tests
├── vector_store
├── .env.example
├── .gitignore
├── docker-compose.yml
├── README.md
└── requirements.txt

## Technologies utilisées

- Python
- FastAPI
- Uvicorn
- Pydantic
- Sentence Transformers
- FAISS
- Mistral API
- Docker
- Docker Compose
- YAML
- Git / GitHub

## Lancement local

1. Cloner le projet

git clone https://github.com/SamB-DATA/rag-events-mvp.git
cd rag-events-mvp

2. Créer le fichier .env

cp .env.example .env

Puis renseigner la clé Mistral si disponible :

MISTRAL_API_KEY=your_mistral_api_key_here

3. Lancer avec Docker

docker compose up --build

4. Ouvrir Swagger

http://localhost:8000/docs

## Endpoints principaux

GET /health - Vérifie que l’API fonctionne
GET /documents - Affiche les documents chargés
POST /rag/build-index - Construit l’index FAISS
GET /rag/status - Vérifie l’état de l’index
POST /rag/search - Lance une recherche sémantique
POST /rag/ask - Génère une réponse RAG avec Mistral
POST /chat/ask - Pose une question avec mémoire conversationnelle
GET /chat/history/{session_id} - Consulte l’historique d’une session
DELETE /chat/history/{session_id} - Supprime l’historique d’une session

## Exemple de requête

{
  "session_id": "samir-test",
  "query": "Je cherche un concert de musique",
  "top_k": 2
}

## Exemple de réponse

{
  "session_id": "samir-test",
  "query": "Je cherche un concert de musique",
  "answer": "Voici les concerts qui correspondent à ta recherche...",
  "sources": [
    {
      "id": "event_003",
      "title": "Concert classique en plein air",
      "location": "Bordeaux",
      "date": "2026-08-10"
    }
  ],
  "history_size": 2
}

## Sécurité

Le projet utilise un fichier .env non versionné, un fichier .env.example pour documenter les variables, un .gitignore pour exclure les secrets, les logs et les fichiers générés.

Les clés API ne doivent jamais être poussées sur GitHub.

## Limites actuelles du MVP

Cette version reste un MVP. Les limites principales sont :

- mémoire conversationnelle stockée uniquement en mémoire locale
- index FAISS généré localement
- pas encore de base de données
- pas encore de CI/CD
- pas encore de déploiement AWS
- pas encore de monitoring CloudWatch
- pas encore d’évaluation RAG automatisée

## Prochaines étapes

- Ajouter des tests unitaires et API
- Ajouter une configuration Docker production
- Préparer le déploiement AWS
- Publier l’image Docker dans ECR
- Déployer l’API sur ECS Fargate
- Ajouter CloudWatch pour les logs
- Ajouter GitHub Actions pour la CI/CD
- Documenter les coûts cloud
- Ajouter une évaluation qualité du RAG

## Compétences démontrées

Avec ce projet, je démontre des compétences en développement backend Python, API REST, conteneurisation, recherche vectorielle, intégration LLM, architecture RAG, gestion de configuration, logging, versionnement Git et préparation cloud.

## Auteur

Samir Belasri
Projet 13 - Parcours Data Engineer OpenClassrooms