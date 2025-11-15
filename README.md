# Étude économétrique : déterminants de l’octroi d’un prêt

Ce projet a pour objectif d’identifier les facteurs socio-économiques influençant la probabilité d’obtenir un prêt bancaire.  
Il s’inscrit dans le cadre d’un travail d’économétrie appliquée et mobilise les outils statistiques utilisés dans l’analyse de données.

## Objectifs du projet

- Construire un modèle linéaire multiple expliquant l’octroi d’un prêt.
- Étudier l’impact de variables socio-économiques : revenu, âge, statut familial, taux d’endettement, etc.
- Réaliser des tests de significativité (t-test, F-test).
- Évaluer la qualité du modèle (R², R² ajusté, analyse des résidus).
- Identifier les variables ayant le plus d’influence sur la décision d’octroi.
- Interpréter les résultats afin d’en tirer des conclusions économiques.

## Données

Les données sont importées depuis le fichier :

data/donnees_pret.xlsx

Elles contiennent notamment :

- Revenu
- Âge
- Taux d’endettement
- Situation familiale
- Montant demandé
- Variable binaire : prêt accordé (1 = oui, 0 = non)

## Méthodologie économétrique

- Nettoyage et préparation des données
- Estimation d’un modèle linéaire multiple (OLS)
- Analyse des coefficients estimés
- Tests statistiques :
  - t-tests (significativité individuelle)
  - F-test (significativité globale)
  - Intervalles de confiance
- Détection de problèmes potentiels :
  - Hétéroscédasticité
  - Multicolinéarité
  - Résidus non normaux

## Stack technique

- Excel : exploration initiale
- Python :
  - pandas : manipulation des données
  - numpy : transformations numériques
  - statsmodels : régression linéaire et tests
  - matplotlib / seaborn : visualisation

## Structure du projet
``` texte
.
├─ data/
│  └─ donnees_pret.xlsx
├─ src/
│  └─ analyse_modele.py
├─ notebooks/
│  └─ 01_modele_lineaire.ipynb
├─ README.md
├─ requirements.txt
```

## Compétences mises en avant

- Économétrie appliquée
- Régression linéaire multiple (OLS)
- Analyse statistique et tests de significativité
- Visualisation de données
- Nettoyage et préparation de données
- Interprétation orientée business
- Utilisation de Python pour l’analyse économique

## Auteur

Projet réalisé par **Lachique Tom**  
Étudiant en Master Information, Communication parcours Data analytics et stratégie de l'information (Université de Toulon)  
À la recherche d’un stage en data analyst.

E-mail : tom.lachique.135@gmail.com  
LinkedIn : https://www.linkedin.com/in/tom-lachique-9b969427b/


