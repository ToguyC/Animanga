## Planification

### Product backlog


| Nom                            | S1 : Inscription à Animanga                                                                      |
| ------------------------------ | ------------------------------------------------------------------------------------------------ |
| **Description (*user story*)** | En tant qu'utilisateur non connecté, je peux me créer un compte afin de pouvoir accéder au site. |
| **Critère d'acceptation**      | ***Pas encore écris de tests***                                                                  |
| **Priorité**                   | 🚫 Bloquant                                                                                      |

| Nom                            | S2 : Connexion à Animanga                                    |
| ------------------------------ | ------------------------------------------------------------ |
| **Description (*user story*)** | En tant qu'utilisateur non connecté, je peux me connecter afin de pouvoir accéder au site. |
| **Critère d'acceptation**      | ***Pas encore écris de tests***                              |
| **Priorité**                   | 🚫 Bloquant                                                   |

| Nom                            | S3 : Importation des animes                                  |
| ------------------------------ | ------------------------------------------------------------ |
| **Description (*user story*)** | En tant qu'utilisateur connecté, je peux écraser les animes avec un nouveau set de données. |
| **Critère d'acceptation**      | ***Pas encore écris de tests***                              |
| **Priorité**                   | 💥 Critique                                                   |

| Nom                            | S4 : Rechercher des animes                                   |
| ------------------------------ | ------------------------------------------------------------ |
| **Description (*user story*)** | En tant qu'utilisateur connecté, je peux effectué une recherche afin d'ajouter des animes dans mes listes personnelles ou de les mettre en tant que *favoris*. |
| **Critère d'acceptation**      | ***Pas encore écris de tests***                              |
| **Priorité**                   | 💥 Critique                                                   |

| Nom                            | S5 : Affichage de la carte d'un anime                        |
| ------------------------------ | ------------------------------------------------------------ |
| **Description (*user story*)** | En tant qu'utilisateur connecté, je peux cliquer sur le titre d'un anime présent dans les résultats de ma présédente recherche afin d'accéder à ses informatinos. |
| **Critère d'acceptation**      | ***Pas encore écris de tests***                              |
| **Priorité**                   | ❗ Important                                                  |

| Nom                            | S6 : Mise à jour d'un anime                                  |
| ------------------------------ | ------------------------------------------------------------ |
| **Description (*user story*)** | En tant qu'utilisateur connecté, je peux mettre à jour le statut, l'appartenance à une liste personnel ainsi que le statut de favoris d'un anime. |
| **Critère d'acceptation**      | ***Pas encore écris de tests***                              |
| **Priorité**                   | ❗ Important                                                  |

| Nom                            | S7 : Affichage du profile                                    |
| ------------------------------ | ------------------------------------------------------------ |
| **Description (*user story*)** | En tant qu'utilisateur connecté, je peux avoir accès à ma page de profile afin de pourvoir voir les statistiques et favoris. Il est également possible de voir la page de profile d'autre utilisateur du site. |
| **Critère d'acceptation**      | ***Pas encore écris de tests***                              |
| **Priorité**                   | ❗ Important                                                  |

| Nom                            | S8 : Affichage des listes                                    |
| ------------------------------ | ------------------------------------------------------------ |
| **Description (*user story*)** | En tant qu'utilisateur connecté, je peux avoir accès à ma page de listes afin de voir toutes mes listes et leur contenu. Il est également possible de voir les listes d'autre utilisateur du site. |
| **Critère d'acceptation**      | ***Pas encore écris de tests***                              |
| **Priorité**                   | ❗ Important                                                  |

| Nom                            | S9 : Gestion des listes                                      |
| ------------------------------ | ------------------------------------------------------------ |
| **Description (*user story*)** | En tant qu'utilisateur connecté, je peux gérer mes propres listes pour en ajouter, en supprimer, ou modifier leur nom. |
| **Critère d'acceptation**      | ***Pas encore écris de tests***                              |
| **Priorité**                   | ❗ Important                                                  |

| Nom                            | S10 : Affichage des favoris                                  |
| ------------------------------ | ------------------------------------------------------------ |
| **Description (*user story*)** | En tant qu'utilisateur connecté, je peux avoir accès à ma page favoris afin de voir tout mes favoris. Il est également possible de voir les favoris d'autre utilisateur du site. |
| **Critère d'acceptation**      | ***Pas encore écris de tests***                              |
| **Priorité**                   | ❗ Important                                                  |

