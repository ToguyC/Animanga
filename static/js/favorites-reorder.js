/**
 * Script pour la prise en charge du changement d'ordre des favoris
 *
 * @author: Tanguy Cavagna
 * @copyright: Copyright 2020, TPI
 * @version: 1.0.0
 * @date: 2020-06-02
 */

const reorder = document.querySelector('.reorder');
let toggleReorder = false;

reorder.addEventListener('click', () => {
    $('.favorites').sortable({ disabled: toggleReorder });
    reorder.innerHTML = toggleReorder === false ? 'Sauvegarder' : 'Réordonner les favoris';

    // Si bouton cliqué pour sauvegarder
    if (toggleReorder === true) {
        const favorites = document.querySelectorAll('.favorites .favorite-item');

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
    }

    toggleReorder = !toggleReorder;
});