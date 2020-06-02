"""Contient la classe de contrôle des activités

@author: Tanguy Cavagna
@copyright: Copyright 2020, TPI
@version: 1.1.0
@date: 2020-06-02
"""
from datetime import timedelta
from datetime import datetime as dt
from sqlite3 import Error as SqliteError

from .SqliteController import SqliteController

class ActivitiesController:
    """Controlleur d'une activité
    """

    def __init__(self):
        pass

    @classmethod
    def get_last_24h(cls, user_id: int) -> []:
        """Récupère les activitées d'un utilisateur
            Arguments:
                user_if {int} -- Id de l'utilisateur
            Returns:
                [] -- Liste des activitées
        """
        activities = cls.__get_list_related(user_id) + cls.__get_favorite_related(user_id)
        # Trie toutes les activitées par date
        activities.sort(key=lambda item: item['date'], reverse=True)

        # Change le format de toutes les dates des activitées
        for a in activities:
            a['date'] = a['date'].strftime('%Y-%m-%d %H:%M:%S')

        return activities

    @classmethod
    def __get_list_related(cls, user_id: int) -> []:
        """Récupère les activitées relatives aux listes
            Arguments:
                user_id {int} -- Id de l'utilisateur
            Returns:
                [] -- Liste des activités
        """
        try:
            current_datetime = dt.now()

            sql_list_additions = """SELECT anime.title, anime.picture, list_has_anime.modificationDate, list.nameList
                                    FROM list_has_anime
                                    JOIN list ON list.idList = list_has_anime.idList
                                    JOIN user_has_list ON user_has_list.idList = list.idList
                                    JOIN anime ON anime.idAnime = list_has_anime.idAnime
                                    WHERE user_has_list.idUser = ?"""

            user_list_additions = SqliteController().execute(sql_list_additions, values=(user_id,), fetch_mode=SqliteController.FETCH_ALL)
            # Récupération des activité des dernières 24h
            user_list_additions = [add for add in user_list_additions if add['modificationDate'] > current_datetime - timedelta(days=1)]

            results = []
            for add in user_list_additions:
                results.append({
                    'title': add['title'],
                    'list': add['nameList'],
                    'picture': add['picture'],
                    'date': add['modificationDate']
                })

            return results
        except SqliteError as e:
            print(str(e))
            return []

    @classmethod
    def __get_favorite_related(cls, user_id: int) -> []:
        """Récupère les activitées relatives aux favoris
            Arguments:
                user_id {int} -- Id de l'utilisateur
            Returns:
                [] -- Liste des activités
        """
        try:
            current_datetime = dt.now()

            sql_favorite_additions = """SELECT anime.title, anime.picture, user_has_favorite.modificationDate
                                    FROM user_has_favorite
                                    JOIN anime ON anime.idAnime = user_has_favorite.idAnime
                                    WHERE user_has_favorite.idUser = ?"""

            user_favorite_additions = SqliteController().execute(sql_favorite_additions, values=(user_id,), fetch_mode=SqliteController.FETCH_ALL)
            # Récupération des activité des dernières 24h
            user_favorite_additions = [add for add in user_favorite_additions if add['modificationDate'] > current_datetime - timedelta(days=1)]

            results = []
            for add in user_favorite_additions:
                results.append({
                    'title': add['title'],
                    'list': 'favoris',
                    'picture': add['picture'],
                    'date': add['modificationDate']
                })

            return results
        except SqliteError as e:
            print(str(e))
            return []