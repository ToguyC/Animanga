/**
 * Script pour la prise en charge des activitée de l'utilisateur
 *
 * @author: Tanguy Cavagna
 * @copyright: Copyright 2020, TPI
 * @version: 1.0.0
 * @date: 2020-06-02
 */

/**
 * Retourne le nombre d'heure, minutes et secondes entre une date et aujourd'hui
 *
 * @param {timestamp} olderTime Timestamp antérieur à aujourd'hui
 */
/* eslint-disable-next-line no-unused-vars */
function timeEllapsedFromNow(olderTime) {
    let timeEllapsed = 0;

    // Récupération des différentes mesures de temps
    const delta = Math.abs((Date.now() - olderTime) / 1000);
    const seconds = Math.floor(delta % 60);
    const hours = Math.floor(delta / 3600) % 24;
    const minutes = Math.floor(delta / 60) % 60;

    // Assignation de la mesure de temps la plus appropriée
    if (hours > 0) {
        timeEllapsed = `${hours} heures`;
    } else if (minutes > 0) {
        timeEllapsed = `${minutes} minutes`;
    } else {
        timeEllapsed = `${seconds} secondes`;
    }

    return `Il y a ${timeEllapsed}`;
}

/**
 * Récupère les activité de l'utilisateur
 */
/* eslint-disable-next-line no-unused-vars */
function fetchActivities() {
    const activities = document.querySelector('.activities');

    if (activities != null) {
        const url = '/get/activities';

        fetch(url, {
            method: 'GET',
            headers: {
                Accept: 'application/json',
                'Content-Type': 'application/json',
            },
        }).then((response) => response.json()).then((json) => {
            activities.innerHTML = '';

            // Affiche les activités
            if (json.activities.length > 0) {
                json.activities.forEach((activity) => {
                    const activityContainer = document.createElement('div');
                    const wrapper = document.createElement('div');
                    const activitySubject = document.createElement('div');
                    const subjectTitle = document.createElement('span');
                    const activityTimestamp = document.createElement('span');
                    const activityImg = document.createElement('img');

                    activityContainer.classList = 'activity col-xl-6 col-md-12';
                    subjectTitle.innerHTML = activity.title;
                    activitySubject.classList.add('activity__subject');
                    activitySubject.appendChild(subjectTitle);
                    activitySubject.innerHTML += `<br> À été ajouté à : ${activity.list}`;
                    activityTimestamp.classList.add('activity__timestamp');
                    activityTimestamp.innerHTML = timeEllapsedFromNow(new Date(activity.date));
                    activityImg.src = activity.picture;

                    wrapper.appendChild(activitySubject);
                    wrapper.appendChild(activityTimestamp);
                    wrapper.appendChild(activityImg);
                    activityContainer.appendChild(wrapper);
                    activities.appendChild(activityContainer);
                });
            } else {
                const noFavorites = document.createElement('div');
                const h4 = document.createElement('h4');
                const span = document.createElement('span');

                noFavorites.className = 'no-activities';
                h4.innerHTML = 'Aucune activité pour le moment';
                span.innerHTML = '（＞人＜；）';

                noFavorites.appendChild(h4);
                noFavorites.appendChild(span);

                activities.appendChild(noFavorites);
            }
        });
    }
}
