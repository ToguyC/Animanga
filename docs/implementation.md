## Implémentation

### Base de données

Le projet de TPI contient 2 types de base de données différents. La base principale est en Sqlite3 et la base de backup distante est en MySQL. Ces deux bases doivent pouvoir stocker les utilisateurs, les animes, les listes personnelles des utilisateurs, ainsi que les favoris des utilisateurs.

Voici le modèle réalisé :

![](https://i.loli.net/2020/05/26/CiqWlPVISstmKn2.png)

#### Dictionnaire de données

<span style="font-weight: bold; font-size: 1.2rem">anime</span>

| Colonne          | Type         | Null |
| ---------------- | ------------ | ---- |
| **idAnime**      | int(11)      | Non  |
| title            | varchar(200) | Non  |
| *#type*          | int(11)      | Non  |
| episodes         | int(3)       | Non  |
| *#status*        | int(11)      | Non  |
| picture          | varchar(200) | Non  |
| thumbnail        | varchar(200) | Non  |
| synonyms         | text         | Oui  |
| modificationDate | timestamp    | Non  |

<span style="font-weight: bold; font-size: 1.2rem">status</span>

| Colonne          | Type        | Null |
| ---------------- | ----------- | ---- |
| **idStatus**     | int(11)     | Non  |
| nameStatus       | varchar(20) | Non  |
| modificationDate | timestamp   | Non  |

<span style="font-weight: bold; font-size: 1.2rem">type</span>

| Colonne          | Type        | Null |
| ---------------- | ----------- | ---- |
| **idType**       | int(11)     | Non  |
| nameType         | varchar(10) | Non  |
| modificationDate | timestamp   | Non  |

<span style="font-weight: bold; font-size: 1.2rem">url</span>

| Colonne          | Type        | Null |
| ---------------- | ----------- | ---- |
| **idUrl**        | int(11)     | Non  |
| urlName          | varchar(45) | Non  |
| *#idAnime*       | int(11)     | Non  |
| isRelation       | tinyint(1)  | Non  |
| modificationDate | timestamp   | Non  |

<span style="font-weight: bold; font-size: 1.2rem">list</span>

| Colonne          | Type        | Null |
| ---------------- | ----------- | ---- |
| **idList**       | int(11)     | Non  |
| nameList         | varchar(45) | Non  |
| modificationDate | timestamp   | Non  |

<span style="font-weight: bold; font-size: 1.2rem">list_has_anime</span>

| Colonne            | Type      | Null |
| ------------------ | --------- | ---- |
| **idListHasAnime** | int(11)   | Non  |
| ***#idList***      | int(11)   | Non  |
| ***#idAnime***     | int(11)   | Non  |
| modificationDate   | timestamp | Non  |

<span style="font-weight: bold; font-size: 1.2rem">user</span>

| Colonne          | Type        | Null |
| ---------------- | ----------- | ---- |
| **idUser**       | int(11)     | Non  |
| emailUser        | varchar(45) | Non  |
| password         | varchar(45) | Non  |
| nicknameUser     | varchar(45) | Non  |
| modificationDate | timestamp   | Non  |

<span style="font-weight: bold; font-size: 1.2rem">user_has_list</span>

| Colonne           | Type      | Null |
| ----------------- | --------- | ---- |
| **idUserHasList** | int(11)   | Non  |
| ***#idUser***     | int(11)   | Non  |
| ***#idList***     | int(11)   | Non  |
| modificationDate  | timestamp | Non  |

<span style="font-weight: bold; font-size: 1.2rem">user_has_favorite</span>

| Colonne               | Type      | Null |
| --------------------- | --------- | ---- |
| **idUserHasFavorite** | int(11)   | Non  |
| ***#idUser***         | int(11)   | Non  |
| ***#idAnime***        | int(11)   | Non  |
| orderId               | int(11)   | Non  |
| modificationDate      | timestamp | Non  |

### Structure

* <img style="float: right; margin-left: 25px; width: 35%" src="https://i.imgur.com/tO7qVFN.png">**/** : Contient tout les fichiers de configuration ainsi que les routes
* **/docs** : Contient la documentation de tout mon projet
    * **/docs/compiled** : Contient la documentation compilée
    * **/docs/scripts** : Contient tout les scripts permettant de créer un fichier unique contenant toute la documentation
* ***/node_modules*** : Contient les dépendances JavaScript (géré par NPM)
* **/packages** : Contient les fichiers `python`
    * **/packages/controllers** : Contient les contrôleurs
    * **/packages/models** : Contient les modèles de données
* **/static** : Contient les fichiers statiques
    * **/static/css** : Contient les fichiers `css`
    * **/static/database** : Contient la base de données sqlite3
    * **/static/fonts** : Contient les polices
    * **/static/img** : Contient les images / svg
    * **/static/js** : Contient les fichiers `javascript`
    * **/static/json** : Contient le fichier `json` contenant tout les animes
    * **/static/scss** : Contient les fichiers `scss`
    * **/static/swagger-components** : Contient les composants pour swagger
* **/templates** : Contient les pages à afficher
    * **/templates/layouts** : Contient le layout générique ainsi que les fichier pouvant être inclus
* **/tests** : Contient le fichier `html` pour Katalon Recorder



### Classes (Python)

Pour correctement interagir avec le code Python, et comme demandé dans le point **A20**, j'ai écrit les classes suivantes :

**\packages\controllers\ActivitiesController**

Classe permettant le contrôle des activités de l'utilisateur

**\packages\controllers\AnimeController**

Classe permettant le contrôle des animes

**\packages\controllers\authentification**

Contient les classe permettant la validation des données des formulaires d'authentification

**\packages\controllers\ListController**

Classe permettant le contrôle des listes

**\packages\controllers\logger**

Contient la fonction utilisée par tout les `except` afin de log les potentielles erreurs

**\packages\controllers\MySQLController**

Classe permettant d'interagir avec la base de données MySQL

**\packages\controllers\SqliteController**

Classe permettant d'interagir avec la base de données Sqlite3

**\packages\controllers\StatusController**

Classe permettant le contrôle des statuts

**\packages\controllers\TypeController**

Classe permettant le contrôle des types

**\packages\controllers\UserController**

Classe permettant le contrôle des utilisateurs

**\packages\models\Anime**

Modèle représentant un anime

**\packages\models\List**

Modèle représentant une liste

**\packages\models\Status**

Modèle représentant un statut

**\packages\models\Type**

Modèle représentant un type

**\packages\models\User**

Modèle représentant un utilisateur

### API interne

Animanga possède un système d'API interne permettant de faire des actions sur les données depuis le front-end. Voici les différentes url d'entrées :

**/get/favorites/**

Permet de récupérer tous les favoris de l'utilisateur connecté

**/get/favorites/\<string:nickname>**

Permet de récupérer tous les favoris d'un utilisateur

**/set/favorite**

Met à jour le statut de favoris d'un anime pour l'utilisateur connecté

**/set/list**

Met à jour l'association d'un anime à une liste

**/delete/defaults**

Permet de supprimer l'anime des listes par défauts de l'utilisateur connecté (Complétés, En cours, Planifiés, Abandonnés)

**/get/animes**

Permet de récupérer les animes d'une liste

**/add/list**

Permet d'ajouter une nouvelle liste à l'utilisateur connecté

**/delete/list**

Permet de supprimer une liste de l'utilisateur connecté

**/set/list/name**

Met à jour le nom d'une liste

**/set/favorites-order**

Met à jour l'ordre des favoris

**/get/activities**

Permet de récupérer toutes les activités des dernières 24h de l'utilisateur connecté