# Journal de bord TPI - Tanguy CAVAGNA

## J1 : lundi 25 mai 2020

### Objectifs

L'objectif de cette journée est de lire l'énoncé dans son intégralité afin de prendre connaissance du cahier des charges, extraire les *user stories* de ce dernier pour pouvoir correctement rédiger mon *product backlog* et enfin rédiger les scénarios de tests fonctionnels, indispensable pour le bon fonctionnement de mon projet.

### Déroulement

Je commence ma journée à 8h00. M. Terrond m'a fait parvenir mon énoncé la veille, que j'ai lu avec attention ce dernier. Par ce biais, j'ai complété avec succès la première étape de la **méthodologie en 6 étapes**, méthodologie que je vais utiliser durant tout le déroulement de ce TPI : *__S'informer__*.

J'ai quelques points incertains concernant mon énoncé dont un quelque peu embêtant. Je poserai mes questions à mon formateur durant la matinée. Je vais maintenant commencer à ***Planifier***, secondes étape de la méthodologie utilisée. Je séparerai mes journée en tranche de 4 heures, soit par demi-journée, et remplirai des différentes tranches horaires avec les *user stories* extraites de mon cahier des charges.

8h15 : J'ai décidé d'utiliser des alias afin de nommer les jours de travail mis à disposition pour le TPI. Les jours seront nommer de **J1** à **J11**. Voici les alias :

* J1 : lundi 25 mai 2020
* J2 : mardi 26 mai 2020
* J3 : mercredi 27 mai 2020
* J4 : jeudi 28 mai 2020
* J5 : vendredi 29 mai 2020
* J6 : mardi 2 juin 2020
* J7 : mercredi 3 juin 2020
* J8 : jeudi 4 juin 2020
* J9 : vendredi 5 juin 2020
* J10 : lundi 8 juin 2020
* J11 : mardi 9 juin 2020

