## Table des matière

- [Animanga](#animanga)
  - [Table des versions](#table-des-versions)
  - [Résumé de l'énoncé](#résumé-de-lénoncé)
  - [Organisation](#organisation)
  - [Livrable](#livrable)
  - [Matériel et logicles à disposition](#matériel-et-logicles-à-disposition)
  - [Descriptif complet du projet](#descriptif-complet-du-projet)
    - [Sitemap](#sitemap)
    - [Description succinte du contenu des pages du site](#description-succinte-du-contenu-des-pages-du-site)
  - [Méthodologie](#méthodologie)
    - [1. S’informer](#1-sinformer)
    - [2. Planifier](#2-planifier)
    - [3. Décider](#3-décider)
    - [4. Réaliser](#4-réaliser)
    - [5. Contrôler](#5-contrôler)
    - [6. Évaluer](#6-évaluer)
  - [Planning](#planning)
  - [Implémentation](#implémentation)
    - [Base de données](#base-de-données)
  - [Plans de test et tests](#plans-de-test-et-tests)
    - [Périmètre des tests](#périmètre-des-tests)
    - [Environnement](#environnement)
    - [Scénarios](#scénarios)
    - [Évolution des tests](#évolution-des-tests)

<div style='page-break-after: always; break-after: page; text-align:right;'></div>

## Table des versions

| N° de version | Date       | Auteur                                    | Modifications                           |
| ------------- | ---------- | ----------------------------------------- | --------------------------------------- |
| 0.1           | 2020-25-05 | Tanguy Cavagna \<<tanguy.cvgn@eduge.ch>\> | Création de la base de la documentation |


## Résumé de l'énoncé

*Les informations suivantes sont éxtraites du cahier des charges du TPI.*

## Organisation

| Éléve                                     | Maître d'apprentissage                   | Experts                                                      |
| ----------------------------------------- | ---------------------------------------- | ------------------------------------------------------------ |
| Tanguy Cavagna \<<tanguy.cvgn@eduge.ch>\> | Pascal Bonvin \<<edu-bonvinp@eduge.ch>\> | Nicolas Terrond \<<nicolas.terrond@sig-ge.ch>\><br />Robin Bouille \<<robin.bouille@gmail.com>\> |

## Livrable

<table>
    <thead>
        <tr>
            <th>Pour les experts et le formateur</td>
            <th>Pour le formateur</td>
        </tr>
    </thead>
	<tbody>
        <tr>
            <td>Planning réel détaillé du projet</td>
            <td rowspan="4">Accès au GitHub</td>
        </tr>
        <tr>
            <td>Documentation du projet contenant le code source au format PDF</td>
        </tr>
        <tr>
            <td>Journal de bord</td>
        </tr>
        <tr>
            <td>Résumé du TPI (1 page A4)</td>
        </tr>
	</tbody>
</table>

## Matériel et logicles à disposition

* Un PC standard école, 2 écrans
* Pycharm
* Netbeans
* Suite office
* MySQl, Sqlite3, Flask, connexion internet

## Descriptif complet du projet

Lorsqu’il s’agit de réaliser un site web, la tradition de l’école d’informatique encourage l’utilisation de PHP et Mysql. Dans le cas de ce diplôme, il s’agit de réaliser un site local avec Python Flask et de gérer les données dans une base de données Sqlite3. De plus la base de donnée locale est synchronisée unidirectionnelement avec une base de donnée Mysql sur un serveur distant. L’ambition de ce projet est de démontrer qu’il est possible de créer un application WEB sans passer par l’installation d’un serveur apache et d’une base données Mysql. A noter que le candidat est un élève brillant qui maîtrise le langage Python.

Les données initiales qui permettront de remplir la base de données sont accessibles sur github au format json (https://github.com/manami-project/anime-offline-database). Elles devront être converties et synchronisées dans la base de données locale qui reste à déterminer.

### Sitemap

![](https://i.loli.net/2020/05/25/Ii93wL5DjEHexbY.png)

### Description succinte du contenu des pages du site

* La page index permet d'avoir le champ de recherche, un bouton "aléatoire", ainsi que les favoris de l'utilisateur et son flux d'activité si connecter.
* La page à propos contient toutes les informations concernant le site ainsi que les librairies utilisées.
* La page connexion permet simplement de se connecter.
* La page inscription, de s'inscrire.
* La page anime / manga permet de voir les informations / actions sur un anime / manga sélectionner (rediriger sur cette page lorsque l'on clique sur un anime / manga sur la page index après une recherche).
* La page aide contient l'aide du site.
* La page profil contient les information de l'utilisateur ainsi que les listes personnelles, dans lesquelles des animes / manga peuvent être ajoutés, ainsi que leur contenu.
* La page favoris permet de modifier l'ordre des animes / manga mit en favoris ainsi que de les retirer de la liste des favoris.
* La page liste contient un CRUD sur les listes personnelles de l'utilisateur.


## Méthodologie

Pour pouvoir planifier correctement ce projet, j'ai décidé d'utilisé la méthode en 6 étapes, décrite ci-dessous :

![Méthode en 6 étapes](https://i.imgur.com/Zi6VG92.png)

### 1. S’informer

La première étape est utile pour pouvoir comprendre le projet dans son ensemble et comprendre toutes les fonctionnalisées nécessaires. Il est aussi indispensable de demander d’éclaircir tous les points flous de l’énoncé.

### 2. Planifier

Le fait de planifier le projet permet de séparer les tâches et de définir des priorités. ses dernières sont les suivantes : 🚫 *Bloquant*, 💥 *Critique*, ❗ *Important*, ❓ *Secondaire*.

Pour représenter le planning nous avons utilisé un diagramme de Gantt. Ce type de diagramme permet de visualiser très correctement la progression quotidienne ainsi que les différences entre les prévisions et le réel.

### 3. Décider

Cette partie nous permet de pouvoir se lancer dans la réalisation du projet. S’il nous reste des points en suspens, c’est le moment de prendre une décision et de se jeter à l’eau une bonne fois pour toute.  

### 4. Réaliser

Nous pouvons enfin nous lancer dans l’implémentation de toutes les fonctionnalités à développer ainsi que la rédaction de la documentation.

### 5. Contrôler

Pour valider cette étape, nous avons tester chacune des fonctionnalités indépendamment des autres pour correctement vérifier leur fonctionnement dans différents cas d’usage.

Une fois l’application terminée, nous avons pu tester son bon fonctionnement sur plusieurs navigateurs différents pour bien être sûre que tout fonctionne comme prévu dans n’importe quel cas d’utilisation.

### 6. Évaluer

Une fois toutes les étapes précédentes achevées, nous avons pu nous lancer dans ce qui peut sembler le plus complexe. Nous avons fait une rétrospective de tout ce que nous avons fait avec un regard critique afin de chercher des points sur lesquels nous pourront nous améliorer par la suite. Pour ce faire, nous avons une section dédiée dans le journal de bord répertoriant les problèmes rencontré ainsi que les solutions trouvées pour ces derniers. Une conclusion est aussi présente à la fin de ce rapport servant de bilan final au projet.





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

| Nom                            | S13 : Synchronisation MySQL Sqlite3                          |
| ------------------------------ | ------------------------------------------------------------ |
| **Description (*user story*)** | En tant que développeur, je dois pouvoir synchroniser les bases MySQL et Sqlite3 unidirectionellement pour créer un backup sur serveur distant. |
| **Critère d'acceptation**      | ***Pas encore écris de tests***                              |
| **Priorité**                   | ❓ Secondaire                                                 |

## Planning

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
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
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
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
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
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
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
            <td rowspan="2" style="font-weight: bold; font-size: 15px">S1 : Inscription à AniHome</td>
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
            <td rowspan="2" style="font-weight: bold; font-size: 15px">S2 : Connexion à AniHome</td>
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
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
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
            <td rowspan="2" style="font-weight: bold; font-size: 15px">S13 : Synchronisation MySQL Sqlite3</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
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
        </tr><tr>
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
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
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
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
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
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
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

## Implémentation

### Base de données
## Plans de test et tests

### Périmètre des tests

Pour *Animanga* j'ai mis en place un protocole de test afin que n'importe quel utilisateur puisse naviguer convenablement dans l'application, peu importe son navigateur WEB.

### Environnement

Lors de ces tests, j'ai utilisé les navigateurs suivants :

* Mozilla Firefox 76.0.1 (64 bits) sur Windows 10 Entreprise 1903
* Google Chrome 81.0.4044.138 (64 bits) sur Windows 10 Entreprise 1903
* Microsoft Edge Version 81.0.416.72 (64 bits) sur Windows 10 Entreprise 1903

### Scénarios

Les scénarios des tests sont détaillés afin que n'importe quelles personne puisse les exécuter. Pour rédiger mes scénarios j'ai utilisé la syntaxe [**Gherkin**](https://cucumber.io/docs/gherkin/).

| __Nom__               | __1.1__ Création d'un nouveau compte                         |
| :-------------------- | :----------------------------------------------------------- |
| __User Story__        | S1 : Inscription à AniHome                                   |
| __Situation__         | **Étant donné que** je suis un nouvel utilisateur de AniHome, je ne possède pas encore de compte. <br>**Quand** je clique sur le bouton *Inscription*, je suis redirigé vers la page d'inscription et je rempli les informations demandées. <br>**Alors**, je suis redirigé sur la page d'accueil avec mon nouveau compte connecté. |
| __Résultats obtenus__ | Je clique sur *Inscription*. Je suis redirigé vers la page d'inscription. Je remplie le formulaire avec des informations valides. Je clique sur *Inscription*. Je suis redirigé vers la page d'accueil avec mon nouveau compte connecté. |
| __Statut__            | ❌ KO                                                         |

| **Nom**               | **1.2** Création d'un nouveau compte (avec erreurs)          |
| :-------------------- | :----------------------------------------------------------- |
| **User Story**        | S1 : Inscription à AniHome                                   |
| **Situation**         | **Étant donné que** je suis un nouvel utilisateur de AniHome, je ne possède pas encore de compte.  <br>**Quand** je clique sur le bouton *Inscription*, je suis redirigé vers la page d'inscription et je rempli le formulaire avec des informations erronées.  <br>**Alors**, le formulaire est rechargé avec un message d'erreur indiquant ce qu'il ne c'est pas bien passé. |
| **Résultats obtenus** | Je clique sur *Inscription*. Je suis redirigé vers la page d'inscription. Je remplie le formulaire avec un email invalide. Je clique sur *Inscription*. Un message s'affiche m'indiquant que l'email fourni n'est pas correct. |
| **Statut**            | ❌ KO                                                         |

| **Nom**               | 2.1 Connexion avec un compte existant                        |
| :-------------------- | :----------------------------------------------------------- |
| **User Story**        | S2 : Connexion à AniHome                                     |
| **Situation**         | **Étant donné que** je suis un utilisateur de AniHome, j'ai déjà un compte à disposition. <br>**Quand** je clique sur le bouton *Connexion*, je suis redirigé vers la page de connexion et je rempli les informations demandées. <br>**Alors**, je suis redirigé sur la page d'accueil avec mon compte connecté. |
| **Résultats obtenus** | Je clique sur *Connexion*. Je suis redirigé vers la page d'inscription. Je remplie le formulaire avec des informations valides. Je clique sur *Connexion*. Je suis redirigé vers la page d'accueil avec mon nouveau compte connecté. |
| **Statut**            | ❌ KO                                                         |

| **Nom**               | **2.2 Déconnexion**                                          |
| :-------------------- | :----------------------------------------------------------- |
| **User Story**        | S2 : Connexion à AniHome                                     |
| **Situation**         | **Étant donné que** je suis un utilisateur connecté au site.<br>**Quand** je clique sur le bouton *Déconnexion* placé dans le dropdown du menu *Utilisateur*.<br>**Alors**, je deviens un utilisateur non connecté et je suis redirigé sur la page de connexion. |
| **Résultats obtenus** | Je clique sur *Utilisateur* et *Déconnexion*. Je ne suis plus connecté et je suis revenue sur la page de connexion. |
| **Statut**            | ❌ KO                                                         |

| **Nom**               | 3.1 Importation des animes                                   |
| :-------------------- | :----------------------------------------------------------- |
| **User Story**        | S3 : Importation des animes                                  |
| **Situation**         | **Étant donné que** je suis un utilisateur connecté au site. <br />**Quand** je clique sur le bouton *Écraser tous les animes* placé dans le dropdown du menu *Utilisateur*.<br />**Alors**, j'écrase toutes les données du site relatives aux animes. Cela comprend les animes en eux même, les favoris ainsi que les animes contenu dans les listes. |
| **Résultats obtenus** | Je clique sur *Utilisateur* et *Écraser tous les animes*. Je suis redirigé vers la page d'accueil et des alertes s'affiche en haut au centre de l'écran indiquant l'état de la mise à jours des animes. |
| **Statut**            | ❌ KO                                                         |

| **Nom**               | 4.1 Recherche des animes                                     |
| :-------------------- | :----------------------------------------------------------- |
| **User Story**        | S4 : Recherche des animes                                    |
| **Situation**         | **Étant donné que** je suis un utilisateur connecté au site. <br />**Quand** je clique sur le bouton 🔍 placé dans la barre de navigation et que j'écris "k On" dans le champs de recherche de la modale.<br />**Alors**, je suis redirigé vers la page d'accueil et les résultats de la recherche affiche l'anime "K-ON!". |
| **Résultats obtenus** | L'anime "K-ON!" est présent dans la zone de résultat de recherche. |
| **Statut**            | ❌ KO                                                         |

| **Nom**               | 4.2 Recherche des animes avec raccourcis                     |
| :-------------------- | :----------------------------------------------------------- |
| **User Story**        | S4 : Recherche des animes                                    |
| **Situation**         | **Étant donné que** je suis un utilisateur connecté au site. <br />**Quand** je fais le raccourcis clavier <kbd>Ctrl</kbd> + <kbd>S</kbd> et que j'écris "k On" dans le champs de recherche de la modale.<br />**Alors**, je suis redirigé vers la page d'accueil et les résultats de la recherche affiche l'anime "K-ON!". |
| **Résultats obtenus** | L'anime "K-ON!" est présent dans la zone de résultat de recherche. |
| **Statut**            | ❌ KO                                                         |

| **Nom**               | 5.1 Affichage de la carte de l'anime                         |
| :-------------------- | :----------------------------------------------------------- |
| **User Story**        | S5 : Affichage de la carte de l'anime                        |
| **Situation**         | **Étant donné que** je suis un utilisateur connecté au site sur la page d'accueil ayant fait une recherche. <br />**Quand** je clique sur le titre d'un anime présent dans la zone de résultat de la recherche.<br />**Alors**, une modale s'affiche contenant l'image de couverture, le titre, le statut de visionnement de l'anime, et les listes personnelles de l'utilisateur. |
| **Résultats obtenus** | La modale s'affiche avec le contenu adéquat.                 |
| **Statut**            | ❌ KO                                                         |

| **Nom**               | 6.1 Mise à jour du statut de l'anime sélectionné             |
| :-------------------- | :----------------------------------------------------------- |
| **User Story**        | S6 : Mise à jour de l'anime                                  |
| **Situation**         | **Étant donné que** je suis un utilisateur connecté au site sur la page d'accueil ayant fait une recherche et ayant ouvert la modale d'informations d'un anime. <br />**Quand** sélectionne un statut autre que "---".<br />**Alors**, le combo-box se met à jour avec la nouvelle valeur sélectionnée. |
| **Résultats obtenus** | La valeur du combo-box c'est bien mise à jour.               |
| **Statut**            | ❌ KO                                                         |

| **Nom**               | 6.2 Ajout de l'anime dans une liste personnelle              |
| :-------------------- | :----------------------------------------------------------- |
| **User Story**        | S6 : Mise à jour de l'anime                                  |
| **Situation**         | **Étant donné que** je suis un utilisateur connecté au site sur la page d'accueil ayant fait une recherche et ayant ouvert la modale d'informations d'un anime. <br />**Quand** je clique sur une check-box blanche d'une des listes personnelles.<br />**Alors**, l'état de la check-box ce met à jour et elle se colore en bleu. L'anime est maintenant présent dans la liste personnelle. |
| **Résultats obtenus** | L'état de la check-box c'est bien mis à jour et est bien coloré en bleu. |
| **Statut**            | ❌ KO                                                         |

| **Nom**               | 6.3 Ajout de l'anime dans les favoris                        |
| :-------------------- | :----------------------------------------------------------- |
| **User Story**        | S6 : Mise à jour de l'anime                                  |
| **Situation**         | **Étant donné que** je suis un utilisateur connecté au site sur la page d'accueil ayant fait une recherche et ayant ouvert la modale d'informations d'un anime. <br />**Quand** je clique sur le cœur blanc pour ajouté au favoris.<br />**Alors**, le cœur se colore et l'anime se rajoute dans la zone des favoris de la page d'accueil. |
| **Résultats obtenus** | Le cœur c'est coloré et l'anime c'est correctement ajouté dans la zone des favoris de la page d'accueil. |
| **Statut**            | ❌ KO                                                         |

| **Nom**               | 6.4 Suppression du statut de l'anime                         |
| :-------------------- | :----------------------------------------------------------- |
| **User Story**        | S6 : Mise à jour de l'anime                                  |
| **Situation**         | **Étant donné que** je suis un utilisateur connecté au site sur la page d'accueil ayant fait une recherche et ayant ouvert la modale d'informations d'un anime.<br />**Quand** sélectionne le statut "---".<br />**Alors**, le combo-box se met à jour avec la nouvelle valeur sélectionnée et l'anime n'est plus présent dans aucun autre statut. |
| **Résultats obtenus** | La valeur du combo-box c'est bien mise à jour et l'anime n'est effectivement plus présent dans les autres statuts. |
| **Statut**            | ❌ KO                                                         |

### Évolution des tests

| N° Test | J1<br /><span style="font-weight: normal">lu.25</span> | J2<br /><span style="font-weight: normal">ma.26</span> | J3<br /><span style="font-weight: normal">me.27</span> | J4<br /><span style="font-weight: normal">je.28</span> | J5<br /><span style="font-weight: normal">ve.29</span> | J6<br /><span style="font-weight: normal">ma.2</span> | J7<br /><span style="font-weight: normal">me.3</span> | J8<br /><span style="font-weight: normal">je.4</span> | J9<br /><span style="font-weight: normal">ve.5</span> | J10<br /><span style="font-weight: normal">lu.8</span> | J11<br /><span style="font-weight: normal">ma.9</span> |
| :-----: | :----------------------------------------------------: | :----------------------------------------------------: | :----------------------------------------------------: | :----------------------------------------------------: | :----------------------------------------------------: | :---------------------------------------------------: | :---------------------------------------------------: | :---------------------------------------------------: | :---------------------------------------------------: | :----------------------------------------------------: | :----------------------------------------------------: |
|   1.1   |                           ❌                            |                           ❌                            |                           ❌                            |                           ❌                            |                           ❌                            |                           ❌                           |                           ❌                           |                           ❌                           |                           ❌                           |                           ❌                            |                           ❌                            |
|   1.2   |                           ❌                            |                           ❌                            |                           ❌                            |                           ❌                            |                           ❌                            |                           ❌                           |                           ❌                           |                           ❌                           |                           ❌                           |                           ❌                            |                           ❌                            |
|   2.1   |                           ❌                            |                           ❌                            |                           ❌                            |                           ❌                            |                           ❌                            |                           ❌                           |                           ❌                           |                           ❌                           |                           ❌                           |                           ❌                            |                           ❌                            |
|   2.2   |                           ❌                            |                           ❌                            |                           ❌                            |                           ❌                            |                           ❌                            |                           ❌                           |                           ❌                           |                           ❌                           |                           ❌                           |                           ❌                            |                           ❌                            |
|   3.1   |                           ❌                            |                           ❌                            |                           ❌                            |                           ❌                            |                           ❌                            |                           ❌                           |                           ❌                           |                           ❌                           |                           ❌                           |                           ❌                            |                           ❌                            |
|   4.1   |                           ❌                            |                           ❌                            |                           ❌                            |                           ❌                            |                           ❌                            |                           ❌                           |                           ❌                           |                           ❌                           |                           ❌                           |                           ❌                            |                           ❌                            |
|   4.2   |                           ❌                            |                           ❌                            |                           ❌                            |                           ❌                            |                           ❌                            |                           ❌                           |                           ❌                           |                           ❌                           |                           ❌                           |                           ❌                            |                           ❌                            |
|   5.1   |                           ❌                            |                           ❌                            |                           ❌                            |                           ❌                            |                           ❌                            |                           ❌                           |                           ❌                           |                           ❌                           |                           ❌                           |                           ❌                            |                           ❌                            |
|   6.1   |                           ❌                            |                           ❌                            |                           ❌                            |                           ❌                            |                           ❌                            |                           ❌                           |                           ❌                           |                           ❌                           |                           ❌                           |                           ❌                            |                           ❌                            |
|   6.2   |                           ❌                            |                           ❌                            |                           ❌                            |                           ❌                            |                           ❌                            |                           ❌                           |                           ❌                           |                           ❌                           |                           ❌                           |                           ❌                            |                           ❌                            |
|   6.3   |                           ❌                            |                           ❌                            |                           ❌                            |                           ❌                            |                           ❌                            |                           ❌                           |                           ❌                           |                           ❌                           |                           ❌                           |                           ❌                            |                           ❌                            |
|   6.4   |                           ❌                            |                           ❌                            |                           ❌                            |                           ❌                            |                           ❌                            |                           ❌                           |                           ❌                           |                           ❌                           |                           ❌                           |                           ❌                            |                           ❌                            |