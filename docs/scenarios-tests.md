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