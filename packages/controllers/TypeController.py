"""Contient la classe de contrôle des types
Les types d'anime sont : Special, Movie, ONA, TV

@author: Tanguy Cavagna
@copyright: Copyright 2020, TPI
@version: 1.0.0
@date: 2020-05-26
"""
from sqlite3 import Error as SqliteError

from .SqliteController import SqliteController
from ..models.Type import Type
from .logger import log

class TypeController:
    """Controlleur des types
    """

    def __init__(self):
        pass
    
    @classmethod
    def get_all(cls) -> [Type]:
        """Récupère tout les types
        
            Returns:
                [Type] -- Listes contenant des types
        """
        try:
            rows = SqliteController().execute("SELECT `idType`, `nameType` FROM `type`", fetch_mode=SqliteController().FETCH_ALL)
            types = [Type(t['idType'], t['nameType']) for t in rows]

            return types
        except SqliteError as e:
            log(e)
            raise e

    @classmethod
    def get_all_as_dict(cls) -> dict:
        """Récupère tout les types sous forme de dictionnaire
        
            Returns:
                dict -- Dictionnaire contenant les types avec le format "name": id
        """
        types = {}
        for t in cls.get_all():
            types.update({t.name: t.id})

        return types