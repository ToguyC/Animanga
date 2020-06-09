## Table des matière

- [Animanga](#animanga)
  - [Table des versions](#table-des-versions)
  - [Préambule](#préambule)
  - [Introduction](#introduction)
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
  - [Planification](#planification)
    - [Product backlog](#product-backlog)
    - [Diagramme de Gantt](#diagramme-de-gantt)
  - [Implémentation](#implémentation)
    - [Base de données](#base-de-données)
    - [Structure](#structure)
    - [Classes (Python)](#classes-python)
    - [API interne](#api-interne)
  - [Librairies et outils externes](#librairies-et-outils-externes)
    - [Pip et NPM](#pip-et-npm)
    - [Flask](#flask)
    - [Jinja](#jinja)
    - [Flask-Login](#flask-login)
    - [Flask-Swagger](#flask-swagger)
    - [MySQL Connector/Python](#mysql-connectorpython)
    - [SASS](#sass)
    - [Swagger](#swagger)
    - [jQuery UI](#jquery-ui)
    - [ESLint](#eslint)
    - [Pylint](#pylint)
    - [Git](#git)
  - [Analyse des fonctionnalités majeurs](#analyse-des-fonctionnalités-majeurs)
    - [Un CRUD complet permet de gérer une entrée manga de la bibliothèque](#un-crud-complet-permet-de-gérer-une-entrée-manga-de-la-bibliothèque)
    - [La base de données locale sqlite3 est synchronisée de façon unidirectionnelle avec la base de données d'un serveur mysql](#la-base-de-données-locale-sqlite3-est-synchronisée-de-façon-unidirectionnelle-avec-la-base-de-données-dun-serveur-mysql)
    - [Les données JSON de github sont importées dans la base de données locale](#les-données-json-de-github-sont-importées-dans-la-base-de-données-locale)
    - [Le service http utilise Python Flask](#le-service-http-utilise-python-flask)
    - [Le planning réel est documenté et comparé au planning prescrit](#le-planning-réel-est-documenté-et-comparé-au-planning-prescrit)
    - [Le projet est publié sur github et une url est communiqué](#le-projet-est-publié-sur-github-et-une-url-est-communiqué)
    - [Le projet Python contient au moins une classe (python objet) conçu par le candidat](#le-projet-python-contient-au-moins-une-classe-python-objet-conçu-par-le-candidat)
  - [Plans de test et tests](#plans-de-test-et-tests)
    - [Périmètre des tests](#périmètre-des-tests)
    - [Environnement](#environnement)
    - [Scénarios](#scénarios)
    - [Évolution des tests](#évolution-des-tests)
  - [Bibliographie](#bibliographie)
  - [Glossaire](#glossaire)
  - [Conclusion](#conclusion)
    - [Difficultés majeures rencontrées](#difficultés-majeures-rencontrées)
    - [Améliorations possibles](#améliorations-possibles)
    - [Bilan personnel](#bilan-personnel)
    - [Remerciements](#remerciements)

<div style='page-break-after: always; break-after: page; text-align:right;'></div>

## Table des versions

| N° de version | Date       | Auteur                                  | Modifications                             |
| ------------- | ---------- | --------------------------------------- | ----------------------------------------- |
| 1.0           | 2020-06-09 | Tanguy Cavagna <<tanguy.cvgn@eduge.ch>> | Version finale de la documentation du TPI |

## Préambule

Toute cette documentation a été rédigée en [Markdown](https://www.markdownguide.org/). PDF que vous avez entre les mains est généré automatiquement grâce au logiciel d'édition pour fichier Markdown : [Typora](https://typora.io). J'ai fait un script Bash servant à fusionner les différents fichiers PDF nécessaires à la composition finale de ce rapport. Par conséquent, il se peut que la mise en page soit quelque peu bancale. C'est pourquoi je vous invite chaleureusement à lire tout ce rapport sur le site <https://animanga.readthedocs.io/fr/latest/>. De plus, mon TPI est hébergé sur un serveur accessible à l'adresse <https://flask.tcsandbox.ch>.

## Introduction

Ce projet a été réalisé dans le cadre du *Travail Pratique Individuel* (TPI) durant la session de mai - juin 2020. Il a pour but de valider les compétences acquises tout au long de la formation *Informaticien CFC* de l'école du CFPT-Informatique au Petit-Lancy.

Animanga est une application web, écrite en Python, permettant aux utilisateurs de faire leur propre bibliothèque d'anime. Pour ce faire, l'utilisateur a la possibilité de créer ses propres listes afin de correctement organiser sa bibliothèque, mettre des animes en tant que favoris, et rechercher les animes qu'il voudrait ajouter à sa collection directement depuis cette application.
## Résumé de l'énoncé

*Les informations suivantes sont éxtraites du cahier des charges du TPI.*

## Organisation

| Éléve                                         | Maître d'apprentissage                   | Experts                                                      |
| --------------------------------------------- | ---------------------------------------- | ------------------------------------------------------------ |
| Tanguy Cavagna<br /><<tanguy.cvgn@eduge.ch>\> | Pascal Bonvin \<<edu-bonvinp@eduge.ch>\> | Nicolas Terrond \<<nicolas.terrond@sig-ge.ch>\><br />Robin Bouille \<<robin.bouille@gmail.com>\> |

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

Pour pouvoir planifier correctement ce projet, j'ai décidé d'utiliser la méthode en 6 étapes, décrite ci-dessous :

![Méthode en 6 étapes](https://i.imgur.com/Zi6VG92.png)

### 1. S’informer

La première étape est utile non seulement pour comprendre le projet dans son ensemble mais également pour se rendre compte de toutes les fonctionnalités nécessaires. Elle permet aussi d’éclaircir tous les points flous de l’énoncé.

### 2. Planifier

Le fait de planifier le projet permet de séparer les tâches, de lister et de définir les priorités. Ses dernières sont les suivantes : 🚫 *Bloquant*, 💥 *Critique*, ❗ *Important*, ❓ *Secondaire*.

Pour représenter le planning, j'ai choisi d'utiliser un diagramme de Gantt. Ce type d'outil de gestion permet de visualiser très correctement la progression quotidienne du projet ainsi que les différences entre ce qui a été prévu et la réalité.

### 3. Décider

S’il reste des points en suspens, c’est le dernier moment pour prendre des décisions (les éclaircir, les laisser de côté, les remettre à plus tard, etc.) afin de pouvoir ensuite "se jeter à l'eau" !  

### 4. Réaliser

Cette partie permet de commencer le projet en tant que tel : implémenter toutes les fonctionnalités à développer et rédiger la documentation.

### 5. Contrôler

Cette étape invite à tester chacune des fonctionnalités indépendamment les unes des autres pour vérifier leur fonctionnement dans différents cas d'usage.

Une fois l'application terminée, il s'agit de tester son bon fonctionnement sur plusieurs navigateurs différents pour bien être certain que tout se déroule comme prévu dans l'import que cas d'utilisation.

### 6. Évaluer

Une fois toutes les étapes précédentes achevées, il s'agit de se lancer dans ce qui peut sembler le plus complexe ; une rétrospective de tout ce qui a été fait avec un regard critique afin de déceler les points à améliorer par la suite.

Pour ce faire, une section est prévue dans le rapport final dans laquelle sont répertoriés les problèmes rencontrés ainsi que les solutions trouvées pour ces derniers.

Pour que je puisse avoir une évaluation complète du projet, le rapport final se termine par une conclusion qui sert de bilan final au projet.

## Planification

### Product backlog


| Nom                            | S1 : Inscription à Animanga                                  |
| ------------------------------ | ------------------------------------------------------------ |
| **Description (*user story*)** | En tant qu'utilisateur non connecté, je peux me créer un compte afin de pouvoir accéder au site. |
| **Critère d'acceptation**      | Les tests *1.1* et *1.10* passent.                           |
| **Priorité**                   | 🚫 Bloquant                                                   |

| Nom                            | S2 : Connexion à Animanga                                    |
| ------------------------------ | ------------------------------------------------------------ |
| **Description (*user story*)** | En tant qu'utilisateur non connecté, je peux me connecter afin de pouvoir accéder au site. |
| **Critère d'acceptation**      | Les tests *2.1* et *2.6* passent.                            |
| **Priorité**                   | 🚫 Bloquant                                                   |

| Nom                            | S3 : Importation des animes                                  |
| ------------------------------ | ------------------------------------------------------------ |
| **Description (*user story*)** | En tant qu'utilisateur connecté, je peux écraser les animes avec un nouveau set de données. |
| **Critère d'acceptation**      | Le test *3.1* passe.                                         |
| **Priorité**                   | 💥 Critique                                                   |

| Nom                            | S4 : Rechercher des animes                                   |
| ------------------------------ | ------------------------------------------------------------ |
| **Description (*user story*)** | En tant qu'utilisateur connecté, je peux effectué une recherche afin d'ajouter des animes dans mes listes personnelles ou de les mettre en tant que *favoris*. |
| **Critère d'acceptation**      | Les tests *4.1* et *4.2* passent.                            |
| **Priorité**                   | 💥 Critique                                                   |

| Nom                            | S5 : Affichage de la carte d'un anime                        |
| ------------------------------ | ------------------------------------------------------------ |
| **Description (*user story*)** | En tant qu'utilisateur connecté, je peux cliquer sur le titre d'un anime présent dans les résultats de ma précédente recherche afin d'accéder à ses informations. |
| **Critère d'acceptation**      | Le test *5.1* passe.                                         |
| **Priorité**                   | ❗ Important                                                  |

| Nom                            | S6 : Mise à jour d'un anime                                  |
| ------------------------------ | ------------------------------------------------------------ |
| **Description (*user story*)** | En tant qu'utilisateur connecté, je peux mettre à jour le statut, l'appartenance à une liste personnel ainsi que le statut de favoris d'un anime. |
| **Critère d'acceptation**      | Les tests *6.1* à *6.6* passent.                             |
| **Priorité**                   | ❗ Important                                                  |

| Nom                            | S7 : Affichage du profile                                    |
| ------------------------------ | ------------------------------------------------------------ |
| **Description (*user story*)** | En tant qu'utilisateur connecté, je peux avoir accès à ma page de profile afin de pourvoir voir les statistiques et favoris. Il est également possible de voir la page de profile d'autre utilisateur du site. |
| **Critère d'acceptation**      | Le test *7.1* passe.                                         |
| **Priorité**                   | ❗ Important                                                  |

| Nom                            | S8 : Affichage des listes                                    |
| ------------------------------ | ------------------------------------------------------------ |
| **Description (*user story*)** | En tant qu'utilisateur connecté, je peux avoir accès à ma page de listes afin de voir toutes mes listes et leur contenu. Il est également possible de voir les listes d'autre utilisateur du site. |
| **Critère d'acceptation**      | Le test *8.1* passe.                                         |
| **Priorité**                   | ❗ Important                                                  |

| Nom                            | S9 : Gestion des listes                                      |
| ------------------------------ | ------------------------------------------------------------ |
| **Description (*user story*)** | En tant qu'utilisateur connecté, je peux gérer mes propres listes pour en ajouter, en supprimer, ou modifier leur nom. |
| **Critère d'acceptation**      | Les tests *9.1* et *9.2* passent.                            |
| **Priorité**                   | ❗ Important                                                  |

| Nom                            | S10 : Affichage des favoris                                  |
| ------------------------------ | ------------------------------------------------------------ |
| **Description (*user story*)** | En tant qu'utilisateur connecté, je peux avoir accès à ma page favoris afin de voir tout mes favoris. Il est également possible de voir les favoris d'autre utilisateur du site. |
| **Critère d'acceptation**      | Les test *10.1* et *10.2* passent.                           |
| **Priorité**                   | ❗ Important                                                  |

| Nom                            | S11 : Gestion des favoris                                    |
| ------------------------------ | ------------------------------------------------------------ |
| **Description (*user story*)** | En tant qu'utilisateur connecté, je peux organiser l'ordre de mes favoris selon mes envies. |
| **Critère d'acceptation**      | Les tests *11.1* et *11.2* passent.                          |
| **Priorité**                   | ❗ Important                                                  |

| Nom                            | S12 : Affichage de la *landing page*                         |
| ------------------------------ | ------------------------------------------------------------ |
| **Description (*user story*)** | En tant qu'utilisateur non connecté, je n'ai ni accès aux animes ni aux listes. La barre de navigation m'affiche un lien pour me connecter et un autre pour m'inscrire. |
| **Critère d'acceptation**      | Le test *12.1* passe.                                        |
| **Priorité**                   | ❓ Secondaire                                                 |

| Nom                            | S13 : Utilisation d'un git                                   |
| ------------------------------ | ------------------------------------------------------------ |
| **Description (*user story*)** | En tant que développeur, je dois pouvoir faire du versionnage de code source et pouvoir accéder à un dépôt distant Github. |
| **Critère d'acceptation**      | Le dépôt git local est configurer correctement et le lien sur le dépôt distant à été bien fait. |
| **Priorité**                   | 🚫 Bloquant                                                   |

| Nom                            | S14 : Configuration de la base de données                    |
| ------------------------------ | ------------------------------------------------------------ |
| **Description (*user story*)** | En tant que développeur, je dois pouvoir utilisé une base de données Sqlite3 et MySQL ayant un modèle identique à celui donné dans l'énoncé. Pour ce faire, j'ai une classe Python me permettant de faire des requêtes sur la base Sqlite3 et une autre classe me permettant de faire des requêtes sur la base MySQL. J'ai aussi un dump de la structure de la base MySQL dans les fichiers statiques de mon application. |
| **Critère d'acceptation**      | Les tables `animes`, `status`, `type`, `url`, `list`, `user`, `list_has_anime`, `user_has_list` et `user_has_favorites` ont bien été crées et sont utilisable par les contrôleurs dédiés. |
| **Priorité**                   | 🚫 Bloquant                                                   |

| Nom                            | S15 : Synchronisation MySQL Sqlite3                          |
| ------------------------------ | ------------------------------------------------------------ |
| **Description (*user story*)** | En tant que développeur, je dois pouvoir synchroniser les bases MySQL et Sqlite3 unidirectionellement pour créer un backup sur serveur distant. |
| **Critère d'acceptation**      | Le test *14.1* passe.                                        |
| **Priorité**                   | ❓ Secondaire                                                 |

| Nom                            | S16 : Configuration Flask                                    |
| ------------------------------ | ------------------------------------------------------------ |
| **Description (*user story*)** | En tant que développeur, je dois configurer l'application Flask afin d'avoir un site hébergé en local et pouvoir communiquer avec la base de données Sqlite3. |
| **Critère d'acceptation**      | Une page web s'affiche sur l'url `localhost:5000`.           |
| **Priorité**                   | 🚫 Bloquant                                                   |

| Nom                            | S17: Vérifications syntaxique                                |
| ------------------------------ | ------------------------------------------------------------ |
| **Description (*user story*)** | En tant que développeur, je peux lancé la commande `npm run lint` pour vérifier la syntaxe, basé sur le preset Airbnb, des fichiers JavaScript, et la commande `python3 -m pylint --output-format=colorized` pour vérifier la syntaxe des fichiers Python, basé sur les conventions PEP8. |
| **Critère d'acceptation**      | Les test *12.1* et *12.2* passent.                           |
| **Priorité**                   | 🚫 Bloquant                                                   |

| Nom                            | S18: Affichage des activités                                 |
| ------------------------------ | ------------------------------------------------------------ |
| **Description (*user story*)** | En tant qu'utilisateur connecté, je vois mon fil d'actualité contenant le temps écoulé depuis l'ajout d'un favoris et l'ajout d'un anime dans une liste. |
| **Critère d'acceptation**      | Le test *15.1* passe.                                        |
| **Priorité**                   | ❓ Secondaire                                                 |

### Diagramme de Gantt

<table>
    <thead>
        <tr>
            <th>Jour</th>
            <th colspan="2" style="text-align: center">J1<br><span>lu.25</span></th>
            <th colspan="2" style="text-align: center">J2<br><span>ma.26</span></th>
            <th colspan="2" style="text-align: center">J3<br><span>me.27</span></th>
            <th colspan="2" style="text-align: center">J4<br><span>je.28</span></th>
            <th colspan="2" style="text-align: center">J5<br><span>ve.29</span></th>
            <th colspan="2" style="text-align: center">J6<br><span>ma.2</span></th>
            <th colspan="2" style="text-align: center">J7<br><span>me.3</span></th>
            <th colspan="2" style="text-align: center">J8<br><span>je.4</span></th>
            <th colspan="2" style="text-align: center">J9<br><span>ve.5</span></th>
            <th colspan="2" style="text-align: center">J10<br><span>lu.8</span></th>
            <th colspan="2" style="text-align: center">J11<br><span>ma.9</span></th>
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
            <td style="background: #F34C56;"></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
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
            <td rowspan="2" style="font-weight: bold; font-size: 15px">S13 : Utilisation d'un git</td>
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
            <td rowspan="2" style="font-weight: bold; font-size: 15px">S14 : Configuration de la base de données</td>
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
            <td rowspan="2" style="font-weight: bold; font-size: 15px">S16 : Configuration de Flask</td>
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
        </tr>
		<tr>
            <td rowspan="2" style="font-weight: bold; font-size: 15px">S12 : Affichage de la landing page</td>
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
            <td style="background: #F34C56;"></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
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
            <td style="background: #F34C56;"></td>
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
        </tr>
        <tr>
            <td rowspan="2" style="font-weight: bold; font-size: 15px">S10 : Affichage des favoris</td>
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
            <td style="background: #F34C56;"></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
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
            <td style="background: #7fc77f;"></td>
            <td style="background: #F34C56;"></td>
            <td></td>
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
            <td rowspan="2" style="font-weight: bold; font-size: 15px">S11 : Organisation des favoris</td>
            <td></td>
            <td></td>
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
        </tr>
        <tr>
            <td rowspan="2" style="font-weight: bold; font-size: 15px">S18 : Affichage des activités</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
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
            <td style="background: #F34C56;"></td>
            <td></td>
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
            <td rowspan="2" style="font-weight: bold; font-size: 15px">S15 : Synchronisation MySQL Sqlite3</td>
            <td></td>
            <td></td>
            <td></td>
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
        </tr>
        <tr>
            <td rowspan="2" style="font-weight: bold;">S17 : Vérifications syntaxique</td>
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
            <td style="background: #7fc77f;"></td>
            <td style="background: #7fc77f;"></td>
            <td style="background: #7fc77f;"></td>
            <td style="background: #7fc77f;"></td>
            <td style="background: #7fc77f;"></td>
            <td style="background: #7fc77f;"></td>
            <td style="background: #7fc77f;"></td>
            <td style="background: #7fc77f;"></td>
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
            <td style="background: #7fc77f;"></td>
            <td style="background: #7fc77f;"></td>
            <td style="background: #7fc77f;"></td>
            <td style="background: #7fc77f;"></td>
            <td style="background: #7fc77f;"></td>
            <td style="background: #7fc77f;"></td>
            <td style="background: #7fc77f;"></td>
            <td style="background: #7fc77f;"></td>
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
            <td style="background: #7fc77f;"></td>
            <td style="background: #7fc77f;"></td>
            <td style="background: #7fc77f;"></td>
            <td style="background: #7fc77f;"></td>
            <td style="background: #7fc77f;"></td>
            <td style="background: #7fc77f;"></td>
            <td style="background: #7fc77f;"></td>
            <td style="background: #7fc77f;"></td>
            <td style="background: #7fc77f;"></td>
            <td style="background: #7fc77f;"></td>
            <td style="background: #7fc77f;"></td>
            <td style="background: #7fc77f;"></td>
            <td style="background: #7fc77f;"></td>
            <td style="background: #7fc77f;"></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td rowspan="2" style="font-weight: bold; font-size: 15px">Résumé </br>du TPI</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
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
            <td rowspan="2" style="font-weight: bold;">Finalisation / Impression</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
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
            <td rowspan="2" style="font-weight: bold;">Tenue du journal de bord</td>
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
            <td style="background: #7fc77f;"></td>
            <td style="background: #7fc77f;"></td>
            <td style="background: #7fc77f;"></td>
            <td style="background: #7fc77f;"></td>
            <td style="background: #7fc77f;"></td>
            <td style="background: #7fc77f;"></td>
            <td style="background: #7fc77f;"></td>
            <td style="background: #7fc77f;"></td>
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
    <div style="display: flex; align-items: center; width: 40%">
        <img src="https://i.imgur.com/LUikyEA.png" style="width: 20px; height: 20px; border-radius: 50%; margin-right: 20px">
        Planification imprévue
    </div>
</div>









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
## Librairies et outils externes

### Pip et NPM

<img style="float: right; margin-left: 25px; width: 30%" src="https://i.imgur.com/Z4wYwdB.png">[Pip](https://pypi.org/project/pip/) et [NPM](https://www.npmjs.com/) sont deux gestionnaires de dépendances que j'ai utilisés pour mon TPI. Pip est le gestionnaire des dépendances Python tandis que NPM est sont équivalent pour JavaScript. Ces deux gestionnaires m'ont permis d'inclure toutes les librairies externes dont j'avais besoin pour mon TPI. Ceci me permet de ne pas avoir à télécharger manuellement les libraires et à les mettre dans mon projet. Leur utilisation m'a permis de faciliter grandement le développement du TPI et d'avoir des dépendances toujours à jour.

### Flask

<img style="float: right; margin-left: 25px; width: 30%" src="https://upload.wikimedia.org/wikipedia/commons/3/3c/Flask_logo.svg">[Flask](https://palletsprojects.com/p/flask/) est un micro framework web écrit en Python. Aucune couche autre que l'hébergement web n'est présent dans ce micro framework. Flask à été créé par [Armin Ronacher](https://en.wikipedia.org/wiki/Armin_Ronacher), membre de [Pocoo](https://www.pocoo.org/), un groupe de développeurs Python formé en 2004 - le 1<sup>er</sup> avril 2010. J'ai choisi d'utiliser ce framework pour mon TPI car il m'a permis d'aisément effectuer les tâches suivantes :

* Héberger mon site en local ainsi de pouvoir créer des routes web. Ces dernières sont des url écrites dans la barre d'adresse du navigateur. Elles sont utilisées non seulement pour éviter de devoir écrire en dur les nom des fichiers à afficher mais aussi de pouvoir exécuter du code avant d'afficher la page à l'utilisateur afin de récupérer des informations nécessaires au bon affichage des informations dynamiques. Un bon exemple d'utilisation est la page d'accueil : si l'utilisateur n'est pas connecté, un fond contenant une image est affiché et la barre de navigation du site ne permet que d'avoir accès à l'accueil, à la page à propos, à celle de connexion et enfin celle d'inscription. L'information comme quoi l'utilisateur n'est pas connecté est récupérée avant que la page soit affichée.
* Configurer le debug de mon site de manière générale. Il est possible de donner des paramètres de configuration à l'application Flask afin de faciliter le développement. J'ai utilisé ces paramètres pour faciliter le rafraichissement des pages dès lors qu'une modification est détectée dans un fichier.

### Jinja

<img style="float: right; margin-left: 25px; width: 30%" src="https://upload.wikimedia.org/wikipedia/commons/8/87/Jinja_software_logo.svg">[Jinja](https://jinja.palletsprojects.com/en/2.11.x/) est un moteur de modèle de page web pour Python. Il a été créé par [Armin Ronacher](https://en.wikipedia.org/wiki/Armin_Ronacher). Sa syntaxe est relativement identique au moteur de modèle Django mais adaptée pour la syntaxe de Python. Ce moteur de modèle est celui par défaut de [Flask](###Flask). 

### Flask-Login

[Flask-Login](https://flask-login.readthedocs.io/en/latest/) donne accès à un gestionnaire de sessions pour [Flask](###Flask). Il prend en compte les tâches standards comme la connexion, la déconnexion, et l'enregistrement de l'utilisateur en session sur une longue période de temps. Dans mon TPI, je l'utilise afin de connecter / déconnecter mes utilisateur et pour pouvoir stocker leurs informations en session durant leur utilisation du site.

### Flask-Swagger

[Flask-Swagger](https://pypi.org/project/flask-swagger/) donne accès à une méthode (swagger) qui inspecte les routes de [Flask](###Flask) contenant une docstring en YAML afin de générer les spécifications nécessaires à [Swagger](###Swagger).

### MySQL Connector/Python

[MySQL Connector/Python](https://dev.mysql.com/doc/connector-python/en/) est une librairie permettant à Python de communiquer avec les serveurs MySQL. Cette librairie est indispensable si l'on veut communiquer avec une base de données MySQL, et elle apporte des avantages tels que la conversion de données entre Python et MySQL. Par exemple, le `datetime` Python et `DATETIME` MySQL.

### SASS

<img style="float: right; margin-left: 25px; width: 30%" src="https://upload.wikimedia.org/wikipedia/commons/9/96/Sass_Logo_Color.svg">[SASS](https://sass-lang.com/) est un préprocesseur CSS. Cet outil permet d'étendre la syntaxe du langage CSS afin de pouvoir ajouter de nouvelles fonctionnalités. SASS permet aussi d'avoir un système de variable plus puissant que celui de CSS ainsi qu'un système d'import de fichier plus épuré à mon goût. En effet, il est possible de créer un fichier pour stocker toutes les couleurs sous forme de variables et ensuite importer ce fichier dans la feuille de style principale pour pouvoir utiliser les couleurs n'importe où.

### Swagger

<img style="float: right; margin-left: 25px; width: 30%" src="https://static1.smartbear.co/swagger/media/assets/images/swagger_logo.svg">[Swagger](https://swagger.io/tools/swagger-ui/) permet de visualiser les url d'une API automatiquement, en se basant sur les spécifications de chaque url. La génération du visuel est automatique et est optimisé pour une interaction avec le client. J'ai utilisé cet outil afin de visualiser correctement les routes utilisées par mon application et de récupérer des données.

### jQuery UI

[jQuery](https://jqueryui.com/) UI est un ensemble d'interactions utilisateur, d'effets, de widgets, et de thèmes construits sur la base de jQuery. J'ai utilisé cet outil afin de pouvoir gérer avec facilité la réorganisation des favoris d'un utilisateur. En effet, il est possible de drag&drop les couvertures des animes présent dans les favoris de l'utilisateur afin de réorganiser l'ordre de ces derniers.

### ESLint

<img style="float: right; margin-left: 25px; width: 30%" src="https://i.imgur.com/CbRxgU2.png">[ESLint](https://eslint.org/) est un outil de vérification syntaxique automatique de code. La vérification est basée sur un ensemble de règles définissant la syntaxe à utiliser. Cet outil m'a été utile pour vérifier que mon code était conforme aux normes [Airbnb](https://github.com/airbnb/javascript), pour éviter d'avoir des morceaux de code potentiellement problématiques ou mal optimisé voire même plus utilisés.

<img src="https://i.imgur.com/ac4CFJV.png">

<div style="width: 100%; text-align: center; color: gray">Cas d'utilisation de ESLint. La command <span style="color: #ff8000;">npm run lint static/js</span> m'indique qu'un point-virgule est manquant à la ligne 93 de mon fichier user-list-handler.js.</div>

### Pylint

<img style="float: right; margin-left: 25px; width: 30%" src="https://i.imgur.com/BxrqM3f.png">[Pylint](https://www.pylint.org/) est aussi un outil de vérification syntaxique comme [ESLint](###eslint). Cependant, il n'utilise pas de standard créé par la communauté mais les standards officiels de Python, le [PEP8](https://www.python.org/dev/peps/pep-0008/).

<img src="https://i.imgur.com/kJ9BcdV.png">

<div style="width: 100%; text-align: center; color: gray">Cas d'utilisation de Pylint. La command <span style="color: #ff8000;">pylint --output-format=colorized packages/controllers/SqliteController.py</span> m'indique, entre autre, que des imports ne sont pas bien placés.</div>

### Git

<img style="float: right; margin-left: 25px; width: 30%" src="https://upload.wikimedia.org/wikipedia/commons/e/e0/Git-logo.svg">[Git](https://git-scm.com/) est un outil de gestion de version. Cet outil a été utilisé durant toute la durée de mon TPI afin de garder un historique des modifications apportées à mon projet ainsi qu'un système de sauvegarde externe sur [Github](https://github.com) en cas de problème technique sur mon ordinateur local.

<div style='page-break-after: always; break-after: page; text-align:right;'></div>


## Analyse des fonctionnalités majeurs

### Un CRUD complet permet de gérer une entrée manga de la bibliothèque

L'utilisateur à un contrôle total sur ses propres listes. Cela comprend la création de nouvelles listes, le renommage et la suppression des listes existantes. Il n'a cependant pas la possibilité de créer lui-même une nouvelle entrée, mais il a la possibilité d'écraser toutes les entrées avec un nouveau jeu de données. Le CRUD est donc sur la gestion des entrées et non sur les entrées elles-mêmes, mais toutes les fonctions nécessaires à un CRUD sont présentes.

### La base de données locale sqlite3 est synchronisée de façon unidirectionnelle avec la base de données d'un serveur mysql

Un système de synchronisation unidirectionnelle est en place avec un algorithme fait manuellement. Le fonctionnement de cette synchronisation est le suivant : récupérer tous les enregistrements Sqlite3 et MySQL, s'il y a plus d'enregistrements Sqlite3, ajouter les enregistrements manquants dans MySQL, sinon les supprimer. Ensuite, comparer les timestamps des enregistrements dont les IDS sont identiques. Si les enregistrements MySQL ont une date inférieure à ceux de Sqlite3, les mettre à jour. Ce processus mérite des améliorations, car il reste lent lorsque MySQL est vide ou qu'énormément de modifications ont été apportées aux données. J'explique comment cela pourrait être amélioré dans la parte prévue à cet effet. Voici le pseudo-code :

```pseudocode
foreach table {
	stocker le nom de la table courante
	
	récupérer le nombre d'enregistrements de Sqlite3 et le stocker
	récupérer le nombre d'enregistrements de MySQL et le stocker
	
	if nombre enregistrements Sqlite3 différent de nombre enregistrements MySQL {
		récupérer ids et timestamp Sqlite3 pour stocker dans tableau id: timestamp
		récupérer ids et timestamp MySQL pour stocker dans tableau id: timestamp
		
		trier les tableaux par id
		
		if tableau Sqlite3 > tableau MySQL {
			stocker ids Sqlite3 non présent dans tableau MySQL
			retirer les ids ci-dessus du tableau Sqlite3
			
			récupérer les enregistrements Sqlite3 correspondant aux ids non présent MySQL
			
			foreach enregistrement Sqlite3 {
				insérer dans MySQL
			}
		} else {
			stocker ids MySQL non présent dans Sqlite3
			
			foreach id MySQL {
				supprimer l'entrée MySQL
			}
		}
	}
	
	déclarer tableau pour ids Sqlite3 dont timestamp diffère du MySQL
	foreach enregistrements Sqlite3 {
		if timestamp courant différent du timestamp MySQL correspondant {
			ajouter l'id dans le tablea créer à cet effet
		}
	}
	
	récupérer les enregistrements Sqlite3 correspondant aux ids
	foreach enregistrement {
		mettre à jour l'enregistrement correspondant dans MySQL
	}
}
```

### Les données JSON de github sont importées dans la base de données locale

Le fichier donné dans l'énoncé comporte ~500k lignes de JSON et a la structure de données suivante :

```json
{
    "data": [
    {
      "sources": [
        "https://anidb.net/anime/10143",
        "https://anilist.co/anime/102416",
        "https://kitsu.io/anime/8925",
        "https://myanimelist.net/anime/20707",
        "https://notify.moe/anime/Ff1bpKmmR"
      ],
      "title": "\"0\"",
      "type": "Special",
      "episodes": 1,
      "status": "FINISHED",
      "picture": "https://cdn.myanimelist.net/images/anime/6/54815.jpg",
      "thumbnail": "https://cdn.myanimelist.net/images/anime/6/54815t.jpg",
      "synonyms": [
        "Chiaki Kuriyama: 「0」",
        "「0」"
      ],
      "relations": []
    },
    ...
}
```

J'ai dû normaliser les données afin de les insérer correctement dans la base de données locale. Grâce à Sqlite3, l'insertion d'autant d'enregistrement est très rapide, il faut compter uniquement quelques secondes. L'écrasement des données peut être réalisé par tous les utilisateurs. Cet aspect peut être amélioré et j'en parle dans la section prévue à cet effet.

### Le service http utilise Python Flask

Comme l'application est développée en Python, il me faut un moyen d'héberger mon site sur le service HTTP. Pour Python, il faut utiliser Flask. la configuration n'est vraiment pas compliquée et pour lancer le serveur, il faut exécuter la commande dans le dossier parent au projet : `python3 -m Animanga.app run`.

### Le planning réel est documenté et comparé au planning prescrit

Un planning m'a été donné dans l'énoncé mais je ne le trouvais pas assez précis. J'ai alors pris l'initiative de refaire un planning prévisionnel. J'y ai inscrit toutes les *user stories* créées lors du premier jour du TPI. Mon planning réel est mixé au planning prévisionnel mais les couleurs sont différentes. Comme cela, il est plus facile de comparer les deux plannings. La légende concernant les couleurs est présente sous le planning.

### Le projet est publié sur github et une url est communiqué

Mon projet utilise Git et est lié à GitHub. l'URL du répertoire distant est <https://github.com/TanguyCavagna/Animanga>.

### Le projet Python contient au moins une classe (python objet) conçu par le candidat

Mon projet est rempli de classes. En effet, j'ai décidé de faire un contrôleur (classe de contrôle des données) par type de données utilisé et un modèle (classe de représentation des données) pour chaque type de données. Toutes ces classes sont expliquées dans la section adéquate, sous la partie *Implémentation*.
## Plans de test et tests

### Périmètre des tests

Pour *Animanga*, j'ai mis en place un protocole de tests afin que n'importe quel utilisateur puisse naviguer convenablement dans l'application, peu importe son navigateur WEB.

### Environnement

Lors de ces tests, j'utilise les navigateurs suivants :

* Mozilla Firefox 76.0.1 (64 bits) sur Windows 10 Entreprise 1903
* Google Chrome 81.0.4044.138 (64 bits) sur Windows 10 Entreprise 1903
* Microsoft Edge Version 81.0.416.72 (64 bits) sur Windows 10 Entreprise 1903

### Scénarios

Les scénarios des tests sont détaillés afin qu'un autre professionnel puisse les exécuter. Pour rédiger mes scénarios, j'utilise la syntaxe [**Gherkin**](https://cucumber.io/docs/gherkin/).

| __Nom__               | __1.1__ Création d'un nouveau compte (<span style="color: #2dd674">informations valides</span>) |
| :-------------------- | :----------------------------------------------------------- |
| __User Story__        | S1 : Inscription à Animanga                                  |
| __Situation__         | **Étant donné que** je suis un nouvel utilisateur de Animanga, je ne possède pas encore de compte. <br>**Quand** je clique sur le bouton *Inscription*, je suis redirigé vers la page d'inscription et je remplis le formulaire avec les informations suivantes :  email: `katalon@recorder.ch`, pseudo: `Katalon`, MDP: `MotDePasse`, confirmation: `MotDePasse`. <br>**Alors**, je suis redirigé sur la page d'accueil avec mon nouveau compte connecté. |
| __Résultats obtenus__ | Je suis redirigé vers la page d'accueil avec mon nouveau compte connecté. |
| __Statut__            | ✔ OK                                                         |

| **Nom**               | **1.2** Création d'un nouveau compte (<span style="color: #d62d46">informations invalides</span>) |
| :-------------------- | :----------------------------------------------------------- |
| **User Story**        | S1 : Inscription à Animanga                                  |
| **Situation**         | **Étant donné que** je suis un nouvel utilisateur de Animanga, je ne possède pas encore de compte.  <br>**Quand** je clique sur le bouton *Inscription*, je suis redirigé vers la page d'inscription et je remplis le formulaire avec les informations suivantes :  email: `-`, pseudo: `Katalon`, MDP: `MotDePasse`, confirmation: `MotDePasse`.  <br>**Alors**, le formulaire est rechargé avec un message d'erreur indiquant ce qui ne s'est pas bien passé. |
| **Résultats obtenus** | Un message s'affiche m'indiquant que l'email n'est pas présent. |
| **Statut**            | ✔ OK                                                         |

| **Nom**               | **1.3** Création d'un nouveau compte (<span style="color: #d62d46">informations invalides</span>) |
| :-------------------- | :----------------------------------------------------------- |
| **User Story**        | S1 : Inscription à Animanga                                  |
| **Situation**         | **Étant donné que** je suis un nouvel utilisateur de Animanga, je ne possède pas encore de compte.<br />**Quand** je clique sur le bouton *Inscription*, je suis redirigé vers la page d'inscription et je remplii le formulaire avec les informations suivantes :  email: `a@b.c`, pseudo: `Katalon`, MDP: `MotDePasse`, confirmation: `MotDePasse`.<br />**Alors**, le formulaire est rechargé avec un message d'erreur indiquant ce qui ne s'est pas bien passé. |
| **Résultats obtenus** | Un message s'affiche m'indiquant que l'email fourni est trop court. |
| **Statut**            | ✔ OK                                                         |

| **Nom**               | **1.4** Création d'un nouveau compte (<span style="color: #d62d46">informations invalides</span>) |
| :-------------------- | :----------------------------------------------------------- |
| **User Story**        | S1 : Inscription à Animanga                                  |
| **Situation**         | **Étant donné que** je suis un nouvel utilisateur de Animanga, je ne possède pas encore de compte.<br />**Quand** je clique sur le bouton *Inscription*, je suis redirigé vers la page d'inscription et je remplis le formulaire avec les informations suivantes :  email: `invalide/@recorder.ch`, pseudo: `Katalon`, MDP: `MotDePasse`, confirmation: `MotDePasse`.<br />**Alors**, le formulaire est rechargé avec un message d'erreur indiquant ce qui ne s'est pas bien passé. |
| **Résultats obtenus** | Un message s'affiche m'indiquant que l'email fourni n'est pas correct. |
| **Statut**            | ✔ OK                                                         |

| **Nom**               | **1.5** Création d'un nouveau compte (<span style="color: #d62d46">informations invalides</span>) |
| :-------------------- | :----------------------------------------------------------- |
| **User Story**        | S1 : Inscription à Animanga                                  |
| **Situation**         | **Étant donné que** je suis un nouvel utilisateur de Animanga, je ne possède pas encore de compte.<br />**Quand** je clique sur le bouton *Inscription*, je suis redirigé vers la page d'inscription et je remplis le formulaire avec les informations suivantes :  email: `katalon@recorder.ch`, pseudo: `-`, MDP: `MotDePasse`, confirmation: `MotDePasse`.<br />**Alors**, le formulaire est rechargé avec un message d'erreur indiquant ce qui ne s'est pas bien passé. |
| **Résultats obtenus** | Un message s'affiche m'indiquant que le pseudo est manquant. |
| **Statut**            | ✔ OK                                                         |

| **Nom**               | **1.6** Création d'un nouveau compte (<span style="color: #d62d46">informations invalides</span>) |
| :-------------------- | :----------------------------------------------------------- |
| **User Story**        | S1 : Inscription à Animanga                                  |
| **Situation**         | **Étant donné que** je suis un nouvel utilisateur de Animanga, je ne possède pas encore de compte.<br />**Quand** je clique sur le bouton *Inscription*, je suis redirigé vers la page d'inscription et je remplis le formulaire avec les informations suivantes :  email: `katalon@recorder.ch`, pseudo: `Katalon`, MDP: `-`, confirmation: `-`.<br />**Alors**, le formulaire est rechargé avec un message d'erreur indiquant ce qui ne s'est pas bien passé. |
| **Résultats obtenus** | Un message s'affiche m'indiquant que le mot de passe est manquant. |
| **Statut**            | ✔ OK                                                         |

| **Nom**               | **1.7** Création d'un nouveau compte (<span style="color: #d62d46">informations invalides</span>) |
| :-------------------- | :----------------------------------------------------------- |
| **User Story**        | S1 : Inscription à Animanga                                  |
| **Situation**         | **Étant donné que** je suis un nouvel utilisateur de Animanga, je ne possède pas encore de compte.<br />**Quand** je clique sur le bouton *Inscription*, je suis redirigé vers la page d'inscription et je remplis le formulaire avec les informations suivantes :  email: `katalon@recorder.ch`, pseudo: `Katalon`, MDP: `Court`, confirmation: `Court`.<br />**Alors**, le formulaire est rechargé avec un message d'erreur indiquant ce qui ne s'est pas bien passé. |
| **Résultats obtenus** | Un message s'affiche m'indiquant que le mot de passe est trop court. |
| **Statut**            | ✔ OK                                                         |

| **Nom**               | **1.8** Création d'un nouveau compte (<span style="color: #d62d46">informations invalides</span>) |
| :-------------------- | :----------------------------------------------------------- |
| **User Story**        | S1 : Inscription à Animanga                                  |
| **Situation**         | **Étant donné que** je suis un nouvel utilisateur de Animanga, je ne possède pas encore de compte.<br />**Quand** je clique sur le bouton *Inscription*, je suis redirigé vers la page d'inscription et je remplis le formulaire avec les informations suivantes :  email: `katalon@recorder.ch`, pseudo: `Katalon`, MDP: `-`, confirmation: `-`.<br />**Alors**, le formulaire est rechargé avec un message d'erreur indiquant ce qui ne s'est pas bien passé. |
| **Résultats obtenus** | Un message s'affiche m'indiquant que le mot de passe de confirmation est manquant. |
| **Statut**            | ✔ OK                                                         |

| **Nom**               | **1.9** Création d'un nouveau compte (<span style="color: #d62d46">informations invalides</span>) |
| :-------------------- | :----------------------------------------------------------- |
| **User Story**        | S1 : Inscription à Animanga                                  |
| **Situation**         | **Étant donné que** je suis un nouvel utilisateur de Animanga, je ne possède pas encore de compte.<br />**Quand** je clique sur le bouton *Inscription*, je suis redirigé vers la page d'inscription et je remplis le formulaire avec les informations suivantes :  email: `katalon@recorder.ch`, pseudo: `Katalon`, MDP: `MotDePasse`, confirmation: `MotDePasseDifferent`.<br />**Alors**, le formulaire est rechargé avec un message d'erreur indiquant ce qui ne s'est pas bien passé. |
| **Résultats obtenus** | Un message s'affiche m'indiquant que les mots de passes sont différent. |
| **Statut**            | ✔ OK                                                         |

| **Nom**               | **1.10** Création d'un nouveau compte (<span style="color: #d62d46">informations invalides</span>) |
| :-------------------- | :----------------------------------------------------------- |
| **User Story**        | S1 : Inscription à Animanga                                  |
| **Situation**         | **Étant donné que** je suis un nouvel utilisateur de Animanga, je ne possède pas encore de compte.<br />**Quand** je clique sur le bouton *Inscription*, je suis redirigé vers la page d'inscription et je remplis le formulaire avec les informations suivantes :  email: `katalon@recorder.ch`, pseudo: `Katalon`, MDP: `MotDePasse`, confirmation: `MotDePasseDifferent`.<br />**Alors**, le formulaire est rechargé avec un message d'erreur indiquant ce qui ne s'est pas bien passé. |
| **Résultats obtenus** | Un message s'affiche m'indiquant que l'email est déjà utilisé. |
| **Statut**            | ✔ OK                                                         |

| **Nom**               | 2.1 Connexion avec un compte existant (<span style="color: #2dd674">informations valides</span>) |
| :-------------------- | :----------------------------------------------------------- |
| **User Story**        | S2 : Connexion à Animanga                                    |
| **Situation**         | **Étant donné que** je suis un utilisateur de Animanga, j'ai déjà un compte à disposition. <br>**Quand** je clique sur le bouton *Connexion*, je suis redirigé vers la page de connexion et je remplis le formulaire avec les informations suivantes : email: `katalon@recorder.ch`, MDP: `MotDePasse`.<br>**Alors**, je suis redirigé sur la page d'accueil avec mon compte connecté. |
| **Résultats obtenus** | Je suis redirigé vers la page d'accueil avec mon nouveau compte connecté. |
| **Statut**            | ✔ OK                                                         |

| **Nom**               | 2.2 Connexion avec un compte existant (<span style="color: #d62d46">informations invalides</span>) |
| :-------------------- | :----------------------------------------------------------- |
| **User Story**        | S2 : Connexion à Animanga                                    |
| **Situation**         | **Étant donné que** je suis un utilisateur de Animanga, j'ai déjà un compte à disposition.<br />**Quand** je clique sur le bouton *Connexion*, je suis redirigé vers la page de connexion et je remplis le formulaire avec les informations suivantes : email: `-`, MDP: `MotDePasse`.<br />**Alors**, je suis redirigé sur la page d'accueil avec mon compte connecté. |
| **Résultats obtenus** | Un message s'affiche m'indiquant que l'email est manquant.   |
| **Statut**            | ✔ OK                                                         |

| **Nom**               | 2.3 Connexion avec un compte existant (<span style="color: #d62d46">informations invalides</span>) |
| :-------------------- | :----------------------------------------------------------- |
| **User Story**        | S2 : Connexion à Animanga                                    |
| **Situation**         | **Étant donné que** je suis un utilisateur de Animanga, j'ai déjà un compte à disposition.<br />**Quand** je clique sur le bouton *Connexion*, je suis redirigé vers la page de connexion et je remplis le formulaire avec les informations suivantes : email: `invalide/@recorder.ch`, MDP: `MotDePasse`.<br />**Alors**, je suis redirigé sur la page d'accueil avec mon compte connecté. |
| **Résultats obtenus** | Un message s'affiche m'indiquant que l'email est invalide.   |
| **Statut**            | ✔ OK                                                         |

| **Nom**               | 2.4 Connexion avec un compte existant (<span style="color: #d62d46">informations invalides</span>) |
| :-------------------- | :----------------------------------------------------------- |
| **User Story**        | S2 : Connexion à Animanga                                    |
| **Situation**         | **Étant donné que** je suis un utilisateur de Animanga, j'ai déjà un compte à disposition.<br />**Quand** je clique sur le bouton *Connexion*, je suis redirigé vers la page de connexion et je remplis le formulaire avec les informations suivantes : email: `katalon@recorder.ch`, MDP: `-`.<br />**Alors**, je suis redirigé sur la page d'accueil avec mon compte connecté. |
| **Résultats obtenus** | Un message s'affiche m'indiquant que le mot de passe est manquant. |
| **Statut**            | ✔ OK                                                         |

| **Nom**               | 2.5 Connexion avec un compte existant (<span style="color: #d62d46">informations invalides</span>) |
| :-------------------- | :----------------------------------------------------------- |
| **User Story**        | S2 : Connexion à Animanga                                    |
| **Situation**         | **Étant donné que** je suis un utilisateur de Animanga, j'ai déjà un compte à disposition.<br />**Quand** je clique sur le bouton *Connexion*, je suis redirigé vers la page de connexion et je remplis le formulaire avec les informations suivantes : email: `katalon@recorder.ch`, MDP: `MotDePasseInexistant`.<br />**Alors**, je suis redirigé sur la page d'accueil avec mon compte connecté. |
| **Résultats obtenus** | Un message s'affiche m'indiquant que la combinaison email - mot de passe est invalide. |
| **Statut**            | ✔ OK                                                         |

| **Nom**               | 2.6 Déconnexion                                              |
| :-------------------- | :----------------------------------------------------------- |
| **User Story**        | S2 : Connexion à Animanga                                    |
| **Situation**         | **Étant donné que** je suis un utilisateur connecté au site.<br>**Quand** je clique sur le bouton *Déconnexion* placé dans le dropdown du menu *Utilisateur*.<br>**Alors**, je deviens un utilisateur non connecté et je suis redirigé sur la page de connexion. |
| **Résultats obtenus** | Je clique sur *Utilisateur* et *Déconnexion*. Je ne suis plus connecté et je suis redirigé sur la page de connexion. |
| **Statut**            | ✔ OK                                                         |

| **Nom**               | 3.1 Importation des animes                                   |
| :-------------------- | :----------------------------------------------------------- |
| **User Story**        | S3 : Importation des animes                                  |
| **Situation**         | **Étant donné que** je suis un utilisateur connecté au site. <br />**Quand** je clique sur le bouton *Écraser tous les animes* placé dans le dropdown du menu *Utilisateur*.<br />**Alors**, j'écrase toutes les données du site relatives aux animes eux-même. Cela comprend les animes en eux même, les favoris ainsi que les animes contenus dans les listes. |
| **Résultats obtenus** | Je clique sur *Utilisateur* et *Écraser tous les animes*. Je suis redirigé vers la page d'accueil et des alertes s'affichent en haut au centre de l'écran indiquant l'état de la mise à jours des animes. |
| **Statut**            | ✔ OK                                                         |

| **Nom**               | 4.1 Recherche des animes                                     |
| :-------------------- | :----------------------------------------------------------- |
| **User Story**        | S4 : Recherche des animes                                    |
| **Situation**         | **Étant donné que** je suis un utilisateur connecté au site. <br />**Quand** je clique sur le bouton 🔍 placé dans la barre de navigation et que j'écris "k On" dans le champ de recherche de la modale.<br />**Alors**, je suis redirigé vers la page d'accueil et les résultats de la recherche affiche l'anime "K-ON!". |
| **Résultats obtenus** | L'anime "K-ON!" est présent dans la zone de résultat de recherche. |
| **Statut**            | ✔ OK                                                         |

| **Nom**               | 4.2 Recherche des animes avec raccourcis                     |
| :-------------------- | :----------------------------------------------------------- |
| **User Story**        | S4 : Recherche des animes                                    |
| **Situation**         | **Étant donné que** je suis un utilisateur connecté au site. <br />**Quand** je fais le raccourcis clavier <kbd>Ctrl</kbd> + <kbd>S</kbd> et que j'écris "k On" dans le champ de recherche de la modale.<br />**Alors**, je suis redirigé vers la page d'accueil et les résultats de la recherche affiche l'anime "K-ON!". |
| **Résultats obtenus** | L'anime "K-ON!" est présent dans la zone de résultat de recherche. |
| **Statut**            | ✔ OK                                                         |

| **Nom**               | 5.1 Affichage de la carte de l'anime                         |
| :-------------------- | :----------------------------------------------------------- |
| **User Story**        | S5 : Affichage de la carte de l'anime                        |
| **Situation**         | **Étant donné que** je suis un utilisateur connecté au site sur la page d'accueil ayant fait une recherche. <br />**Quand** je clique sur le titre d'un anime présent dans la zone de résultat de la recherche.<br />**Alors**, une modale s'affiche contenant l'image de couverture, le titre, le statut de visionnement de l'anime, et les listes personnelles de l'utilisateur. |
| **Résultats obtenus** | La modale s'affiche avec le contenu adéquat.                 |
| **Statut**            | ✔ OK                                                         |

| **Nom**               | 6.1 Mise à jour du statut de l'anime sélectionné             |
| :-------------------- | :----------------------------------------------------------- |
| **User Story**        | S6 : Mise à jour de l'anime                                  |
| **Situation**         | **Étant donné que** je suis un utilisateur connecté au site sur la page d'accueil ayant fait une recherche et ayant ouvert la modale d'informations d'un anime. <br />**Quand** sélectionne un statut autre que "---".<br />**Alors**, le combo-box se met à jour avec la nouvelle valeur sélectionnée. |
| **Résultats obtenus** | La valeur du combo-box s'est bien mise à jour.               |
| **Statut**            | ✔ OK                                                         |

| **Nom**               | 6.2 Ajout de l'anime dans une liste personnelle              |
| :-------------------- | :----------------------------------------------------------- |
| **User Story**        | S6 : Mise à jour de l'anime                                  |
| **Situation**         | **Étant donné que** je suis un utilisateur connecté au site sur la page d'accueil ayant fait une recherche et ayant ouvert la modale d'informations d'un anime. <br />**Quand** je clique sur une check-box blanche d'une des listes personnelles.<br />**Alors**, l'état de la check-box se met à jour et elle se colore en bleu. L'anime est maintenant présent dans la liste personnelle. |
| **Résultats obtenus** | L'état de la check-box s'est bien mis à jour et est bien coloré en bleu. |
| **Statut**            | ✔ OK                                                         |

| **Nom**               | 6.3 Ajout de l'anime dans les favoris                        |
| :-------------------- | :----------------------------------------------------------- |
| **User Story**        | S6 : Mise à jour de l'anime                                  |
| **Situation**         | **Étant donné que** je suis un utilisateur connecté au site sur la page d'accueil ayant fait une recherche et ayant ouvert la modale d'informations d'un anime. <br />**Quand** je clique sur le cœur blanc pour ajouter au favoris.<br />**Alors**, le cœur se colore et l'anime se rajoute dans la zone des favoris de la page d'accueil. |
| **Résultats obtenus** | Le cœur s'est coloré et l'anime s'est correctement ajouté dans la zone des favoris de la page d'accueil. |
| **Statut**            | ✔ OK                                                         |

| **Nom**               | 6.4 Suppression du statut de l'anime                         |
| :-------------------- | :----------------------------------------------------------- |
| **User Story**        | S6 : Mise à jour de l'anime                                  |
| **Situation**         | **Étant donné que** je suis un utilisateur connecté au site sur la page d'accueil ayant fait une recherche et ayant ouvert la modale d'informations d'un anime.<br />**Quand** je sélectionne le statut "---".<br />**Alors**, le combo-box se met à jour avec la nouvelle valeur sélectionnée et l'anime n'est plus présent dans aucun autre statut. |
| **Résultats obtenus** | La valeur du combo-box s'est bien mise à jour et l'anime n'est effectivement plus présent dans les autres statuts. |
| **Statut**            | ✔ OK                                                         |

| **Nom**               | 6.5 Suppression de l'anime d'une liste personnelle           |
| :-------------------- | :----------------------------------------------------------- |
| **User Story**        | S6 : Mise à jour de l'anime                                  |
| **Situation**         | **Étant donné que** je suis un utilisateur connecté au site sur la page d'accueil ayant fait une recherche et ayant ouvert la modale d'informations d'un anime.<br />**Quand** je clique sur une check-box bleue d'une des listes personnelles.<br />**Alors**, l'état de la check-box se met à jour et se colore en blanc. L'anime n'est plus présent dans la cette liste personnelle. |
| **Résultats obtenus** | L'état de la check-box s'est bien mis à jour et est coloré en blanc. |
| **Statut**            | ✔ OK                                                         |

| **Nom**               | 6.6 Suppression de l'anime des favoris                       |
| :-------------------- | :----------------------------------------------------------- |
| **User Story**        | S6 : Mise à jour de l'anime                                  |
| **Situation**         | **Étant donné que** je suis un utilisateur connecté au site sur la page d'accueil ayant fait une recherche et ayant ouvert la modale d'informations d'un anime.<br />**Quand** je clique sur le cœur rose pour supprimer des favoris.<br />**Alors**, le cœur se colore en blanc et l'anime se supprime de la zone des favoris de la page d'accueil. |
| **Résultats obtenus** | Le cœur s'est coloré en blanc et l'anime s'est correctement supprimé de la zone des favoris de la page d'accueil. |
| **Statut**            | ✔ OK                                                         |

| **Nom**               | 7.1 Affichage du profile de l'utilisateur connecté           |
| :-------------------- | :----------------------------------------------------------- |
| **User Story**        | S7 : Affichage du profile                                    |
| **Situation**         | **Étant donné que** je suis un utilisateur connecté.<br />**Quand** je clique sur *Profile* dans la barre de navigation.<br />**Alors**, la page de profile de l'utilisateur connecté s'affiche avec ses statistiques et ses favoris. |
| **Résultats obtenus** | La page de profile de l'utilisateur connecté s'affiche correctement et les statistiques ainsi que les favoris sont les siens. |
| **Statut**            | ✔ OK                                                         |

| **Nom**               | 8.1 Affichage des listes de l'utilisateur connecté           |
| :-------------------- | :----------------------------------------------------------- |
| **User Story**        | S8 : Affichage des listes                                    |
| **Situation**         | **Étant donné que** je suis un utilisateur connecté.<br />**Quand** je clique sur *Listes* dans la barre de navigation.<br />**Alors**, la page contenant toutes les listes de l'utilisateur connecté s'affiche ainsi que les animes contenus dans ces listes. |
| **Résultats obtenus** | La page contenant les listes de l'utilisateur connecté s'est correctement affichée et les animes sont correctement affiché aussi. |
| **Statut**            | ✔ OK                                                         |

| **Nom**               | 9.1 Créer une liste                                          |
| :-------------------- | :----------------------------------------------------------- |
| **User Story**        | S9 : Gestion des listes                                      |
| **Situation**         | **Étant donné que** je suis un utilisateur connecté.<br />**Quand** je suis sur la page des listes et que j'écris "Ma nouvelle liste" dans le champ de texte *Nouvelle liste* et que j'appuie sur <kbd>Enter</kbd>.<br />**Alors**, la liste apparaît en bas des listes déjà présentes avec une 🗑️ à côté. |
| **Résultats obtenus** | La liste à bien été ajoutée en base des listes déjà présente. |
| **Statut**            | ✔ OK                                                         |

| **Nom**               | 9.2 Supprimer une liste                                      |
| :-------------------- | :----------------------------------------------------------- |
| **User Story**        | S9 : Gestion des listes                                      |
| **Situation**         | **Étant donné que** je suis un utilisateur connecté.<br />**Quand** je suis sur la page des listes et que je clique sur 🗑️ d'une liste présente.<br />**Alors**, la liste ne sera plus présente dans les listes déjà existantes. |
| **Résultats obtenus** | La liste à bien été supprimée et n'est plus présente dans les listes déjà existantes. |
| **Statut**            | ✔ OK                                                         |

| **Nom**               | 9.3 Renommer une liste                                       |
| :-------------------- | :----------------------------------------------------------- |
| **User Story**        | S9 : Gestion des listes                                      |
| **Situation**         | **Étant donné que** je suis un utilisateur connecté.<br />**Quand** je double-clique sur le nom de la liste, je peux renommer la liste et valider en appuyant sur <kbd>Entré</kbd>.<br />**Alors**, le nom de la liste est changé. |
| **Résultats obtenus** | Le nom de la liste est bien mis à jour.                      |
| **Statut**            | ✔ OK                                                         |

| **Nom**               | 10.1 Affichage des favoris sur l'accueil                     |
| :-------------------- | :----------------------------------------------------------- |
| **User Story**        | S10 : Affichage des favoris                                  |
| **Situation**         | **Étant donné que** je suis un utilisateur connecté.<br />**Quand** je suis sur la page d'accueil.<br />**Alors**, mes favoris sont présents sur la page. |
| **Résultats obtenus** | Mes favoris sont bien affichés.                              |
| **Statut**            | ✔ OK                                                         |

| **Nom**               | 10.2 Affichage des favoris du profile                        |
| :-------------------- | :----------------------------------------------------------- |
| **User Story**        | S10 : Affichage des favoris                                  |
| **Situation**         | **Étant donné que** je suis un utilisateur connecté.<br />**Quand** je suis sur ma page de profile.<br />**Alors**, mes favoris sont présent sur la page. |
| **Résultats obtenus** | Mes favoris sont bien affiché.                               |
| **Statut**            | ✔ OK                                                         |

| **Nom**               | 11.1 Organisation des favoris                                |
| :-------------------- | :----------------------------------------------------------- |
| **User Story**        | S11 : Organisation des favoris                               |
| **Situation**         | **Étant donné que** je suis un utilisateur connecté.<br />**Quand** je suis sur la page des favoris et je clique sur le bouton *Réorganiser les favoris*, je peux glisser déposer les animes dans l'ordre que je veux. Je clique sur le bouton *Sauvegarder* pour enregistrer l'ordre.<br />**Alors**, mes favoris sont enregistrés dans l'ordre voulu. |
| **Résultats obtenus** | Mes favoris ont bien été réorganisé.                         |
| **Statut**            | ✔ OK                                                         |

| **Nom**               | 11.2 suppression des favoris                                 |
| :-------------------- | :----------------------------------------------------------- |
| **User Story**        | S11 : Organisation des favoris                               |
| **Situation**         | **Étant donné que** je suis un utilisateur connecté.<br />**Quand** je suis sur la page des favoris et je clique sur le bouton *Réorganiser les favoris*, je peux cliquer sur <img src="https://i.imgur.com/FzE4PuB.png" width="25px"> pour enlever l'anime des favoris.<br />**Alors**, l'anime ne fait plus partie des favoris. |
| **Résultats obtenus** | L'anime est bien retiré des favoris.                         |
| **Statut**            | ✔ OK                                                         |

| **Nom**               | 12.1 Affichage de la landing page                            |
| :-------------------- | :----------------------------------------------------------- |
| **User Story**        | S12 : Affichage de la landing page                           |
| **Situation**         | **Étant donné que** je suis un utilisateur non connecté.<br />**Quand** je suis sur le site.<br />**Alors**, une page d'accueil s'affiche avec comme possibilité : la visite de la page *À propos*, la connexion et l'inscription. |
| **Résultats obtenus** | La page d'accueil ainsi que la barre de navigation sont affichés correctement pour un utilisateur non connecté. |
| **Statut**            | ✔ OK                                                         |

| **Nom**               | 13.1 Respect du preset Airbnb                                |
| :-------------------- | :----------------------------------------------------------- |
| **User Story**        | S17 : Vérification syntaxique                                |
| **Situation**         | **Étant donné que** je suis un développeur. <br />**Quand** j'exécute la commande `npm run lint` dans le dossier de mon projet. <br />**Alors**, aucune erreur de syntaxe sur la base du preset Airbnb n'est relevée. |
| **Résultats obtenus** | <span style="font-size: 0.8rem">\> Animanga@1.0.0 lint /home/cavagnat/Documents/programmation/python/Animanga<br/>\> eslint '**/*.js' --ignore-pattern node_modules/</span> |
| **Statut**            | ✔ OK                                                         |

| **Nom**               | 13.2 Respect des conventions PEP8                            |
| :-------------------- | :----------------------------------------------------------- |
| **User Story**        | S17 : Vérification syntaxique                                |
| **Situation**         | **Étant donné que** je suis un développeur. <br />**Quand** j'exécute la commande `python3 -m pylint --output-format=colorized packages` à la racine de mon projet.<br /> **Alors**, aucune erreur de syntaxe sur la base des conventions PEP8 n'est relevée. |
| **Résultats obtenus** | La note attribuée au code et supérieur à 10/10.              |
| **Statut**            | ✔ OK                                                         |

| **Nom**               | 14.1 Synchronisation Sqlite3 - MySQL                         |
| :-------------------- | :----------------------------------------------------------- |
| **User Story**        | S15 : Synchronisation MySQL Sqlite3                          |
| **Situation**         | **Étant donné que** je suis un utilisateur connecté.<br />**Quand** je clique sur l'icône de synchronisation.<br />**Alors**, la page charge et je suis redirigé vers la page d'accueil. |
| **Résultats obtenus** | Les données sont identiques entre la base Sqlite3 et MySQL.  |
| **Statut**            | ✔ OK                                                         |

| **Nom**               | 15.1 Affichage des activités des 24 dernières heures         |
| :-------------------- | :----------------------------------------------------------- |
| **User Story**        | S15 : Affichage des activités                                |
| **Situation**         | **Étant donné que** je suis un utilisateur connecté.<br />**Quand** je mets un anime en favoris et dans une liste (changement de statut aussi).<br />**Alors**, une carte s'affiche sur l'accueil avec le nom de l'anime modifié ainsi que son image, le nom de la liste dans laquelle il a été ajouté, et le temps écoulé depuis la mise à jour. |
| **Résultats obtenus** | La carte s'affiche avec les informations correctes.          |
| **Statut**            | ✔ OK                                                         |

### Évolution des tests

| N° Test | J1<br /><span style="font-weight: normal">lu.25</span> | J2<br /><span style="font-weight: normal">ma.26</span> | J3<br /><span style="font-weight: normal">me.27</span> | J4<br /><span style="font-weight: normal">je.28</span> | J5<br /><span style="font-weight: normal">ve.29</span> | J6<br /><span style="font-weight: normal">ma.2</span> | J7<br /><span style="font-weight: normal">me.3</span> | J8<br /><span style="font-weight: normal">je.4</span> | J9<br /><span style="font-weight: normal">ve.5</span> | J10<br /><span style="font-weight: normal">lu.8</span> | J11<br /><span style="font-weight: normal">ma.9</span> |
| :-----: | :----------------------------------------------------: | :----------------------------------------------------: | :----------------------------------------------------: | :----------------------------------------------------: | :----------------------------------------------------: | :---------------------------------------------------: | :---------------------------------------------------: | :---------------------------------------------------: | :---------------------------------------------------: | :----------------------------------------------------: | :----------------------------------------------------: |
|   1.1   |                           ❌                            |                           ❌                            |                           ✔                            |                           ✔                            |                           ✔                            |                           ✔                           |                           ✔                           |                           ✔                           |                           ✔                           |                           ✔                            |                           ✔                            |
|   1.2   |                           ❌                            |                           ❌                            |                           ✔                            |                           ✔                            |                           ✔                            |                           ✔                           |                           ✔                           |                           ✔                           |                           ✔                           |                           ✔                            |                           ✔                            |
|   1.3   |                           ❌                            |                           ❌                            |                           ✔                            |                           ✔                            |                           ✔                            |                           ✔                           |                           ✔                           |                           ✔                           |                           ✔                           |                           ✔                            |                           ✔                            |
|   1.4   |                           ❌                            |                           ❌                            |                           ✔                            |                           ✔                            |                           ✔                            |                           ✔                           |                           ✔                           |                           ✔                           |                           ✔                           |                           ✔                            |                           ✔                            |
|   1.5   |                           ❌                            |                           ❌                            |                           ✔                            |                           ✔                            |                           ✔                            |                           ✔                           |                           ✔                           |                           ✔                           |                           ✔                           |                           ✔                            |                           ✔                            |
|   1.6   |                           ❌                            |                           ❌                            |                           ✔                            |                           ✔                            |                           ✔                            |                           ✔                           |                           ✔                           |                           ✔                           |                           ✔                           |                           ✔                            |                           ✔                            |
|   1.7   |                           ❌                            |                           ❌                            |                           ✔                            |                           ✔                            |                           ✔                            |                           ✔                           |                           ✔                           |                           ✔                           |                           ✔                           |                           ✔                            |                           ✔                            |
|   1.8   |                           ❌                            |                           ❌                            |                           ✔                            |                           ✔                            |                           ✔                            |                           ✔                           |                           ✔                           |                           ✔                           |                           ✔                           |                           ✔                            |                           ✔                            |
|   1.9   |                           ❌                            |                           ❌                            |                           ✔                            |                           ✔                            |                           ✔                            |                           ✔                           |                           ✔                           |                           ✔                           |                           ✔                           |                           ✔                            |                           ✔                            |
|   2.1   |                           ❌                            |                           ❌                            |                           ✔                            |                           ✔                            |                           ✔                            |                           ✔                           |                           ✔                           |                           ✔                           |                           ✔                           |                           ✔                            |                           ✔                            |
|   2.2   |                           ❌                            |                           ❌                            |                           ✔                            |                           ✔                            |                           ✔                            |                           ✔                           |                           ✔                           |                           ✔                           |                           ✔                           |                           ✔                            |                           ✔                            |
|   2.3   |                           ❌                            |                           ❌                            |                           ✔                            |                           ✔                            |                           ✔                            |                           ✔                           |                           ✔                           |                           ✔                           |                           ✔                           |                           ✔                            |                           ✔                            |
|   2.4   |                           ❌                            |                           ❌                            |                           ✔                            |                           ✔                            |                           ✔                            |                           ✔                           |                           ✔                           |                           ✔                           |                           ✔                           |                           ✔                            |                           ✔                            |
|   2.5   |                           ❌                            |                           ❌                            |                           ✔                            |                           ✔                            |                           ✔                            |                           ✔                           |                           ✔                           |                           ✔                           |                           ✔                           |                           ✔                            |                           ✔                            |
|   2.6   |                           ❌                            |                           ❌                            |                           ✔                            |                           ✔                            |                           ✔                            |                           ✔                           |                           ✔                           |                           ✔                           |                           ✔                           |                           ✔                            |                           ✔                            |
|   3.1   |                           ❌                            |                           ✔                            |                           ✔                            |                           ✔                            |                           ✔                            |                           ✔                           |                           ✔                           |                           ✔                           |                           ✔                           |                           ✔                            |                           ✔                            |
|   4.1   |                           ❌                            |                           ❌                            |                           ❌                            |                           ✔                            |                           ✔                            |                           ✔                           |                           ✔                           |                           ✔                           |                           ✔                           |                           ✔                            |                           ✔                            |
|   4.2   |                           ❌                            |                           ❌                            |                           ❌                            |                           ✔                            |                           ✔                            |                           ✔                           |                           ✔                           |                           ✔                           |                           ✔                           |                           ✔                            |                           ✔                            |
|   5.1   |                           ❌                            |                           ❌                            |                           ❌                            |                           ✔                            |                           ✔                            |                           ✔                           |                           ✔                           |                           ✔                           |                           ✔                           |                           ✔                            |                           ✔                            |
|   6.1   |                           ❌                            |                           ❌                            |                           ❌                            |                           ❌                            |                           ✔                            |                           ✔                           |                           ✔                           |                           ✔                           |                           ✔                           |                           ✔                            |                           ✔                            |
|   6.2   |                           ❌                            |                           ❌                            |                           ❌                            |                           ❌                            |                           ❌                            |                           ✔                           |                           ✔                           |                           ✔                           |                           ✔                           |                           ✔                            |                           ✔                            |
|   6.3   |                           ❌                            |                           ❌                            |                           ❌                            |                           ❌                            |                           ✔                            |                           ✔                           |                           ✔                           |                           ✔                           |                           ✔                           |                           ✔                            |                           ✔                            |
|   6.4   |                           ❌                            |                           ❌                            |                           ❌                            |                           ❌                            |                           ✔                            |                           ✔                           |                           ✔                           |                           ✔                           |                           ✔                           |                           ✔                            |                           ✔                            |
|   6.5   |                           ❌                            |                           ❌                            |                           ❌                            |                           ❌                            |                           ❌                            |                           ✔                           |                           ✔                           |                           ✔                           |                           ✔                           |                           ✔                            |                           ✔                            |
|   6.6   |                           ❌                            |                           ❌                            |                           ❌                            |                           ❌                            |                           ✔                            |                           ✔                           |                           ✔                           |                           ✔                           |                           ✔                           |                           ✔                            |                           ✔                            |
|   7.1   |                           ❌                            |                           ❌                            |                           ❌                            |                           ❌                            |                           ✔                            |                           ✔                           |                           ✔                           |                           ✔                           |                           ✔                           |                           ✔                            |                           ✔                            |
|   8.1   |                           ❌                            |                           ❌                            |                           ❌                            |                           ❌                            |                           ❌                            |                           ✔                           |                           ✔                           |                           ✔                           |                           ✔                           |                           ✔                            |                           ✔                            |
|   9.1   |                           ❌                            |                           ❌                            |                           ❌                            |                           ❌                            |                           ❌                            |                           ✔                           |                           ✔                           |                           ✔                           |                           ✔                           |                           ✔                            |                           ✔                            |
|   9.2   |                           ❌                            |                           ❌                            |                           ❌                            |                           ❌                            |                           ❌                            |                           ✔                           |                           ✔                           |                           ✔                           |                           ✔                           |                           ✔                            |                           ✔                            |
|  10.1   |                           ❌                            |                           ❌                            |                           ❌                            |                           ✔                            |                           ✔                            |                           ✔                           |                           ✔                           |                           ✔                           |                           ✔                           |                           ✔                            |                           ✔                            |
|  10.2   |                           ❌                            |                           ❌                            |                           ❌                            |                           ✔                            |                           ✔                            |                           ✔                           |                           ✔                           |                           ✔                           |                           ✔                           |                           ✔                            |                           ✔                            |
|  11.1   |                           ❌                            |                           ❌                            |                           ❌                            |                           ❌                            |                           ❌                            |                           ✔                           |                           ✔                           |                           ✔                           |                           ✔                           |                           ✔                            |                           ✔                            |
|  11.3   |                           ❌                            |                           ❌                            |                           ❌                            |                           ❌                            |                           ❌                            |                           ✔                           |                           ✔                           |                           ✔                           |                           ✔                           |                           ✔                            |                           ✔                            |
|  12.1   |                           ❌                            |                           ✔                            |                           ✔                            |                           ✔                            |                           ✔                            |                           ✔                           |                           ✔                           |                           ✔                           |                           ✔                           |                           ✔                            |                           ✔                            |
|  13.1   |                           ❌                            |                           ✔                            |                           ✔                            |                           ✔                            |                           ✔                            |                           ✔                           |                           ✔                           |                           ✔                           |                           ✔                           |                           ✔                            |                           ✔                            |
|  13.2   |                           ❌                            |                           ✔                            |                           ✔                            |                           ✔                            |                           ✔                            |                           ✔                           |                           ✔                           |                           ✔                           |                           ✔                           |                           ✔                            |                           ✔                            |
|  14.1   |                           ❌                            |                           ❌                            |                           ❌                            |                           ❌                            |                           ❌                            |                           ❌                           |                           ❌                           |                           ✔                           |                           ✔                           |                           ✔                            |                           ✔                            |
|  15.1   |                           ❌                            |                           ❌                            |                           ❌                            |                           ❌                            |                           ❌                            |                           ❌                           |                           ✔                           |                           ✔                           |                           ✔                           |                           ✔                            |                           ✔                            |
## Bibliographie

Voici les différentes ressource techniques consultées lors lu développement de mon projet :

* Le documentation officielle Python : <https://docs.python.org/3/>
* MDN web docs, recueil très complet concernant le HTML, CSS, et JavaScript, créer par Mozilla : <https://developer.mozilla.org/en-US/>
* Site de questions en lignes pour développeurs de tout les horizons : <https://stackoverflow.com/>
* Le guide de style Airbnb, spécialisé pour la syntaxe JavaScript : <https://github.com/airbnb/javascript>
* Les sources des librairies externes utilisées lors de ce projet :
  * Documentation officielle de Flask : <https://palletsprojects.com/p/flask/>
  * Documentation officielle de Jinja2 : <https://jinja.palletsprojects.com/en/2.11.x/>
  * Documentation officielle de Flask-Login : <https://flask-login.readthedocs.io/en/latest/>
  * Exemple d'utilisation de flask-swagger : <https://pypi.org/project/flask-swagger/>
  * Documentation complète de Mysql Connector/Python : <https://dev.mysql.com/doc/connector-python/en/>
  * Explications de ce qu'est Swagger : <https://swagger.io/tools/swagger-ui/>
  * Documentation officielle de JquerUI : <https://jqueryui.com/>
  * Sources de SwaggerUI, répertoire distant comportant les fichiers utilisés pour l'affichage de mes points d'entrés pour mon API interne : <https://github.com/swagger-api/swagger-ui>

## Glossaire

|                                        Termes | Explications                                                 |
| --------------------------------------------: | :----------------------------------------------------------- |
|            **Anime**<br />(Anglais : *anime*) | Série, films ou épisodes spéciaux en dessins animé d'origine japonaise. |
|             **Liste**<br />(Anglais : *list*) | Conteneur pouvant accueil 1 ou plusieurs animes en son sein afin de pouvoir organisé correctement sa collection. |
|          **Statut**<br />(Anglais : *status*) | État de visionnement d'un anime. Ce dernier peut être *Complété*, *En cours*, *Abandonné* ou *Planifié.* |
|       **Favoris**<br />(Anglais : *favorite*) | Anime que l'utilisateur aime particulièrement beaucoup.      |
|                                     **Route** | Url ne pointant pas sur un fichier directement mais fonctionnant comme une requête faite au serveur afin d'afficher des données ou faire une action précise. |
|                                  **Template** | Page HTML comportant une mise en page précise et où les données sont inséré dynamiquement grâce à des requête ou au back-end lors du chargement de la page. |
|                                  **Back-end** | Partie caché d'une application permettant de communiquer avec tout le côté serveur. Cela comprend la base de données, l'authentification, etc... |
|                                 **Front-end** | Partie visible par l'utilisateur d'une application. C'est cette partie qui comprend entre autre toute la partie ergonomie et les interfaces. |
|                                **Librairies** | Ensemble de fonctionnalités externes au projet conçu par des développeur pour des développeur. |
|                                    **Script** | Programme chargé d'exécuter une tâche pré-défini permettant habituellement d'automatisé des actions. |
| **API** (*Application Programming Interface*) | Permet d'avoir accès à des fonctionnalités d'un site facilement. En web, ces accesseurs sont des urls définissant clairement ce qu'elles font (Exemple : */get/users* ➡ récupère les utilisateurs). |
|                                 **Framework** | En web, ensemble d'outils et de fonctionnalités construit spécialement pour le support de services web, gestion de ressources et déploiement web. Un framework apporte un manière standardisé de réalisé un projet et automatise des protocole fastidieux si fait manuellement . |


## Conclusion

### Difficultés majeures rencontrées

Durant tout le développement de mon projet, aucun problème bloquant n'a surgi. Voici cependant la liste des soucis majeurs que j'ai rencontrés :

* > L'outil de fusion de PDF que j'utilisais - [pdfunite](http://manpages.ubuntu.com/manpages/bionic/man1/pdfunite.1.html) - ne prenait pas en charge les titres lors de la fusion de plusieurs PDF. Ainsi, si un PDF comportait des titres, après la fusion sa fusion avec les autres documents, les titres étaient considérés comme simple texte.

  ➡ J'ai pu corriger ce souci en changeant de librairie de fusion de document PDF. La recherche d'une nouvelle librairie n'a pas été compliquée du tout car il existe un nombre élevé de librairies permettant de fusionner des PDF, dont [pdftk](https://www.pdflabs.com/tools/pdftk-the-pdf-toolkit/) et le didacticiel disponible à [cette adresse](https://www.ostechnix.com/how-to-merge-pdf-files-in-command-line-on-linux/).

* > Lors de la synchronisation, j'utilise des timestamps pour savoir quels enregistrements ont été modifiés. Cependant, j'utilisais un format différent entre ma base Sqlite3 et MySQL. Dans Sqlite3, le format utilisé était `%Y-%m-%d %H:%M:%f` ce qui donne `2020-06-08 09:08:32.276`. Les millisecondes sont présentes avec ce format. Or, le format utilisé par défaut dans MySQL est `%Y-%m-%d %H:%M:%S` ce qui donne `2020-06-08 09:08:32`. Cette différence de format faisait que lorsqu'un timestamp Sqlite3 dont les millisecondes sont plus grandes que `.500`, ce timestamp était arrondi vers le haut et donc mes timestamps étaient différents.

  ➡ Le souci n'était de loin pas compliqué à régler mais j'ai mis un certain temps avant de trouver ce qui causait un différent entre Sqlite3 et MySQL. Une fois la cause trouvée, j'ai simplement fait en sorte que la date que j'insère dans Sqlite3 ne comporte pas les millisecondes En procédant ainsi, la synchronisation se fait sans problème.

### Améliorations possibles

Étant donnée la courte période mise à disposition, il est clair que des améliorations sont possibles sur les fonctionnalités existantes. Voici un aperçu de ce qui pourrait être amélioré :

* Ajouter la fonctionnalité de pouvoir modifier son profile. Cela comporte le pseudo, l'email et le mot de passe ;

* Faire en sorte que l'interface du site soit *responsive design* (qu'il s'adapte sur tout type d'écran). Pour le moment, cette fonctionnalité n'est qu'à demi implémentée ;

* Proposer davantage de résultats lors d'une recherche. Pour le moment, seuls les neufs résultats les plus adéquats par rapport à la chaine recherché apparaissent ;

* Modifier la fonctionnalité de synchronisation unidirectionnelle entre Sqlite3 et MySQL. Pour le moment, l'algorithme utilisé est relativement efficace mais il pourrait être amélioré, par exemple, en stockant le timestamp de la dernière synchronisation dans une table, en supprimant tous les enregistrements qui ne sont plus présents dans Sqlite3 de MySQL, en ne sélectionnant que les enregistrements dont la date est supérieure ou égale à la dernière synchronisation, en mettant à jours les enregistrements MySQL et en ajoutant les enregistrements manquant. Cette façon de faire permettrait à l'algorithme d'être beaucoup plus rapide qu'actuellement.


Outre les fonctionnalités existantes, j'ai pensé à ces quelques idées durant le développement de l'application :

* Ajouter la fonctionnalité de pouvoir se faire une liste d'amis en cherchant le pseudo de l'utilisateur dans un champs prévu à cet effet et ensuite avoir une page dédiée à l'affichage de cette dite liste d'amis afin de pouvoir aller voir le profil de ces derniers ;
* Ajouter un système de rôle permettant aux administrateurs de pouvoir gérer les animes sans que les utilisateurs puissent le faire pour éviter toute fausse manipulation ;
* Ajouter la fonctionnalité permettant aux utilisateurs de mettre une note à un anime et une progression de visionnage (nombre d'épisodes regardés) ;
* Modifier le contenu des activités pour ajouter celles des amis.

### Bilan personnel

Ce projet m'a énormément plus. Le sujet était parfait pour moi : j'adore réaliser des projets en Python, surtout web, et je suis passionné par les animes. Le fait de pouvoir lier ces deux passions était très agréable.

Je trouve très plaisant d'utiliser cette application de par sa simplicité et son contenu fourni. Le fait d'écrire une documentation aussi volumineuse était une première pour moi ! Ce fût non seulement satisfaisant mais aussi très enrichissant. J'ai en effet, appris quantité de choses.

### Remerciements

J'apporte mes remerciements à :

* M. Pascal Bonvin pour son suivi assidu lors de ce TPI ;
* M. Nicolas Ettlin pour ses conseils avisés concernant l'utilisation d'eslint et quelques techniques CSS ;
* Ma famille pour la relecture et l'aide à la correction orthographique et grammaticale.