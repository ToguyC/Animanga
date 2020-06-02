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
let listCancelRenames = document.querySelectorAll('#lists .lists-container ul li .cancel__rename');
let listRenameInput = document.querySelectorAll('#lists .lists-container ul li input');
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
            'search-terms': searchTerms,
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
                listSectionTitle.innerHTML = list;
                
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
    });
}

/**
 * Récupère les animes de la list cliquée
 */
function listNamesClickEventSetup() {
    listNames.forEach((listName) => {
        const currentListName = listName;
        
        // Event clique pour le nom des listes afin d'afficher les animes de cette dite liste
        currentListName.addEventListener('click', () => {
            const list = currentListName.parentElement;

            if (!list.classList.contains('new-list')) {
                // Parcour toutes les listes existantes dans la page et supprime la classe 
                // `selected` pour l'ajouté sur la liste courante
                lists.forEach((l) => l.classList.remove('selected'));
                list.classList.add('selected');

                fetchListAnimes(listSearchString.value, list.dataset.list);
            }
        });

        if (![
                'Complétés',
                'En cours',
                'Planifiés',
                'Abandonés'
            ].includes(currentListName.innerHTML)) {
            // Event double clique pour renommer la liste seulement si elle ne fait 
            // pas parti de celles par défaut
            currentListName.addEventListener('dblclick', () => {
                const newNameInput = currentListName.parentNode.querySelector('input');
                const cancelButton = currentListName.parentNode.querySelector('.cancel__rename');
                const removeButton = currentListName.parentNode.querySelector('.remove__list');

                newNameInput.classList.remove('d-none');
                newNameInput.value = currentListName.innerHTML;
                cancelButton.classList.remove('d-none');
                currentListName.classList.add('d-none');
                removeButton.classList.add('d-none');
            });
        }
    });
}

/**
 * Supprime une liste
 *
 * @param {int} idList Id de la liste à supprimer
 */
function deleteList(idList) {
    fetch('/delete/list', {
        method: 'DELETE',
        headers: {
            Accept: 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            idList,
        }),
    }).then((response) => response.json()).then(() => {
        window.location.reload();
    });
}

/**
 * Supprime la liste cliqueé
 */
function removeListClickEventSetup() {
    // Event clique pour la suppression d'une liste
    listRemovables.forEach((removeTrigger) => {
        removeTrigger.addEventListener('click', () => {
            const list = removeTrigger.parentNode;
            deleteList(list.dataset.list);
        });
    });
}

/**
 * Ajoute une nouvelle liste personnelle à l'utilisateur
 *
 * @param {string} newListName Nom de la nouvelle liste
 */
function addNewList(newListName) {
    fetch('/add/list', {
        method: 'PUT',
        headers: {
            Accept: 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            newListName,
        }),
    }).then((response) => response.json()).then((json) => {
        newListString.value = '';
        const createdList = json.list;

        const li = document.createElement('li');
        const listName = document.createElement('span');
        const udpateNameInput = document.createElement('input');
        const removeButton = document.createElement('span');

        li.dataset.list = createdList.id;
        listName.classList.add('list__name');
        listName.innerHTML = createdList.name;
        udpateNameInput.type = 'text';
        udpateNameInput.name = 'new_list_name';
        udpateNameInput.style.width = "80%";
        udpateNameInput.classList.add('d-none');
        udpateNameInput.id = `${createdList.id}_new_list_name`;
        removeButton.classList.add('remove__list');
        removeButton.innerHTML = '🗑';

        li.appendChild(listName);
        li.appendChild(udpateNameInput);
        li.appendChild(removeButton);

        // Ajoute la nouvelle liste juste avant le champ text permettant d'ajouter 
        // une nouvelle liste
        document.querySelector('#lists .lists-container ul').insertBefore(li, lists[lists.length - 1]);

        // Mise à jour des éléments DOM pour les listes
        lists = document.querySelectorAll('#lists .lists-container ul li');
        listNames = document.querySelectorAll('#lists .lists-container ul li .list__name');
        listRemovables = document.querySelectorAll('#lists .lists-container ul li .remove__list');
        listCancelRenames = document.querySelectorAll('#lists .lists-container ul li .cancel__rename');
        listRenameInput = document.querySelectorAll('#lists .lists-container ul li input');

        // Ajout des events pour la liste venant d'être créer
        listNamesClickEventSetup();
        removeListClickEventSetup();
        cancelListRenameClickEvent();
    });
}

/**
 * Annulle le renommage de la lsite
 */
function cancelListRenameClickEvent() {
    // Event clique pour l'annullation du renommage d'une liste
    listCancelRenames.forEach((cancelTrigger) => {
        cancelTrigger.addEventListener('click', () => {
            const list = cancelTrigger.parentNode;
            const newNameInput = list.querySelector('input');
            const cancelButton = list.querySelector('.cancel__rename');
            const removeButton = list.querySelector('.remove__list');
            const listName = list.querySelector('.list__name');

            newNameInput.classList.add('d-none');
            newNameInput.value = '';
            cancelButton.classList.add('d-none');
            listName.classList.remove('d-none');
            removeButton.classList.remove('d-none');
        });
    });
}

/**
 * Renomme la liste
 * 
 * @param {int} listId Id de la liste à modifier
 * @param {string} newListName Nouveau nom de la liste
 */
function renameList(idList, newListName) {
    fetch('/set/list/name', {
        method: 'PATCH',
        headers: {
            Accept: 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            idList,
            newListName,
        }),
    }).then((response) => response.json()).then((json) => {
        window.location.reload();
    });
}

// Affiche les animes des listes de l'utilisateur dont le titre concorde avec
// la chaine recherchée lorsque la touche entrés est pressée
listSearchString.onkeydown = (e) => {
    if (e.keyCode === 13) { // Touche entrée
        fetchListAnimes(listSearchString.value, null);
    }
};

// Créer une nouvelle liste pour l'utilisateur connecté lorsque la touche entrée et pressée
if (newListString !== undefined) {
    newListString.onkeydown = (e) => {
        if (e.keyCode == 13) {
            addNewList(newListString.value);
        }
    }
}

// Renomme une liste
if (listRenameInput !== undefined) {
    listRenameInput.forEach((renameInput) => {
        renameInput.onkeydown = (e) => {
            if (e.keyCode == 13) {
                renameList(renameInput.parentNode.dataset.list, renameInput.value);
            }
        }
    });
}

window.addEventListener('load', () => {
    fetchListAnimes(null, null);
    listNamesClickEventSetup();
    removeListClickEventSetup();
    cancelListRenameClickEvent();
});
