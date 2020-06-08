/**
 * Script pour la prise en charge du changement d'ordre des favoris
 *
 * @author: Tanguy Cavagna
 * @copyright: Copyright 2020, TPI
 * @version: 1.0.0
 * @date: 2020-06-02
 */

const reorder = document.querySelector('.reorder');
let removers = document.querySelectorAll('.favorite-remover');
let toggleReorder = false;

/**
 * Affiche ou cache les boutton de suppression des favoris
 */
function toggleHideFavoriteRemovers(hide = true) {
    removers.forEach((remover) => {
        if (hide === true) {
            remover.classList.add('d-none');
        } else {
            remover.classList.remove('d-none');
        }
    });
}

reorder.addEventListener('click', () => {
    $('.favorites').sortable({ disabled: toggleReorder });
    reorder.innerHTML = toggleReorder === false ? 'Sauvegarder' : 'Réordonner les favoris';

    // Si bouton cliqué pour sauvegarder
    if (toggleReorder === true) {
        const favorites = document.querySelectorAll('.favorites .favorite-item');
        toggleHideFavoriteRemovers(true);

        const ids = [];
        favorites.forEach((favorite) => {
            ids.push(favorite.dataset.id);
        });

        fetch('/set/favorites-order', {
            method: 'PATCH',
            headers: {
                Accept: 'application/json',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ ids }),
        }).then((response) => response.json()).then(() => {
            // Ne rien faire
        }).catch(() => {
            // Ne rien faire
        });
    } else { // Clique sur `Réordonner les favoris` pour afficher les boutons de suppression
        removers = document.querySelectorAll('.favorite-remover');
        toggleHideFavoriteRemovers(false);
    }

    toggleReorder = !toggleReorder;
});