| Nom                            | S10 : Gestion des favoris                                    |
| ------------------------------ | ------------------------------------------------------------ |
| **Description (*user story*)** | En tant qu'utilisateur connecté, je peux organiser l'ordre de mes favoris selon mes envies. |
| **Critère d'acceptation**      | ***Pas encore écris de tests\***                             |
| **Priorité**                   | ❗ Important                                                  |

| Nom                            | S11 : Affichage de la *landing page*                         |
| ------------------------------ | ------------------------------------------------------------ |
| **Description (*user story*)** | En tant qu'utilisateur non connecté, je n'ai ni accès aux animes ni aux listes. La barre de navigation m'affiche un lien pour me connecter et un autre pour m'inscrire. |
| **Critère d'acceptation**      | ***Pas encore écris de tests***                              |
| **Priorité**                   | ❓ Secondaire                                                 |

| Nom                            | S12 : Utilisation d'un git                                   |
| ------------------------------ | ------------------------------------------------------------ |
| **Description (*user story*)** | En tant que développeur, je dois pouvoir faire du versionnage de code source et pouvoir accéder à un dépôt distant Github. |
| **Critère d'acceptation**      | Le dépôt git local est configurer correctement et le lien sur le dépôt distant à été bien fait. |
| **Priorité**                   | 🚫 Bloquant                                                   |

| Nom                            | S13 : Configuration de la base de données                    |
| ------------------------------ | ------------------------------------------------------------ |
| **Description (*user story*)** | En tant que développeur, je dois pouvoir utilisé une base de données Sqlite3 et MySQL ayant un modèle identique à celui donné dans l'énoncé. Pour ce faire, j'ai une classe Python me permettant de faire des requêtes sur la base Sqlite3 et une autre classe me permettant de faire des requêtes sur la base MySQL. J'ai aussi un dump de la structure de la base MySQL dans les fichiers statiques de mon application. |
| **Critère d'acceptation**      | Les tables `animes`, `status`, `type`, `url`, `list`, `user`, `list_has_anime`, `user_has_list` et `user_has_favorites` ont bien été crées et sont utilisable par les contrôleurs dédiés. |
| **Priorité**                   | 🚫 Bloquant                                                   |

| Nom                            | S13 : Synchronisation MySQL Sqlite3                          |
| ------------------------------ | ------------------------------------------------------------ |
| **Description (*user story*)** | En tant que développeur, je dois pouvoir synchroniser les bases MySQL et Sqlite3 unidirectionellement pour créer un backup sur serveur distant. |
| **Critère d'acceptation**      | ***Pas encore écris de tests***                              |
| **Priorité**                   | ❓ Secondaire                                                 |

| Nom                            | S15 : Configuration Flask                                    |
| ------------------------------ | ------------------------------------------------------------ |
| **Description (*user story*)** | En tant que développeur, je dois configurer l'application Flask afin d'avoir un site hébergé en local et pouvoir communiquer avec la base de données Sqlite3. |
| **Critère d'acceptation**      | ***Pas encore écris de tests\***                             |
| **Priorité**                   | 🚫 Bloquant                                                   |

| Nom                            | S16 : Vérifications syntaxique                               |
| ------------------------------ | ------------------------------------------------------------ |
| **Description (*user story*)** | En tant que développeur, je peux lancé la commande `npm run lint` pour vérifier la syntaxe, basé sur le preset Airbnb, des fichiers JavaScript, et la commande `python3 -m pylint --output-format=colorized` pour vérifier la syntaxe des fichiers Python, basé sur les conventions PEP8. |
| **Critère d'acceptation**      | Les test *12.1* et *12.2* passent.                           |
| **Priorité**                   | 🚫 Bloquant                                                   |

## Diagramme de Gantt

Planning prévisionnel : <span style="color: #F7DC79; font-weight: bold">#F7DC79</span>

Planning réel : <span style="color: #7FC77F; font-weight: bold">#7FC77F</span>

