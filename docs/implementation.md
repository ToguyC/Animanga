## Implémentation

### Base de données

Le projet de TPI contient 2 types de base de données différents. La base principale est en Sqlite3 et la base de backup distante est en MySQL. Ces deux bases doivent pouvoir stocker les utilisateurs, les animes, les listes personnelles des utilisateurs, ainsi que les favoris des utilisateurs.

Voici le modèle réalisé :

![](https://i.loli.net/2020/05/26/CiqWlPVISstmKn2.png)

### Dictionnaire de données

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