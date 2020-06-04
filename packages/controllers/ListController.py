"""Contient la classe de contrôle des utilisateurs

@author: Tanguy Cavagna
@copyright: Copyright 2020, TPI
@version: 1.0.0
@date: 2020-05-28
"""
from datetime import datetime as dt

from .SqliteController import SqliteError, SqliteController
from .logger import log
from ..models.List import List

class ListController:
    """Controlleur d'une list
    """

    @classmethod
    def __encapsulate_lists(cls, raw_results: dict) -> [List]:
        """Encapsule les résultats d'une requete

            Arguments:
                raw_resutls {dict} -- Résultats provenant de `SqliteController.execute`

            Returns:
                [Anime] -- Liste de listes encapsuler
        """
        return [
            List(result['idList'],
                 result['nameList']
            ) for result in raw_results
        ]

    @classmethod
    def __serialize_encapsulated_lists(cls, encapsulated_lists: list) -> [dict]:
        """Sérialize toutes les listes contenu dans une liste de liste encapsulé

            Arguments:
                encapsulated_lists {list} -- Liste des animes encapsulé

            Returns:
                [dict] -- Liste de tout les animes sérialisé
        """
        return [_list.serialize() for _list in encapsulated_lists]

    @classmethod
    def get_defaults_for_user(cls, user_id: int) -> [List]:
        """Retourne les listes par défaut d'un utilisateur

            Arguments:
                user_id {int} -- Id de l'utilisateur en question

            Returns:
                [List] -- Liste des listes par défaut de l'utilisateur
        """
        try:
            sql_user_list = """SELECT list.idList, nameList
                               FROM list
                               JOIN user_has_list ON list.idList = user_has_list.idList
                               WHERE user_has_list.idUser = ?
                               AND nameList IN ('Complétés', 'En cours', 'Abandonés', 'Planifiés')"""

            results = SqliteController().execute(sql_user_list, values=(user_id,), fetch_mode=SqliteController.FETCH_ALL)

            encapsulated = cls.__encapsulate_lists(results)

            return cls.__serialize_encapsulated_lists(encapsulated)
        except SqliteError as e:
            log(e)
            return []

    @classmethod
    def get_list_of_an_anime(cls, anime_id: int) -> [List]:
        """Récupère toutes les listes d'un anime

            Arguments:
                anime_id {int} -- Id de l'anime

            Returns:
                [List] -- Liste de toutes les listes de l'anime
        """
        try:
            sqli_lists = """SELECT list.idList, nameList
                            FROM list
                            JOIN list_has_anime ON list.idList = list_has_anime.idList
                            WHERE list_has_anime.idAnime = ?"""

            results = SqliteController().execute(sqli_lists, values=(anime_id,), fetch_mode=SqliteController.FETCH_ALL)

            encapsulated = cls.__encapsulate_lists(results)

            return cls.__serialize_encapsulated_lists(encapsulated)
        except SqliteError as e:
            log(e)
            return []

    @classmethod
    def get_user_lists(cls, user_id: int) -> [List]:
        """Récupère toutes les listes d'un utilisateur

            Arguments:
                user_id {int} -- Id de l'utilisateur

            Returns:
                [List] -- Toutes les listes de l'utilisateur
        """
        try:
            sql_user_lists = """SELECT list.idList, nameList
                                FROM list
                                JOIN user_has_list ON list.idList = user_has_list.idList
                                WHERE user_has_list.idUser = ?"""

            results = SqliteController().execute(sql_user_lists, values=(user_id,), fetch_mode=SqliteController.FETCH_ALL)

            encapsulated = cls.__encapsulate_lists(results)

            return cls.__serialize_encapsulated_lists(encapsulated)
        except SqliteError as e:
            log(e)
            return []

    @classmethod
    def get_by_id(cls, list_id: int) -> List:
        """Récupère une liste via son id

            Arguments:
                list_id {int} -- Id de la liste

            Return:
                List -- Liste trouvée
        """
        try:
            sql_select = "SELECT idList, nameList FROM list WHERE idList = ?"

            row = SqliteController().execute(sql_select, values=(list_id,), fetch_mode=SqliteController.FETCH_ONE)

            return List(row['idList'], row['nameList'])
        except SqliteError as e:
            log(e)
            return None

    @classmethod
    def add_new_list(cls, new_name: str, user_id: int) -> List:
        """Ajoute une nouvelle liste pour l'utiliateur connecté

            Arguments:
                new_name {str} -- Nom de la nouvelle liste
                user_id {int} -- Id de l'utilisateur connecté

            Returns:
                List -- Nouvelle liste créée
        """
        try:
            sql_insert = "INSERT INTO list(nameList, modificationDate) VALUES(?, ?)"
            sql_link_to_user = "INSERT INTO user_has_list(idUser, idList, modificationDate) VALUES(?, ?, ?)"

            current_date = dt.now().strftime('%Y-%m-%d %H:%M:%S')

            list_id = SqliteController().execute(sql_insert, values=(new_name, current_date,), fetch_mode=SqliteController.NO_FETCH)
            SqliteController().execute(sql_link_to_user, values=(user_id, list_id, current_date,), fetch_mode=SqliteController.NO_FETCH)

            return cls.get_by_id(list_id).serialize()
        except SqliteError as e:
            log(e)
            return None

    @classmethod
    def delete_by_id(cls, list_id: int, user_id: int) -> bool:
        """Supprime une liste via son id

            Arguments:
                list_id {int} -- Id de la list à supprimer
                user_id {int} -- Id de l'utilisateur connecté
        
            Returns:
                bool -- États de la requete
        """
        try:
            sql_unlink_anime = "DELETE FROM list_has_anime WHERE idList = ?"
            sql_unlink_to_user = "DELETE FROM user_has_list WHERE idUser = ? AND idList = ?"
            sql_delete = "DELETE FROM list WHERE idList = ?"

            SqliteController().execute(sql_unlink_anime, values=(list_id,), fetch_mode=SqliteController.NO_FETCH)
            SqliteController().execute(sql_unlink_to_user, values=(user_id, list_id,), fetch_mode=SqliteController.NO_FETCH)
            SqliteController().execute(sql_delete, values=(list_id,), fetch_mode=SqliteController.NO_FETCH)

            return True
        except SqliteError as e:
            print(str(e))
            raise e

    @classmethod
    def rename(cls, list_id: int, new_list_name: str) -> bool:
        """Renomme une liste

            Arguments:
                list_id {int} -- Id de la liste à renommé
                new_list_name {str} -- Nouveau nom de la liste

            Returns:
                bool -- État de la requête
        """
        try:
            sql_update = "UPDATE list SET nameList = ? WHERE idList = ?"

            SqliteController().execute(sql_update, values=(new_list_name, list_id,), fetch_mode=SqliteController.NO_FETCH)

            return True
        except SqliteError as e:
            log(e)
            return False