<table>
    <thead>
        <tr>
            <th>Jour</th>
            <th colspan="2" style="text-align: center">J1<br><span>lu.25</span></th>
            <th colspan="2" style="text-align: center">J2<br><span>ma.26</span></th>
            <th colspan="2" style="text-align: center">J3<br><span>me.27</span></th>
            <th colspan="2" style="text-align: center">J4<br><span>je.28</span></th>
            <th colspan="2" style="text-align: center">J5<br><span>ve.29</span></th>
            <th colspan="2" style="text-align: center">J7<br><span>ma.2</span></th>
            <th colspan="2" style="text-align: center">J8<br><span>me.3</span></th>
            <th colspan="2" style="text-align: center">J9<br><span>je.4</span></th>
            <th colspan="2" style="text-align: center">J10<br><span>ve.5</span></th>
            <th colspan="2" style="text-align: center">J11<br><span>lu.8</span></th>
            <th colspan="2" style="text-align: center">J12<br><span>ma.9</span></th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan="2">Lecture de l'énoncé</td>
            <td style="background: #f7dc79;"></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td style="background: #7fc77f;"></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td rowspan="2">Rédaction backlog</td>
            <td style="background: #f7dc79;"></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td style="background: #7fc77f;"></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td rowspan="2">Rédaction scénarios</td>
            <td></td>
            <td style="background: #f7dc79;"></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td></td>
            <td style="background: #7fc77f;"></td>
            <td style="background: #7fc77f;"></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td rowspan="2">Rédaction planning</td>
            <td></td>
            <td style="background: #f7dc79;"></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td></td>
            <td style="background: #7fc77f;"></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
		<tr>
            <td rowspan="2" style="font-weight: bold; font-size: 15px">S12 : Utilisation d'un git</td>
            <td></td>
            <td style="background: #f7dc79;"></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td></td>
            <td style="background: #7fc77f;"></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td rowspan="2" style="font-weight: bold; font-size: 15px">S13 : Configuration de la base de données</td>
            <td></td>
            <td></td>
            <td style="background: #f7dc79;"></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td></td>
            <td></td>
            <td style="background: #7fc77f;"></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td rowspan="2" style="font-weight: bold; font-size: 15px">S15 : Configuration de Flask</td>
            <td></td>
            <td></td>
            <td style="background: #f7dc79;"></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td></td>
            <td></td>
            <td style="background: #7fc77f;"></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td rowspan="2" style="font-weight: bold; font-size: 15px">S3 : Importation des données</td>
            <td></td>
            <td></td>
            <td style="background: #f7dc79;"></td>
            <td style="background: #f7dc79;"></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td></td>
            <td></td>
            <td style="background: #7fc77f;"></td>
            <td style="background: #7fc77f;"></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td rowspan="2" style="font-weight: bold; font-size: 15px">S1 : Inscription à Animanga</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td style="background: #f7dc79;"></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td rowspan="2" style="font-weight: bold; font-size: 15px">S2 : Connexion à Animanga</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td style="background: #f7dc79;"></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
		<tr>
            <td rowspan="2" style="font-weight: bold; font-size: 15px">S11 : Affichage de la landing page</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td style="background: #f7dc79;"></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td></td>
            <td></td>
            <td></td>
            <td style="background: #7fc77f;"></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td rowspan="2" style="font-weight: bold; font-size: 15px">S4 : Rechercher des animes</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td style="background: #f7dc79;"></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td rowspan="2" style="font-weight: bold; font-size: 15px">S5 : Affichage de la carte de l'anime</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td style="background: #f7dc79;"></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td rowspan="2" style="font-weight: bold; font-size: 15px">S6 : Mise à jour de l'anime</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td style="background: #f7dc79;"></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td rowspan="2" style="font-weight: bold; font-size: 15px">S7 : Affichage du profile</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td style="background: #f7dc79;"></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td rowspan="2" style="font-weight: bold; font-size: 15px">S8 : Affichage des listes</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td style="background: #f7dc79;"></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td rowspan="2" style="font-weight: bold; font-size: 15px">S9 : Gestion des listes</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td style="background: #f7dc79;"></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td rowspan="2" style="font-weight: bold; font-size: 15px">S10 : Organisation des favoris</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td style="background: #f7dc79;"></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td rowspan="2" style="font-weight: bold; font-size: 15px">S14 : Synchronisation MySQL Sqlite3</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td style="background: #f7dc79;"></td>
            <td style="background: #f7dc79;"></td>
            <td style="background: #f7dc79;"></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td rowspan="2" style="font-weight: bold;">S16 : Vérifications syntaxique</td>
            <td></td>
            <td></td>
            <td></td>
            <td style="background: #f7dc79;"></td>
            <td style="background: #f7dc79;"></td>
            <td style="background: #f7dc79;"></td>
            <td style="background: #f7dc79;"></td>
            <td style="background: #f7dc79;"></td>
            <td style="background: #f7dc79;"></td>
            <td style="background: #f7dc79;"></td>
            <td style="background: #f7dc79;"></td>
            <td style="background: #f7dc79;"></td>
            <td style="background: #f7dc79;"></td>
            <td style="background: #f7dc79;"></td>
            <td style="background: #f7dc79;"></td>
            <td style="background: #f7dc79;"></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td></td>
            <td></td>
            <td></td>
            <td style="background: #7fc77f;"></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td rowspan="2" style="font-weight: bold; font-size: 10px">Tests en profondeur et corrections des bugs</td>
            <td></td>
            <td></td>
            <td></td>
            <td style="background: #f7dc79;"></td>
            <td style="background: #f7dc79;"></td>
            <td style="background: #f7dc79;"></td>
            <td style="background: #f7dc79;"></td>
            <td style="background: #f7dc79;"></td>
            <td style="background: #f7dc79;"></td>
            <td style="background: #f7dc79;"></td>
            <td style="background: #f7dc79;"></td>
            <td style="background: #f7dc79;"></td>
            <td style="background: #f7dc79;"></td>
            <td style="background: #f7dc79;"></td>
            <td style="background: #f7dc79;"></td>
            <td style="background: #f7dc79;"></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td></td>
            <td></td>
            <td></td>
            <td style="background: #7fc77f;"></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
		<tr>
            <td rowspan="2" style="font-weight: bold; font-size: 10px">Tenir à jour la documentation</td>
            <td style="background: #f7dc79;"></td>
            <td style="background: #f7dc79;"></td>
            <td style="background: #f7dc79;"></td>
            <td style="background: #f7dc79;"></td>
            <td style="background: #f7dc79;"></td>
            <td style="background: #f7dc79;"></td>
            <td style="background: #f7dc79;"></td>
            <td style="background: #f7dc79;"></td>
            <td style="background: #f7dc79;"></td>
            <td style="background: #f7dc79;"></td>
            <td style="background: #f7dc79;"></td>
            <td style="background: #f7dc79;"></td>
            <td style="background: #f7dc79;"></td>
            <td style="background: #f7dc79;"></td>
            <td style="background: #f7dc79;"></td>
            <td style="background: #f7dc79;"></td>
            <td style="background: #f7dc79;"></td>
            <td style="background: #f7dc79;"></td>
            <td style="background: #f7dc79;"></td>
            <td style="background: #f7dc79;"></td>
            <td style="background: #f7dc79;"></td>
            <td></td>
        </tr>
        <tr>
            <td style="background: #7fc77f;"></td>
            <td style="background: #7fc77f;"></td>
            <td style="background: #7fc77f;"></td>
            <td style="background: #7fc77f;"></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td rowspan="2" style="font-weight: bold; font-size: 15px">Résumé du TPI</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td style="background: #f7dc79;"></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td rowspan="2" style="font-weight: bold; font-size: 10px">Finalisation / Impression</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td style="background: #f7dc79;"></td>
            <td style="background: #f7dc79;"></td>
        </tr>
        <tr>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
		<tr>
            <td rowspan="2" style="font-weight: bold; font-size: 10px">Tenue du journal de bord</td>
            <td style="background: #f7dc79;"></td>
            <td style="background: #f7dc79;"></td>
            <td style="background: #f7dc79;"></td>
            <td style="background: #f7dc79;"></td>
            <td style="background: #f7dc79;"></td>
            <td style="background: #f7dc79;"></td>
            <td style="background: #f7dc79;"></td>
            <td style="background: #f7dc79;"></td>
            <td style="background: #f7dc79;"></td>
            <td style="background: #f7dc79;"></td>
            <td style="background: #f7dc79;"></td>
            <td style="background: #f7dc79;"></td>
            <td style="background: #f7dc79;"></td>
            <td style="background: #f7dc79;"></td>
            <td style="background: #f7dc79;"></td>
            <td style="background: #f7dc79;"></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td style="background: #7fc77f;"></td>
            <td style="background: #7fc77f;"></td>
            <td style="background: #7fc77f;"></td>
            <td style="background: #7fc77f;"></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
    </tbody>
</table>
<div style="display: flex;">
    <div style="display: flex; align-items: center; width: 40%">
        <img src="https://i.loli.net/2020/05/25/GLgXIau45ERibwO.png" style="width: 20px; height: 20px; border-radius: 50%; margin-right: 20px">
        Planification prévisionnelle
    </div>
    <div style="display: flex; align-items: center; width: 40%">
        <img src="https://i.loli.net/2020/05/25/kscEVbJ4Wh9xuSv.png" style="width: 20px; height: 20px; border-radius: 50%; margin-right: 20px">
        Planification réelle
    </div>
</div>




