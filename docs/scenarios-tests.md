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