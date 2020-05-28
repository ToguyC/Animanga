"""Contient la classe de contrôle des status
Les status sont : FINISHED, CURRENTLY, UPCOMING, UNKNOWN

@author: Tanguy Cavagna
@copyright: Copyright 2020, TPI
@version: 1.0.0
@date: 2020-05-26
"""
from sqlite3 import Error as SqliteError
from .SqliteController import SqliteController
from ..models.Status import Status

class StatusController:
    """Controlleur des status
    """

    def __init__(self):
        pass
    
    @classmethod
    def get_all(cls) -> [Status]:
        """Récupère tout les statuts
        
            Returns:
                [Status] -- Listes contenant les statuts
        """
        try:
            rows = SqliteController().execute("SELECT `idStatus`, `nameStatus` FROM `status`", fetch_mode=SqliteController().FETCH_ALL)
            status = [Status(t['idStatus'], t['nameStatus']) for t in rows]

            return status
        except SqliteError as e:
            log(e)
            raise e

    @classmethod
    def get_all_as_dict(cls) -> dict:
        """Récupère tout les statuts sous forme de dictionnaire
        
            Returns:
                dict -- Dictionnaire contenant les statuts avec le format "name": "id"
        """
        status = {}
        for s in cls.get_all():
            status.update({s.name: s.id})

        return status