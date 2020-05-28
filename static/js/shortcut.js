/**
 * Script pour la prise en charge des raccourcis clavier
 *
 * @author: Tanguy Cavagna
 * @copyright: Copyright 2020, TPI
 * @version: 1.0.0
 * @date: 2020-05-28
 */

/**
 * Prise en charge des évènements keydown
 *
 * @param {event} e Évènement keyup
 */
function keydownHandler(e) {
    // Prise en charge du CTRL+S
    if (e.ctrlKey && e.keyCode === 83) {
        e.preventDefault(); // Annule l'event de sauvegarde natif

        const searchModalTrigger = document.getElementById('search-modal-trigger');

        if (searchModalTrigger !== undefined) {
            searchModalTrigger.click();
        }
    }
}

document.addEventListener('keydown', keydownHandler, false);
