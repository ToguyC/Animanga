<table style="border: none">
    <tr style="background: white; border: none">
        <td style="border: none; font-size: .7rem; color: gray">RÉSUMÉ DU RAPPORT TPI</td>
        <td style="border: none; font-weight: bold; font-size: .7rem;">Tanguy Cavagna - mai - juin 2020</td>
    </tr>
    <tr style="background: white; border: none">
        <td style="border: none; color: #006EDB; font-size: 1.5rem; font-weight: bold" rowspan="2">Animanga</td>
        <td style="border: none; font-size: .7rem">École de métiers : <span style="float: right">CFPT Informatique, Petit-Lancy GE</span></td>
    </tr>
    <tr style="background: white; border: none; font-size: .7rem">
        <td style="border: none">Entreprise formatrice : <span style="float: right">Formation plein temps</span></td>
    </tr>
</table>


### Situation de départ

Ce *Travail Pratique Individuel* (TPI), de 88 heures disposées sur 11 jours, a été réalisé dans le cadre de l'examen de validation d'acquis pour la formation CFC-Informatique Développement d'Application. L'énoncé qui m'a été attribué me donne le projet suivant : une application web permettant de faire des listes personnelles d'animes, ainsi que de mettre ces animes en favoris. Les utilisateurs doivent avoir un compte pour accéder à l'application et ainsi utiliser le site. Les données doivent provenir d'un fichier `json` donné et doivent être importées dans une base de données Sqlite3. D'autres fonctionnalités sont indispensables pour pouvoir rechercher les animes et affiché les activités de l'utilisateur.

### Mise en œuvre

L'application a été réalisée avec Python et le micro-framework Flask pour la partie back-end, JavaScript pour le front-end, ainsi que Sqlite3 et MySQL pour la base de données. L'application fonctionne grâce à des routes mises en place dans Flask et les pages chargent les données en utilisant `fetch` de JavaScript ainsi que des variables Python interprétées lors du chargement de la page. Les tâches de l'énoncé ont été divisées en *user stories* et la *méthodologie en 6 étapes* a été utilisé pour structuré la progression du projet. Un protocole de test complet a été créé pour rendre l'application conforme à l'énoncé. Un journal de bord quotidien a été tenu à jour et comporte toutes les étapes entreprises tout au long du travail, les problèmes rencontrés, solutions apportées et rendez-vous télévisuel fait.

### Résultats

Toutes les fonctionnalités de l'énoncé ont été implémentées et les utilisateurs ont une expérience agréable lors de l'utilisation de l'application. Le code JavaScript est conforme aux normes Airbnb, vérifier grâce à l'analyseur syntaxique (*linter*) ESLint, tout comme le Python est conforme aux normes PEP8 grâce à l'analyseur syntaxique Pylint. Une documentation complète a également été rédigée.