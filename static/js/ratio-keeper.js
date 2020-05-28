/**
 * Script permettant le redimensionnement des image en fonction de la taille de l'écran
 *
 * @author: Tanguy Cavagna
 * @copyright: Copyright 2020, TPI
 * @version: 1.0.0
 * @date: 2020-05-28
 */

const resultsItemPictures = document.querySelectorAll('.search-results .result-item .left .picture');
const resultsItem = document.querySelectorAll('.search-results .result-item');

/**
 * Redéfini la taille des images pour garder un ratio correct
 */
function resizeThumbnails() {
    let newHeight = -1;
    // Re defini la hauteur de l'image en fonction de sa largeur
    resultsItemPictures.forEach((item) => {
        const currentItem = item;
        newHeight = parseInt(currentItem.getBoundingClientRect().width / 0.7333, 10);
        currentItem.style.height = `${newHeight}px`;
    });
    // Defini la hauteur max de la carte en foncion de la hauteur de l'image principale
    resultsItem.forEach((item) => {
        const currentItem = item;
        currentItem.style.maxHeight = `${currentItem.querySelector('.left .picture').getBoundingClientRect().height}px`;
    });
}

window.addEventListener('load', resizeThumbnails);
window.addEventListener('resize', resizeThumbnails);