8h25 : Lors de la création des *user stories* j'ai remarqué qu'il me fallait décider d'une manière de priorisé les tâches. J'ai opté pour me basé sur la méthode [MoSCoW](https://en.wikipedia.org/wiki/MoSCoW_method). Cependant les niveaux de priorité ne correspondaient pas entièrement pour un TPI. J'ai alors décider de modifier les intitulé :

* **Must** devient 🚫 **Bloquant**
* **Should** devient 💥 **Critique**
* **Could** devient ❗ **Important**
* **Won't** devient ❓ **Secondaire**

J'ai aussi décidé d'utiliser la syntaxe suivante afin de présenter mes *user stories* :

| Nom                            | S<n° de la *story*\> : <Nom de la *user story*\>             |
| ------------------------------ | ------------------------------------------------------------ |
| **Description (*user story*)** | <Description de la story pour connaître avec précision le but à atteindre\> |
| **Critère d'acceptation**      | <n° des tests à passé pour valider cette *story*\>           |
| **Priorité**                   | <Priorité de la *story*\>                                    |

9h : J'ai fait un script bash me permettant un rassembler tout mes fichiers Markdown de ma documentation dans un seul et même fichier. Ceci est nécessaire car je prévois de publier ma documentation en ligne, à l'aide du site [readthedocs.org](https://readthedocs.org).

10h : En plus de la documentation publique, il faut une version PDF. Pour ce faire j'utilise le logiciel [Typora](https://typora.io) pour exporter mon fichier réunissant toute ma documentation en PDF. Une fois cela fait, j'utilise un autre script bash que j'ai réalisé permettant de fusionner plusieurs fichiers PDF en un seul. Ce dernier se nomme : `Rapport du TPI et documentation technique`. Il contient le rapport, les annexes, le résumé, l'énoncé, le journal de bord, et le code source.

10h30 : Descriptif de mes outils de bureautique : j'utilise [Typora](https://typora.io) (un éditeur Markdown compatible sous tout OS) pour rédiger l'entièreté de ma documentation. La création des fichiers PDF est faite grâce à l'export vers PDF de Typora ainsi qu'à un script écrit par moi-même.

Concernant le style appliqué à ma documentation, j'ai utilisé la couleur <img src="https://i.loli.net/2020/05/25/pqzGhglItRj3fkJ.png" style="zoom:25%;" /> <span style="color: #C4C4C4">#</span>**006EDB** comme principale. La police est Poppins, aussi utilisée dans le projet en lui même.

10h50 : J'ai eu un rendez-vous GMeet avec mon formateur pour vérifier que tout allait bien. J'ai poser la question suivante et voici la réponse donnée :

> Est-ce que le planning que vous m'avez donné est celui qu'il faudra utilisé ?

➡ Le planning que j'ai donné est un modèle permettant de suivre de façon basique l'avancée du projet. Si vous avez un planning plus précis, vous pouvez sans autre l'utiliser et comparer ensuite le vôtre avec celui que j'ai donné.

11h25 : J'ai terminé la rédaction de mon *product backlog* temporaire. Des modifications peuvent encore être apportés si j'en trouve le besoin.

11h45 : J'ai compilé une version de test de ma documentation pour vérifier qu'il ni aie pas d'erreur. Je prend ma pause de midi.

---

12h50 : Reprise de la journée. Je m'attaque maintenant au diagramme de Gantt. J'ai choisi de le réalisé avec un tableau HTML car je ne suis pas à l'aise avec les outils spécialisé comme Gantter.

14h15 : J'ai remarqué un soucis lors de la fusion des fichiers Markdown. Une partie d'un fichier se dédouble mais je ne sais pas encore pourquoi.

15h50 : Mon soucis de duplication est résolu. Ce problème venait du fait que j'ajoutais ma table des matières sans supprimer le contenu précédent. Désormais, je supprime le contenu du fichier avant de le remplacer par le contenu mis-à-jour avec la table des matières. Je vais pouvoir commencer l'écriture des scénarios de tests fonctionnels.

16h45 : J'ai écris une partie des scénarios de tests. Il m'en reste encore quelques un que j'ajouterai demain matin.

### Bilan

La journées c'est plutôt bien passée. J'ai cependant pris un peu de retard sur la rédaction des scénarios de tests à cause de mon problème de duplication lors de la compilation de la documentation. Cependant, ceci reste un écart que très minime sur mon planning. Je sort tout de mais satisfait de cette première journée.

## J2 : mardi 26 mai 2020

### Objectifs

L'objectif de cette journée est premièrement de rattraper le peu de retard que j'ai eu hier sur les scénarios de tests. Ensuite, je ferai le modèle de base de données, je configurerai l'application Flask, et je ferai le code permettant d'importer les données.

### Déroulement

8h : Je commence ma journée. Je dois finir les scénarios de tests que je n'avais pas pu terminer hier. Ceci ne devrait pas me prendre beaucoup de temps.

8h30 : J'ai terminé les scénarios. Je passe maintenant à la conception de la base de données. Grâce à l'énoncé, j'ai pu extraire les différentes tables du projet : `anime`, `status`, `type`, `url`, `list`, `list_has_anime`, `user`, `user_has_list`, `user_has_favorite`.

8h55 : J'ai réalisé le modèle de base de données que voici :

![](https://i.loli.net/2020/05/26/CiqWlPVISstmKn2.png)

9h : Je vais faire la partie *Base de donnée* du chapitre *Implémentation* de la documentation étant donné que j'ai toutes les informations nécessaire.

9h25 : J'ai terminé de documenter la partie *Base de données*. J'y ai mis le modèle ci-dessus ainsi que le dictionnaire de données.

9h30 : Je configure l'application Flask pour pouvoir avoir un environnement de développement fonctionnel et ainsi pouvoir faire la suite du projet.

J'ai inscrit une `secret_key` à l'application Flask. Cette clef est utilisé dans les systèmes d'encryptions. Flask lui-même n'a pas besoin de cette clef mais d'autre librairies externes, tel que `flask-login`, que j'utiliserai afin de pouvoir connecter un utilisateur, doit avoir cette clef. La valeur de cette clef est `Super` en Sha256.

9h55 : J'ai une application Flask basique fonctionnelle. Je peux rendre des vues depuis une route sans problèmes.

10h : J'ai mis en place le système de documentation automatique d'API : [Swagger](https://swagger.io).

Pour que ce système puisse être mis en place, il faut une librairie externe nommé `flask_swagger`. De plus, certains fichiers sont indispensable au bon fonctionnement de Swagger. Le plus primordiale est la page HTML. J'ai décidé de la nommé `endpoints.html` et de la placé dans le dossier `templates`. Cette page est disponible [ici](https://github.com/swagger-api/swagger-ui/blob/master/dist/index.html). Cependant, je l'ai adapté pour qu'elle soit correctement implémentée dans l'application FLask.

En plus de la page HTML, il nous faut rajouter 2 fichiers `javascript` qui iront dans le dossier `static/js`, 2 images qui iront dans le `static/img` et enfin 1 fichier `css` qui ira dans le `static/css`. Voici le lien pour télécharger les fichiers :

- [swagger-ui-bundle.js](https://github.com/swagger-api/swagger-ui/blob/master/dist/swagger-ui-bundle.js)
- [swagger-ui-standalone-preset.js](https://github.com/swagger-api/swagger-ui/blob/master/dist/swagger-ui-standalone-preset.js.map)
- [favicon-16x16.png](https://github.com/swagger-api/swagger-ui/blob/master/dist/favicon-16x16.png)
- [favicon-32x32.png](https://github.com/swagger-api/swagger-ui/blob/master/dist/favicon-32x32.png)
- [swagger-ui.css](https://github.com/swagger-api/swagger-ui/blob/master/dist/swagger-ui.css)

La structure du dossier `static` ressemble désormais à ceci :

```
Animanga
└── static
	├── css
	│   └── swagger-ui.css
    ├── js
    │   ├── swagger-ui-bundle.js
    │   └── swagger-ui-standalone-preset.js
    └── img
        ├── favicon-16x16.png
        └── favicon-32x32.png
```

10h25 : J'ai installer la police Poppins en local. De ce fait, je n'aurai pas de soucis si le site perd la connexion à internet et que les polices sont chargées depuis Google Fonts.

10h30 : Je commence maintenant l'importation des données en base.

11h40 : J'ai terminé l'importation des types et statuts des animes depuis le fichier JSON. Il me reste à faire l'importation des animes eux même. Je prend ma pause de midi.

---

13h : Reprise de la journée et continuation de l'importation des données dans la base de données.

14h : J'ai terminé l'import des données et tout semble parfaitement bien s'ajouter en base. Étant donné que j'ai un peu d'avance, je vais mettre ma documentation en ligne sur [readthedocs.org](https://readthedocs.org/). Le site hébergeant la documentation utilise [Mkdocs](https://www.mkdocs.org/) pour convertir la documentation de Markdown à HTML. C'est pourquoi j'ai installé mkdocs dans [WSL 2](https://docs.microsoft.com/en-us/windows/wsl/wsl2-index) sur ma machine pour vérifier si ma documentation compilait correctement.

14h15 : La documentation est en ligne à l'adresse : <https://animanga.readthedocs.io/fr/latest/>.

Pour le moment, étant donné que je n'ai pas encore mis en place la connexion, je ne peux effectuer mes tests que manuellement. Cependant, dès lors que la connexion sera mise en place, j'utiliserai [Katalon Recorder](https://chrome.google.com/webstore/detail/katalon-recorder-selenium/ljdobmomdgdljniojadhoplhkpialdid) pour automatiser mes tests.

14h25 : J'ai effectué le test *3.1* pour vérifier que mes données soient correctement importées. Comme j'ai de l'avance de vais faire l'affichage de la *landing page*.

15h20 : J'ai terminé l'implémentation de la *landing page*.  Pour le moment je ne peux tester le basculement de l'état connecté à l'état déconnecté que via la variable `is_authenticated` de que je change dans le fichier `routes.py`. Demain je pourrai changé puisque je met en place la connexion et l'inscription. Je n'aurai donc plus besoin de cette variable. Le test *11.1* passe concernant l'affichage de la *landing page*.

Je vais configurer deux vérificateurs de syntaxe différent pour mon projet. Le premier est [pylint](https://www.pylint.org/) pour Python, et le second est [eslint](https://eslint.org/) pour le JavaScript. Pour eslint, je vais utilisé un preset de vérification : airbnb. Cela me permet d'écrire mes script javaScript dans un cadre syntaxique strict et donc de ne pas sortir des conventions actuelles.

15h30 : Eslint est installé et je lance la commande `npm run lint static/js` pour vérifier mes fichiers JavaScript.

15h35 : J'ai corrigé les erreurs que eslint m'avait montré et je m'attaque maintenant à pylint.

16h : Le vérification de syntaxe pylint fonctionne correctement. Je lance la commande `python3 -m pylint --output-format=colorized packages` pour vérifier la syntaxe des fichiers se trouvant dans le dossier `packages`.

16h10 : J'ai corrigé les erreurs relevées par pylint. Je vais mettre à jour mon planning et mes scénarios de tests afin d'ajouter la vérification syntaxique.

16h30 : J'ai ajouté la vérification syntaxique dans le planning comme *user story* et j'ai créer un test pour le Python et un pour le JavaScript afin de validé la *user story*.


### Bilan

Je suis très content de l'avancement d'aujourd'hui. J'ai eu un peu de retard hier mais très vite rattrapé ce matin. J'ai réussi à prendre un peu d'avance dans le projet et donc je suis très confiant pour la suite. Cela m'a permis de rajouté la vérification syntaxique pour Python et pour JavaScript.

## J3 : mercredi 27 mai 2020

### Objectifs

L'objectif de cette journée est de faire le système de connexion et d'inscription. Comme j'ai déjà fait l'affichage de la landing page hier, je pense peut être avancer sur une autre tâche.

### Déroulement

8h : Je commence à faire la partie inscription Je vais créer un contrôleur pour les utilisateur pour mieux pouvoir gérer ces derniers.

8h30 : J'ai fait le formulaire HTML et je commence à faire la partie prise en charges de ce dernier.

9h : J'ai eu la visite de M. Terrond. M. Bouille étant pris à la Protection Civile, il n'a pas pu être présent. Le but de cette visite était de voir si tout ce passe bien et de répondre au possible questions. Étant donné que tout ce passe bien pour moi, la visite n'a duré que très peu de temps.

9h40 : J'ai des soucis avec mon système d'export de documentation vers PDF. L'export ne s'effectue pas mais aucun moyen de savoir quelle est la cause. Je cherche activement ce qui pourrait poser problème.

10h20 : J'ai réussis à régler le problème d'export pour le moment mais rien ne me dit que cela ne réarrivera pas. Si cela doit être le cas, j'ai un moyen auxiliaire d'exporter ma documentation. Je me remet à travailler sur la partie inscription.

11h45 : J'ai terminé l'inscription. L'insère de nouvel utilisateur semble fonctionner. Avec les quelques minutes qu'il me reste avant la pause de midi, je met en place des automations Katalon Recorder pour les futurs tests.

12h : J'ai terminé l'automation du test fonctionnel d'inscription avec valeurs correctes. Je ferai les autres dès que j'aurai du temps aujourd'hui. Je prend ma pause de midi.

---

13h : Je me remet au travail en commençant la partie connexion. Étant donné le retard pris à cause du problème d'exportation vers PDF, je ne commence la connexion que maintenant. Ceci ne va causer d'autre retards car j'avais pris de l'avance hier concernant la *landing page* que j'aurais du réaliser aujourd'hui.

13h40 : La *connexion* est terminée et fonctionne à merveille. Je créer maintenant des tests d'automations pour éviter de retapé tout le temps la même chose lors des futurs tests. J'utilise Katalon Recorder pour cela.

14h20 : Je vais maintenant pouvoir optimiser un peu le code pour l'inscription et la connexion étant donné que je n'ai pas pu le faire ce matin à cause de mon soucis d'erreur d'export de la documentation.

15h20 : J'ai eu un rendez-vous avec mon référent TPI pour faire un point. Comme tout ce passe bien le rendez-vous n'a duré que très peu de temps et je suis tout de suite retourné travailler.

17h : J'ai terminé l'optimisation de la validation des champs. Je me suis basé sur la libraire [wtforms](https://github.com/Khan/wtforms/tree/master/wtforms). Cette librairie est utilisé pour générer et valider automatiquement des formulaires. Comme cette libraire est trop imposant pour un TPI, j'ai décidé de m'inspirer de cette dernière uniquement pour la partie validation de formulaire. Je demanderai demain matin à mon référent s'il est d'accord que je garde cette manière de valider mes champs de formulaire ou si c'est toujours trop imposant. 

En plus de cela, j'ai configurer Katalon Recorder pour prendre en compte la connexion aussi. J'ai maintenant un dossier à la racine de mon projet nommé `tests` qui contient le fichier HTML contenant tout les *tests cases* pour Katalon Recorder.

### Bilan

Je suis plutôt content de ma journée. J'ai pu correctement faire le code de l'inscription ainsi que la connexion. De plus, comme j'avais du temps restant avant la fin de la journée, j'ai décidé de mettre en place Katalon Recorder afin d'automatiser mes tests fonctionnels et j'ai aussi décidé d'optimiser le code de validation des champs de mes formulaires. Je n'ai cependant toujours pas fait validé cette idée d'optimisation donc je le ferai demain matin.

## J4 : jeudi 28 mai 2020

### Objectifs

### Déroulement

8h : J'ai réfléchi hier soir et j'ai réalisé que ce que j'avais entrepris la veille sur l'optimisation de la validation des champs était beaucoup trop imposant. Je me décide à le refaire de manière bien plus légère.

9h20 : J'ai terminé ma nouvelle version de l'optimisation des champs. Bien plus simple à lire et à maintenir. Très content du résultat. Je commence maintenant la partie recherche d'anime. Une des parties les plus importantes du projet.

Pour les recherche en base, j'ai une table virtuelle Sqlite3 pour pouvoir faire de la recherche Fulltext. Sqlite3 ne supporte pas le Fulltexte sur une table standard, il faut créer une table virtuelle avec un template supportant Fulltext. Tout le procédé est expliqué [ici](https://www.sqlitetutorial.net/sqlite-full-text-search/).

10h10 : La recherche par chaine de caractères est terminé. Il me reste à faire l'affichage mais ceci ne sera pas long. Je le ferai cet après-midi car maintenant je vais faire la récupération d'un anime aléatoire.

10h20 : J'ai eu un rendez-vous GMeet avec mon référent pour voir mon avancement et pour lui poser une question concernant la validation des champs. J'ai demandé si ce que j'avais fais était  bien et si je pouvais le garder. Sa réponse à été positive et j'ai pu continuer mon projet.

10h40 : La récupération d'un anime aléatoirement est terminé. J'ai remarqué en programmant que j'ai des **try/except** dans pratiquement toutes les méthodes de classes. Le **except** est toujours le même mais rien n'est centralisé. J'ai alors décidé de commencer à faire une fonction centralisant tout les logs.

11h35 : La fonction de log est terminé et j'ai placé dans tout les **except** un appel à cette méthode.

Comme j'ai encore un peu de temps avant la pause de midi, je décide de commencé à affiché les résultats de la recherche.

12h : J'ai terminé l'affichage des résultats de la recherche et je prend ma pause de midi.

---

13h : Je reprend le travail en faisant la prise en charge de la barre de recherche.

13h20 : J'ai terminé la prise en charge de la barre de recherche et je commende maintenant à faire l'affichage de la carte pour les animes. Pour la barre de recherche je suis parti sur deux manières différentes de l'affiché. La première, classique, est de cliquer sur la 🔍. Une modale s'affichage alors avec un champ de type de texte pour y entré notre recherche, ainsi qu'une crois sur la droite pour effacé le contenu du champ. La seconde manière est par le raccourci <kbd>Ctrl</kbd> + <kbd>S</kbd>.

14h30 : J'ai terminé d'affiché la carte (modal) de l'anime. Je vais commencé la mise à jour de l'anime pour l'utilisateur connecté.

17h : Je n'ai pas terminé la mise à jour de l'anime mais comme je doit le faire demain normalement ce n'est pas un soucis.

### Bilan

Cette journée était très sympa. Je n'ai pas eu de problèmes et j'ai pris un peu d'avance. Le journal n'est pas très rempli pour cet après-midi mais tout ce qu'il y a a savoir sur ma journée y est. Rien de spéciale ne c'est passé. Je suis très content d'avoir mis en place les automations Katalon car dès que je change quelque chose, je peux lancé les tests pour voir si rien n'a régressé.

## J5 : vendredi 29 mai 2020

### Objectif

Le but de cette journée est de faire la mise à jour de l'anime pour un utilisateur, afficher sa page de profile, et afficher ses favoris. Je pense que je vais faire l'affichage des favoris en même temps que la mise à jour de l'anime pour pouvoir avoir un retour visuel sur le bon fonctionnement ou pas du code.

### Déroulement

8h : Je commence ma journée par la mise à jour de l'anime. Je ne pense pas que cela va me prendre toute la matinée comme prévue et c'est donc aussi pour ceci que je vais faire la partie affichage des favoris en même temps.

9h30 : J'ai terminé la partie mise à jour de l'état de favoris pour les animes. Je vais maintenant les afficher pour pourvoir avoir un retour visuel et aussi pour avoir un éléments à tester en case de réussite lors des tests d'automations.

### Bilan

