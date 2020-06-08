## Conclusion

### Difficultés majeures rencontrées

Durant tout le développement de mon projet, aucun problème bloquant n'a été rencontré. Voici cependant la liste des soucis les plus majeurs :

* > L'outil de fusion de PDF que j'utilisait - [pdfunite](http://manpages.ubuntu.com/manpages/bionic/man1/pdfunite.1.html) - ne prenait pas en charge les titres lors de la fusion de plusieurs PDF. En effet, si un PDF seul comportait des titres, après la fusion ces derniers étaient considéré comme simple texte.

  ➡ J'ai pu corriger ce soucis en changeant de librairie de fusion de document PDF. La recherche de nouvelle librairie n'était pas compliqué du tout car il existe un nombre élevé de librairies permettant de fusionner des PDF, dont [pdftk](https://www.pdflabs.com/tools/pdftk-the-pdf-toolkit/) et le didacticiel disponible à [cette adresse](https://www.ostechnix.com/how-to-merge-pdf-files-in-command-line-on-linux/).

* > Lors de la synchronisation, j'utilise des timestamps pour savoir quels enregistrements ont été modifié. Cependant, j'utilisais un format différent entre ma base Sqlite3 et MySQL. Dans Sqlite3, le format utilisé était `%Y-%m-%d %H:%M:%f` ce qui donne `2020-06-08 09:08:32.276`. Les millisecondes sont présentes avec ce format. Or, le format utilisé par défaut dans MySQL est `%Y-%m-%d %H:%M:%S` ce qui donne `2020-06-08 09:08:32`. Cette différence de format faisait que lorsqu'un timestamp Sqlite3 dont les millisecondes sont plus grandes que `.500`, ce timestamp est arrondi vers le haut et donc mes timestamps sont différents.

  ➡ Le soucis n'était de loin pas compliqué à régler mais j'ai mis un certain moment afin de trouvé ce qui causait le soucis d'enregistrement différent entre Sqlite3 et MySQL. Une fois la cause trouvé, j'ai simplement fait en sorte que la date que j'insérais dans Sqlite3 ne comportait pas les millisecondes et tout est rentré dans l'ordre.

### Améliorations possibles

Étant donné la courte période mise à disposition, il est claire que des améliorations sont possibles sur les fonctionnalités existantes. Voici un aperçut de ce qui pourrait être améliorer :

* Ajouter la fonctionnalité de pouvoir modifier son profile. Cela comporte le pseudo, email et le mot de passe

* Faire en sorte que l'interface du site soit *responsive design* (qu'il s'adapte sur tout type d'écran). Pour le moment, cette fonctionnalité n'est implémentée qu'à moitié

* Mettre plus de résultat lors d'une recherche. Pour le moment ce n'est que les neufs les plus adéquats par rapport à la chaine recherché

* Modifier la fonctionnalité de synchronisation unidirectionnel entre Sqlite3 et MySQL. Pour le moment, l'algorithme utilisé est relativement efficace mais il pourrait être amélioré de cette façon par exemple :

  Stocké le timestamp de la dernière synchronisation dans une table, supprimer tout les enregistrements plus présents dans Sqlite3 de MySQL, sélectionner que les enregistrements dont la date est supérieur ou égale à la dernière synchronisation et mettre à jours les enregistrements MySQL et ajouté ceux qui manque.

  Cette façon de faire permettrait à algorithme d'être beaucoup plus rapide qu'actuellement.

Outre les fonctionnalités existantes, j'ai penser à ces quelques idées durant le développement de l'application :

* Ajouter la fonctionnalité de pouvoir se faire une liste d'amis en cherchant le pseudo de l'utilisateur dans un champs prévu à cet effet et ensuite avoir une page dédié à l'affichage de cette dite liste d'amis afin de pouvoir aller voir le profil de ces derniers.
* Ajouter un système de rôle permettant aux administrateur de pouvoir gérer les animes sans que les utilisateur puisse le faire pour éviter toute fausse manipulation
* Ajouter la fonctionnalité permettant aux utilisateur de mettre une note à un anime et une progression de visionnage (nombre d'épisode regardé)
* Modifier le contenu des activités pour ajouter celles des amis

### Bilan personnel

Ce projet m'a énormément plus. Le sujet était parfait pour moi : j'adore réaliser des projet en Python, surtout web, et je suis passionné par les animes. Le fait de pouvoir lier ces deux passions était très agréable. Je trouve très plaisant d'utilisé cette application de part sa simplicité et son contenu fourni. Le fait d'écrire une documentation aussi grosse était une première pour moi et ce fût très enrichissant, en plus de me satisfaire grandement.

### Remerciements

J'apporte mes remerciements à :

* M. Pascal Bonvin pour son suivi assidu lors de ce TPI
* M. Nicolas Ettlin pour ses conseils avisé concernant l'utilisation d'eslint et quelque techniques CSS.