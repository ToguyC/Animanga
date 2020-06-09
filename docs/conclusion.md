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