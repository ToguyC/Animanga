/* global: fetchFavorites */

/**
 * Script pour la prise en charge du chargement des favoris, ajout de favoris,
 * ajout d'anime dans les listes
 *
 * @author: Tanguy Cavagna
 * @copyright: Copyright 2020, TPI
 * @version: 1.0.0
 * @date: 2020-05-29
 */

const favoriteTogglers = document.querySelectorAll('.favorite-toggler');

// Changement du status de favoris de l'anime
favoriteTogglers.forEach((favoriteToggler) => {
    favoriteToggler.addEventListener('click', (e) => {
        const toggler = e.target.closest('.favorite-toggler');

        fetch('/set/favorite', {
            method: 'PATCH',
            headers: {
                Accept: 'application/json',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ idAnime: toggler.dataset.id }),
        }).then((response) => response.json()).then((json) => {
            // Check le toggle favoris selon l'état de l'anime
            if (json.Status === true) {
                toggler.classList.add('is-favorite');
            } else {
                toggler.classList.remove('is-favorite');
            }

            fetchFavorites();
        });
    });
});