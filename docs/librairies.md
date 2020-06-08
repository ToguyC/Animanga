## Librairies et outils externes

### Pip et NPM

<img style="float: right; margin-left: 25px; width: 30%" src="https://i.imgur.com/Z4wYwdB.png">[Pip](https://pypi.org/project/pip/) et [NPM](https://www.npmjs.com/) sont deux gestionnaires de dépendances que j'ai utilisé pour mon TPI. Pip est le gestionnaire des dépendances Python tandis que NPM est sont équivalent pour JavaScript. Ces deux gestionnaires m'ont permis d'inclure toutes les librairies externe que j'avais besoin pour mon TPI. Ceci me permet de ne pas avoir à télécharger manuellement les libraires et à les mettre dans mon projet. Leur utilisation m'a permis de grandement facilité le développement du TPI et d'avoir des dépendances toujours à jour.

### Flask

<img style="float: right; margin-left: 25px; width: 30%" src="https://upload.wikimedia.org/wikipedia/commons/3/3c/Flask_logo.svg">[Flask](https://palletsprojects.com/p/flask/) est un micro framework web écrit en Python. Aucune couche autre que l'hébergement web n'est présent dans ce micro framework. Flask à été créer par [Armin Ronacher](https://en.wikipedia.org/wiki/Armin_Ronacher), membre de [Pocoo](https://www.pocoo.org/), un groupe de développeurs Python formé en 2004, le 1<sup>er</sup> avril 2010. J'ai choisi d'utiliser ce framework pour mon TPI car il m'a permis d'aisément :

* Héberger mon site en local ainsi que de pouvoir créer des routes web. Ces dernières sont url écrites dans la barre d'adresse du navigateur. Elles sont utilisées pour éviter de devoir écrire en dure les nom des fichiers à afficher ainsi que de pouvoir exécuter du code avant d'afficher la page à l'utilisateur afin de récupérer des informations nécessaire au bon affichage des informations dynamiques. Un bon exemple d'utilisation est la page d'accueil : si l'utilisateur n'est pas connecté, un fond contenant une image est affiché et la barre de navigation su site ne permet que d'avoir accès à l'accueil, la page à propos, la page de connexion et enfin d'inscription. L'informations comme quoi l'utilisateur n'est pas connecté est récupérée avant que la page soit affiché.
* Configurer le debug de mon site de manière générale. Il est possible de données des paramètres de configuration à l'application Flask afin de facilité le développement. J'ai utilisé ces paramètres pour facilité le rafraichissement des pages dès lors qu'une modification est détectée dans un fichier.

### Jinja

<img style="float: right; margin-left: 25px; width: 30%" src="https://upload.wikimedia.org/wikipedia/commons/8/87/Jinja_software_logo.svg">[Jinja](https://jinja.palletsprojects.com/en/2.11.x/) est un moteur de modèle de page web pour Python. Il a été créer par [Armin Ronacher](https://en.wikipedia.org/wiki/Armin_Ronacher). Sa syntaxe est relativement identique au moteur de modèle Django mais adaptée pour la syntaxe de Python. Ce moteur de modèle est celui par défaut de [Flask](###Flask). 

### Flask-Login

[Flask-Login](https://flask-login.readthedocs.io/en/latest/) donne accès à un gestionnaire de sessions pour [Flask](###Flask). Il prend en compte les tâches standards comme la connexion, la déconnexion, et l'enregistrement de l'utilisateur en session sur une long période de temps. Dans mon TPI je l'utilise afin de connecter / déconnecter mes utilisateur et pour pouvoir stocker leurs informations en session durant leur utilisation du site.

### Flask-Swagger

[Flask-Swagger](https://pypi.org/project/flask-swagger/) donne accès à une méthode (swagger) qui inspecte les routes de [Flask](###Flask) contenant une docstring en YAML afin de générer les spécifications nécessaires à [Swagger](###Swagger).

### MySQL Connector/Python

[MySQL Connector/Python](https://dev.mysql.com/doc/connector-python/en/) est une librairie permettant à Python de communiquer avec les serveurs MySQL. Cette librairie est indispensable si l'on veut communiquer avec une base de données MySQL, et elle apporte des avantages tel que la conversion de données entre Python et MySQL. Par exemple, le `datetime` Python et `DATETIME` MySQL.

### SASS

<img style="float: right; margin-left: 25px; width: 30%" src="https://upload.wikimedia.org/wikipedia/commons/9/96/Sass_Logo_Color.svg">[SASS](https://sass-lang.com/) est un préprocesseur CSS. Cet outil permet d'étendre la syntaxe du langage CSS afin de pouvoir ajouter de nouvelles fonctionnalités. SASS permet aussi d'avoir un système de variable plus puissant que celui de CSS ainsi qu'un système d'import de fichier plus épuré à mon goût. En effet, il est possible de créer un fichier pour stocké toutes les couleurs sous forme de variables et ensuite importé ce fichier dans la feuille de style principale pour pouvoir utilisé les couleurs n'importe où.

### Swagger

<img style="float: right; margin-left: 25px; width: 30%" src="https://static1.smartbear.co/swagger/media/assets/images/swagger_logo.svg">[Swagger](https://swagger.io/tools/swagger-ui/) permet de visualiser les url d'une API automatiquement, basé sur les spécifications de chaque url. La générations du visuel est automatique et est optimisé pour une interaction avec le client. J'ai utilisé cet outil afin de visualiser correctement les routes utilisées par mon application afin de récupérer des données.

### jQuery UI

[jQuery](https://jqueryui.com/) UI est un ensemble d'interactions utilisateur, d'effets, de widget, et de thème construit sur la base de jQuery. J'ai utilisé cet outil afin de pouvoir gérer avec facilité la réorganisation des favoris d'un utilisateur. En effet, il est possible de glisser déposé les couvertures des animes présent dans les favoris de l'utilisateur afin de réorganisé l'ordre de ces derniers.

### ESLint

<img style="float: right; margin-left: 25px; width: 30%" src="https://i.imgur.com/CbRxgU2.png">[ESLint](https://eslint.org/) est un outil vérification syntaxique automatique de code. La vérification est basé sur un ensemble de règles définissant la syntaxe à utiliser. Cet outil m'a été utile pour vérifier que mon code était conforme aux normes [Airbnb](https://github.com/airbnb/javascript), pour éviter d'avoir des morceaux de code potentiellement problématiques ou mal optimiser ou même plus utilisé.

<img src="https://i.imgur.com/ac4CFJV.png">

<div style="width: 100%; text-align: center; color: gray">Cas d'utilisation de ESLint. La command <span style="color: #ff8000;">npm run lint static/js</span> m'indique qu'un point-virgule est manquant à la ligne 93 de mon fichier user-list-handler.js</div>

### Pylint

<img style="float: right; margin-left: 25px; width: 30%" src="https://i.imgur.com/BxrqM3f.png">[Pylint](https://www.pylint.org/) est aussi un outil de vérification syntaxique comme [ESLint](###eslint). Cependant, il n'utilise pas de standard créer par la communauté mais les standards officiels de Python, le [PEP8](https://www.python.org/dev/peps/pep-0008/).

<img src="https://i.imgur.com/kJ9BcdV.png">

<div style="width: 100%; text-align: center; color: gray">Cas d'utilisation de Pylint. La command <span style="color: #ff8000;">pylint --output-format=colorized packages/controllers/SqliteController.py</span> m'indique entre autre que des imports ne sont pas bien placés</div>

### Git

<img style="float: right; margin-left: 25px; width: 30%" src="https://upload.wikimedia.org/wikipedia/commons/e/e0/Git-logo.svg">[Git](https://git-scm.com/) est un outil de gestion de version. Cet outil à été utilisé durant toute la durée de mon TPI afin de garder un historiques des modifications apportées à mon projet ainsi qu'un système de sauvegarde externe sur [Github](https://github.com) en cas de problème technique sur mon ordinateur local.

<div style='page-break-after: always; break-after: page; text-align:right;'></div>

