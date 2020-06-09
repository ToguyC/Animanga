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