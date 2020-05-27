"""Contient le model d'un utilisateur

@author: Tanguy Cavagna
@copyright: Copyright 2020, TPI
@version: 1.0.0
@date: 2020-05-27
"""
from flask_login import UserMixin

class User(UserMixin):
    """Modèle d'un utilisateur. Classe héritée de UserMixin pour pouvoir être prise en compte comme classe de flask-loggin
    """
    
    def __init__(self, user_id: int, email: str, nickname: str):
        self.id = user_id
        self.email = email
        self.nickname = nickname

    def serialize(self) -> dict:
        """Sérialise les données
        """
        return {
            'id': self.id,
            'email': self.email,
            'nickname': self.nickname
        }