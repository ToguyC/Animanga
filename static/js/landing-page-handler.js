/**
 * Script pour la prise e charge de la page d'accueil lorsque utilisateur connecté ou pas
 *
 * @author: Tanguy Cavagna
 * @copyright: Copyright 2020, TPI
 * @version: 1.0.0
 * @date: 2020-05-26
 */

const background = document.querySelector('.background');
const navbar = document.querySelector('.navbar');
const searchClear = document.querySelector('.search-clear');
const searchString = document.querySelector('.search-form .search-string');

if (background != null) {
    navbar.style.background = 'transparent';
}

if (searchClear != null) {
    searchClear.addEventListener('click', () => {
        searchString.value = '';
    });
}

if (searchString != null) {
    // Redirige sur la page de recherche lors de l'appuie sur la touche entrée
    // dans le champs de recherche
    searchString.onkeydown = (e) => {
        if (e.keyCode === 13) { // Touche entrée
            window.location.replace(`/search/${searchString.value}`);
        }
    };
}
