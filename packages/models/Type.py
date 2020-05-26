"""Contient le model d'un type

@author: Tanguy Cavagna
@copyright: Copyright 2020, TPI
@version: 1.0.0
@date: 2020-05-26
"""

class Type:
    """Modèle d'un type
    """

    def __init__(self, type_id: int, name: str):
        self.id = type_id
        self.name = name

    def serialize(self) -> dict:
        """Sérialise les données
        """
        return {
            'id': self.id,
            'name': self.name
        }