"""Contient la classe de contrôle des utilisateurs

@author: Tanguy Cavagna
@copyright: Copyright 2020, TPI
@version: 1.0.0
@date: 2020-05-28
"""
from .SqliteController import SqliteError, SqliteController
from .logger import log
from ..models.List import List

class ListControlleur:
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
