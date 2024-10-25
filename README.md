# Le GastroAnnuaire®

Un annuaire gastronomique moderne réalisé en Django.

## Description

**Le GastroAnnuaire®** est un projet éducatif de type annuaire de restaurants et établissements culinaires, conçu pour permettre aux utilisateurs de consulter, rechercher et partager leurs avis sur divers lieux gastronomiques. Le projet est développé en Django et propose une structure modulaire avec différentes applications pour la gestion des restaurants, commentaires, usagers, et fonctionnalités administratives.

## Fonctionnalités

- **Liste d'établissements** : Catégorisation des établissements par type (restaurant, café, boulangerie, etc.).
- **Fiches détaillées** : Informations complètes pour chaque établissement avec description, emplacement et coordonnées.
- **Gestion des utilisateurs** : Système d'authentification avec gestion de profil.
- **Avis et notations** : Les utilisateurs peuvent noter et commenter chaque établissement.
- **Recherche** : Fonction de recherche et de filtrage pour trouver les établissements selon les critères souhaités.
  
## Technologies et Outils Utilisés

- **Framework** : Django 5.0.1
- **Base de données** : SQLite (configurée par défaut, extensible à d'autres SGBD)
- **Front-end** : Django Templates, CSS, et JavaScript
- **Formulaires** : Utilisation de `crispy_forms` avec le pack de templates `bootstrap4`
- **Authentification** : Basée sur le système Django avec redirection après connexion
  
## Installation et Lancement en Local

Suivez ces étapes pour installer et lancer le projet sur votre machine :

1. **Cloner le dépôt** :
   ```bash
   git clone https://github.com/lilianmirabel/Le-GastroAnnuaire.git
   cd Le-GastroAnnuaire
   ```

2. **Créer un environnement virtuel** (optionnel mais recommandé) :
   ```bash
   python3 -m venv env
   source env/bin/activate  # Sur Windows : env\Scripts\activate
   ```

3. **Installer les dépendances** :
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurer la base de données** :
   Appliquez les migrations pour configurer la base de données SQLite :
   ```bash
   python manage.py migrate
   ```

5. **Démarrer le serveur** :
   ```bash
   python manage.py runserver
   ```

6. **Accéder à l'application** :
   Visitez [http://127.0.0.1:8000](http://127.0.0.1:8000) dans votre navigateur pour accéder à l'application.

## Structure des Applications

Le projet utilise plusieurs applications pour organiser les fonctionnalités de manière modulaire :

- **`commentaire`** : Gestion des avis et notations des utilisateurs.
- **`restaurant`** : Gestion des informations d'établissement, y compris type de cuisine, adresse, et description.
- **`administrateur`** : Interface pour la gestion des utilisateurs et du contenu.
- **`usagers`** : Gestion de l'authentification et du profil utilisateur.

## Configuration des Templates et Statics

Les chemins des templates sont configurés dans `settings.py` pour chaque application, et les fichiers statiques sont stockés dans `TPFinal/static`. Le package `crispy_forms` est configuré avec `bootstrap4` pour une meilleure présentation des formulaires.

## Configuration de Sécurité

**Attention** : Ce projet est en mode développement avec `DEBUG = True`. Avant de déployer en production, assurez-vous de :
- Désactiver le mode debug (`DEBUG = False`).
- Changer la clé secrète (`SECRET_KEY`) pour une version plus sécurisée.
- Configurer `ALLOWED_HOSTS` avec les domaines de votre déploiement.

## Contribution

Les contributions sont les bienvenues ! Pour contribuer :

1. **Forkez le dépôt**.
2. **Créez une branche de fonctionnalité** : `git checkout -b feature/AjoutDeFonctionnalité`.
3. **Apportez vos modifications** et **committez-les** : `git commit -m 'Ajout d'une fonctionnalité'`.
4. **Poussez la branche** : `git push origin feature/AjoutDeFonctionnalité`.
5. **Ouvrez une Pull Request**.

## Auteurs

Développé par [Lilian Mirabel](https://github.com/lilianmirabel) dans le cadre d'un projet de cours.
