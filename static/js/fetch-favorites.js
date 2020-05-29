/**
 * Récupère les animes favoris de l'utilisateur
 * 
 * @param {boolean} col Est-ce l'affichage avec colonne de Bootstrap doit être utilisé
 * @param {string} searchedUser Pseudo de l'utilisateur cherché si sur la page d'un autre utilisateur que celui connecté
 */
/* eslint-disable-next-line no-unused-vars */
function fetchFavorites(col = false, searchedUser = null) {
    const favorites = document.querySelector('.favorites');

    if (favorites != null) {
        let url = '/get/favorites';

        // Ajout du slug `nickname` si l'on veut récupérer les favoris d'un
        // autre utilisateur que celui connecté
        if (searchedUser != null) {
            url += `/${searchedUser}`;
        }

        fetch(url, {
            method: 'GET',
            header: {
                Accept: 'application/json',
                'Content-Type': 'application/json',
            },
        }).then((response) => response.json()).then((json) => {
            favorites.innerHTML = '';

            // Affiche les favoris
            if (json.animes.length > 0) {
                json.animes.forEach((anime) => {
                    const favoriteItem = document.createElement('div');
                    const favoritePicture = document.createElement('img');
                    
                    favoriteItem.classList.add('favorite-item');
                    favoriteItem.dataset.id = anime.id;

                    if (col === true) {
                        favoriteItem.classList.add('col-xl-4');
                    }

                    favoritePicture.src = anime.picture;
                    favoriteItem.appendChild(favoritePicture);
                    favorites.appendChild(favoriteItem);
                });
            } else {
                const noFavorite = document.createElement('div');
                const h4 = document.createElement('h4');
                const span = document.createElement('span');

                noFavorite.classList.add('no-favorites');
                h4.innerHTML = 'Aucun favoris pour le moment';
                span.innerHTML = '（＞人＜；）';

                noFavorite.appendChild(h4);
                noFavorite.appendChild(span);
                favorites.append(noFavorite);
            }
        });
    }
}