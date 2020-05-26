"""Contient le model d'un status

@author: Tanguy Cavagna
@copyright: Copyright 2020, TPI
@version: 1.0.0
@date: 2020-05-26
"""

class Status:
    """Modèle d'un statut
    """

    def __init__(self, status_id: int, name: str):
        self.id = status_id
        self.name = name

    def serialize(self) -> dict:
        """Sérialise les données
        """
        return {
            'id': self.id,
            'name': self.name
        }