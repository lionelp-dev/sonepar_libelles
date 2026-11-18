# Sonepar Libellés

Projet pédagogique réalisé dans le cadre d’un entretien pour une alternance. Il s’agit d’un cas pratique autonome, inspiré des enjeux de gestion des habilitations de l’ERP Infor M3.

L’application Django illustre comment rendre les droits associés aux fonctions M3 compréhensibles et exploitables. Faute d’accès à un environnement Infor M3 dans le cadre de cet exercice, les données sources sont simulées à l’aide de fichiers CSV placés dans le dossier `donnees/`.

## Contexte pédagogique

Le cas d’usage s’inspire d’une équipe chargée de la gestion des habilitations et des audits M3 : autoriser ou non certains profils à accéder aux fonctions de l’ERP, puis exploiter ces données dans des rapports ou des exports.

Ce dépôt couvre le volet **Django / Python** de l’exercice. Il ne constitue pas une application interne de Sonepar et ne se connecte à aucun environnement M3.

## Finalité métier

Dans le cadre de cet exercice, les niveaux d’accès aux fonctions M3 sont représentés par des valeurs numériques (`0`, `1` ou `2`). L’application associe ces valeurs à leurs libellés correspondants afin de faciliter leur lecture et leur interprétation.

Elle permet notamment de préparer des données enrichies pour des exports CSV, contenant à la fois le niveau d’accès et son libellé métier.

## Données simulées

Les fichiers CSV du dossier `donnees/` constituent un jeu de données fictif destiné à initialiser la base de données de l’application Django.

Ils sont organisés en deux ensembles : les données simulant les informations récupérables depuis M3 et les référentiels de correspondance utilisés pour leur associer des libellés.

### Données issues de M3

Quatre fichiers simulent les réponses de transactions API d’Infor M3 :

| Fichier CSV | API / Transaction | Contenu |
| --- | --- | --- |
| `MNS150MI_LstUsers.csv` | MNS150MI / LstUsers | Utilisateurs M3 |
| `MNS405MI_Lst.csv` | MNS405MI / Lst | Rôles disponibles |
| `MNS410MI_LstRolesByUser.csv` | MNS410MI / LstRolesByUser | Rôles attribués aux utilisateurs |
| `SES400MI_LstAuthByRole.csv` | SES400MI / LstAuthByRole | Autorisations par rôle et fonction |

Ces fichiers permettent de représenter les relations entre les utilisateurs, leurs rôles et les autorisations associées aux fonctions M3.

Les structures et les données ont été simplifiées pour les besoins de l’exercice. Elles ne constituent pas des réponses authentiques des API M3.

### Référentiels de libellés

Trois fichiers complémentaires définissent les correspondances utilisées par l’application :

| Fichier CSV | Contenu |
| --- | --- |
| `libelles_fonctions.csv` | Codes des fonctions M3 et libellés correspondants |
| `libelles_niveaux_acces.csv` | Niveaux d’accès numériques et libellés associés |
| `libelles_options.csv` | Codes des options autorisées et libellés correspondants |

Pour les besoins de l’exercice, les niveaux d’accès sont interprétés selon la correspondance suivante :

| Niveau | Libellé |
| --- | --- |
| `0` | Aucun droit actif accordé par ce rôle |
| `1` | Consultation uniquement |
| `2` | Modification autorisée |

Cette classification est une convention pédagogique et ne correspond pas à une nomenclature standard confirmée des autorisations de fonctions M3.

### Exploitation des données

Une fois les fichiers importés en base de données, l’application peut rapprocher les utilisateurs, leurs rôles et les autorisations associées aux fonctions M3.

Les référentiels permettent ensuite d’enrichir ces informations avec les libellés des fonctions, des niveaux d’accès et des options autorisées, afin de produire des exports CSV compréhensibles et exploitables dans le cadre des audits.

## Prérequis

- Python 3.12 ou supérieur ;
- `pip` ;
- Git (pour cloner le dépôt).

Le projet utilise SQLite en développement : aucune base de données externe n'est nécessaire. La base est créée dans `database/db.sqlite3` lors de l'application des migrations.

## Structure du projet

```text
app/        Application Django et commandes de gestion
config/     Configuration Django
database/   Base SQLite locale
donnees/    Fichiers CSV simulant les données M3
manage.py   Point d'entrée Django
```

## Installation

Depuis la racine du dépôt :

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Sous Windows (PowerShell), l'activation de l'environnement virtuel s'effectue avec :

```powershell
.\.venv\Scripts\Activate.ps1
```

## Initialiser les données

Appliquer les migrations, charger les référentiels CSV, puis générer un audit :

```bash
python manage.py migrate
python manage.py seed_all
python manage.py audit_habilitations
```

La commande `seed_all` charge les référentiels de fonctions, niveaux d'accès, options, utilisateurs, rôles et associations M3. Chaque seeder ne charge des données que si sa table est vide.

La commande `audit_habilitations` rapproche les utilisateurs, rôles, autorisations et référentiels. Elle crée un audit horodaté et affiche ses habilitations dans le terminal. Chaque lancement conserve un nouvel historique dans la base.

## Données

Les CSV attendus par les commandes de chargement se trouvent dans `donnees/`. Ils sont séparés par des points-virgules et encodés en UTF-8. Gardez leurs noms et leurs en-têtes inchangés pour que les commandes `*_seed` puissent les importer.

## Technologies

### Utilisées dans ce dépôt

- Python
- Django
- Django REST Framework
- SQLite
