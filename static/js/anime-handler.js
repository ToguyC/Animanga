/* global fetchFavorites */

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
const statusCombo = document.querySelectorAll('.status_combo');
const customChecks = document.querySelectorAll('.custom-check');

/**
 * Supprime un anim des listes par défaut
 *
 * @param {int} idAnime Id de l'anime à supprimer des listes par défaut
 * @param {function} callback Function à éxecuter en tant que callback du fetch
 */
function deleteAnimeFromDefaultLists(idAnime, callback = () => {}) {
    return fetch('/delete/defaults', {
        method: 'DELETE',
        headers: {
            Accept: 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ idAnime }),
    }).then((response) => response.json()).then(() => {
        callback();
    });
}

/**
 * Ajout un anime dans une liste
 *
 * @param {int} idAnime Id de l'anime
 * @param {int} idList Id de la liste
 * @param {function} callback Fonction à éxecuter en tant que callback du fetch
 */
function putAnimeInList(idAnime, idList, callback = (json) => {}) {
    fetch('/set/list', {
        method: 'PUT',
        headers: {
            Accept: 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ idAnime, idList }),
    }).then((response) => response.json()).then((json) => {
        callback(json);
    });
}

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

// Changement du statut de visionnement de l'anime. (Complété, En cous, Abondoné, Planifié)
statusCombo.forEach((comboOption) => {
    comboOption.addEventListener('change', async () => {
        const idAnime = comboOption.value.split('-')[0];
        const idList = comboOption.value.split('-')[1];


        if (idList !== 'none') {
            await deleteAnimeFromDefaultLists(idAnime);
            putAnimeInList(idAnime, idList);
        } else {
            deleteAnimeFromDefaultLists(idAnime);
        }
    });
});

// Ajout d'un anime dans une liste
customChecks.forEach((customCheck) => {
    customCheck.addEventListener('click', (e) => {
        const check = e.target;
        const input = check.querySelector('input[type="checkbox"]');
        input.checked = !input.checked;

        const idAnime = input.value.split('-')[0];
        const idList = input.value.split('-')[1];

        putAnimeInList(idAnime, idList, (json) => {
            if (json.Status === true) {
                check.classList.add('checked');
            } else {
                check.classList.remove('checked');
            }
        });
    });
})
