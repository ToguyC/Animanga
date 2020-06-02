/**
 * Script pour la prise en charge des listes de l'utilisateur
 *
 * @author: Tanguy Cavagna
 * @copyright: Copyright 2020, TPI
 * @version: 1.0.0
 * @date: 2020-06-02
 */

let lists = document.querySelectorAll('#lists .lists-container ul li');
let listNames = document.querySelectorAll('#lists .lists-container ul li .list__name');
let listRemovables = document.querySelectorAll('#lists .lists-container ul li .remove__list');
const listSearchString = document.querySelector('#search-list .search-string');
const newListString = document.querySelector('#new-list__name');

/**
 * Récupère tout les animes d'une liste et les affiche
 * 
 * @param {string} searchTerms Chaine de recherche
 * @param {int} idList Id de la liste à fetch
 */
function fetchListAnimes(searchTerms, idList) {
    fetch('/get/animes', {
        method: 'POST',
        headers: {
            Accept: 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            nicknameUser: document.getElementById('searched_user').dataset.nickname,
            idList,
            'search-terms': searchTerms
        }),
    }).then((response) => response.json()).then((json) => {
        const animes = json.animes;
        const animesContainer = document.querySelector('#animes-container');

        if (Object.keys(animes).length > 0) {
            const animeLists = Object.keys(animes);

            animesContainer.innerHTML = '';

            animeLists.forEach((list) => {
                const listSection = document.createElement('div');
                const listSectionTitle = document.createElement('h2');

                listSection.classList = 'mb-5 list-section';
                listSectionTitle.innerHTML = list.split('-')[1];

                animes[list].forEach((anime) => {
                    const animeItem = document.createElement('div');
                    const animeItemTitle = document.createElement('h4');
                    const animeItemPicture = document.createElement('img');

                    animeItem.classList.add('anime-item');
                    animeItemTitle.innerHTML = anime.title;
                    animeItemPicture.src = anime.picture;

                    animeItem.appendChild(animeItemTitle);
                    animeItem.appendChild(animeItemPicture);

                    listSection.appendChild(animeItem);
                });

                animesContainer.appendChild(listSectionTitle);
                animesContainer.appendChild(listSection);
            });
        } else {
            animesContainer.innerHTML = '';

            const infos = document.createElement('div');
            infos.classList.add('lists-empty');

            const title = document.createElement('h4');
            const separator = document.createElement('span');
            const sub = document.createElement('span');
            const img = document.createElement('img');
            title.innerHTML = 'Aucun anime';
            separator.classList.add('separator');
            sub.innerHTML = 'Remplis tes listes pour la rendre heureuse !';
            img.src = '/static/img/whale.svg';

            infos.appendChild(title);
            infos.appendChild(separator);
            infos.appendChild(sub);
            infos.appendChild(img);

            animesContainer.appendChild(infos);
        }
    })
}

/**
 * Récupère les animes de la list cliquée
 */
function listNameClickEventSetup() {
    // Event clique pour le nom des listes afin d'afficher les animes de cette dite liste
    listNames.forEach((listName) => {
        const currentListName = listName;

        currentListName.addEventListener('click', () => {
            const list = currentListName.parentElement;

            if (!list.classList.contains('new-list')) {
                // Parcour toutes les listes existantes dans la page et supprime la classe `selected` 
                // pour l'ajouté sur la liste courante
                lists.forEach((l) => l.classList.remove('selected'));
                list.classList.add('selected')

                fetchListAnimes(listSearchString.value, list.dataset.list);
            }
        });
    });
}

window.addEventListener('load', () => {
    fetchListAnimes(null, null);
    listNameClickEventSetup();
});