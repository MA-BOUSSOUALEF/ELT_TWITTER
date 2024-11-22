# **Twitter Data Pipeline Project**

Ce projet implémente un pipeline de données en utilisant **Python 3**, **Apache Airflow**, et **AWS**. Il vise à extraire, transformer et charger des données Twitter issues d'un fichier CSV Kaggle, puis à les servir via une API locale.

---

## **Contexte**

Twitter a retiré la majorité des données accessibles via son API, rendant l'accès direct impossible pour certaines données publiques. Pour contourner cela, un fichier CSV contenant des données Twitter a été récupéré depuis [Kaggle](https://www.kaggle.com/). Ces données ont ensuite été :
- **Traitées** : nettoyage et normalisation des colonnes et valeurs.
- **Transformées** : enrichissement ou modification des données pour qu'elles soient prêtes à l'usage.
- **Servies** : rendues accessibles via une API locale.

Enfin, **Apache Airflow** est utilisé pour orchestrer l'ensemble des étapes du pipeline, qui tourne sur une instance EC2 AWS. Les fichiers résultants sont stockés sur **Amazon S3**.

---

## **Architecture du Pipeline**

### 1. **Extraction**
- Les données sont extraites depuis un fichier CSV récupéré sur Kaggle.
- Ce fichier est chargé dans le pipeline pour un traitement ultérieur.

### 2. **Transformation**
- Les données extraites sont nettoyées pour supprimer les valeurs manquantes, les doublons et normaliser les formats.
- Les colonnes inutiles ou redondantes sont supprimées, et les données sont mises au format nécessaire pour l'analyse.

### 3. **Chargement (ETL)**
- Les données nettoyées sont exportées vers un fichier CSV, puis stockées sur **AWS S3**.
- Une API locale, créée avec Python, expose les données transformées pour des utilisations futures.

### 4. **Orchestration avec Airflow**
- Airflow est configuré pour exécuter les étapes ETL via un **DAG (Directed Acyclic Graph)**. 
- Airflow est déployé sur une instance EC2 AWS.

---

## **Technologies Utilisées**

- **Python 3** : Langage principal pour le développement du pipeline.
- **Apache Airflow** : Orchestration des tâches ETL.
- **AWS S3** : Stockage des fichiers CSV transformés.
- **AWS EC2** : Hébergement d'Airflow et de l'API locale.
- **Kaggle** : Source des données Twitter.
- **API locale (Flask ou FastAPI)** : Interface pour exposer les données.

---

## **Installation et Exécution**

### Prérequis
- Python 3.10+
- Apache Airflow
- Compte AWS avec accès à S3
- Instance EC2 configurée
- Bibliothèques Python nécessaires (listées dans `twitter_commande.sh`)

### Étapes

1. **Cloner le dépôt**
   ```bash
   git clone git@github.com:MA-BOUSSOUALEF/ELT_TWITTER.git
   
## This is API
<img width="604" alt="csvToAPi" src="https://github.com/user-attachments/assets/1307a446-e58a-43c9-b266-03d776719c4b">

## This is Airflow
<img width="937" alt="twitter" src="https://github.com/user-attachments/assets/22062687-16d2-422e-9061-c935276f0643">
