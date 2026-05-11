# Projet 13 - Passage d’un système RAG du POC au MVP

## Contexte du projet

Dans ce projet, je transforme un système RAG développé lors du projet 11 en MVP scalable et industrialisable.

L’objectif est de concevoir une architecture cloud robuste capable de fournir des recommandations d’événements culturels personnalisées à travers un chatbot intelligent.

Le projet s’inscrit dans le parcours Data Engineer OpenClassrooms.

---

## Objectifs du MVP

- Ajouter une mémoire conversationnelle
- Ajouter un contexte géographique utilisateur
- Ajouter une recherche web temps réel
- Industrialiser le système RAG
- Mettre en place un monitoring
- Préparer un déploiement cloud AWS
- Structurer le projet avec Docker et configuration sécurisée

---

## Stack technique

- Python
- FastAPI
- LangChain
- FAISS
- Mistral AI
- Docker
- AWS
- YAML
- GitHub

---

## Structure du projet

```text
app/                -> code principal
config/             -> fichiers YAML
data/               -> données
docker/             -> configuration Docker
docs/               -> documentation projet
monitoring/         -> supervision et métriques
notebooks/          -> expérimentations
reports/            -> livrables projet
tests/              -> tests unitaires
vector_store/       -> index vectoriels