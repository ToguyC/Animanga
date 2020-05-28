"""Contient le model d'une liste

@author: Tanguy Cavagna
@copyright: Copyright 2020, TPI
@version: 1.0.0
@date: 2020-05-28
"""

class List:
    """Modèle d'une liste
    """

    def __init__(self, list_id: int, name: str):
        self.id = list_id
        self.name = name

    def serialize(self) -> dict:
        """Sérialise les données
        """
        return {
            'id': self.id,
            'name': self.name
        }