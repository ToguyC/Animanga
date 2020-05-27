"""Contient la classe de contrôle des utilisateurs

@author: Tanguy Cavagna
@copyright: Copyright 2020, TPI
@version: 1.0.0
@date: 2020-05-27
"""
from datetime import datetime as dt

from sqlite3 import Error as SqliteError
from .SqliteController import SqliteController
from .TypeController import TypeController
from ..models.User import User

class UserController:
    """Contrôleur d'un utilisateur
    """

    @classmethod
    def exists(cls, email: str) -> bool:
        """Test is l'email existe déjà en base

            Arguments:
                email {str} -- Email à tester
            
            Returns:
                bool -- Est-ce que l'email existe
        """
        try:
            sql_exists = "SELECT COUNT(*) AS `Count` FROM user WHERE emailUser = ?"

            count = SqliteController().execute(sql_exists, values=(email,), fetch_mode=SqliteController.FETCH_ONE)['Count']

            return bool(count > 0)
        except SqliteError as e:
            print(str(e))
            return True

    @classmethod
    def check_password(cls, email: str, hashed_password: str) -> bool:
        """Test la validité du mot de passe

            Arguments:
                email {str} -- Email de l'utiliateur à tester
                hashed_password {str} -- Mot de passe à tester

            Returns:
                bool -- Est-ce que le mot de passe est valide
        """
        try:
            sql_check = "SELECT COUNT(*) AS `Count` FROM user WHERE emailUser = ? AND password = ?"

            count = SqliteController().execute(sql_check, values=(email, hashed_password,), fetch_mode=SqliteController.FETCH_ONE)['Count']

            return bool(count == 1)
        except SqliteError as e:
            print(str(e))
            return False

    @classmethod
    def insert(cls, email: str, nickname: str, password: str) -> User:
        """Insère un nouvel utilisateur en base

            Arguments:
                email {str} -- Email
                nickname {str} -- Pseudo
                passowrd {str} -- Mot de passe

            Returns:
                User -- Nouvel utilisateur créé
        """
        try:
            sql_insert = "INSERT INTO user(emailUser, password, nicknameUser, modificationDate) VALUES(?, ?, ?, ?)"

            values_user = ((
                email,
                password,
                nickname,
                dt.now()
            ))

            last_row_id = SqliteController().execute(sql_insert, values=values_user, fetch_mode=SqliteController.NO_FETCH)

            return User(last_row_id, email, nickname)
        except SqliteError as e:
            print(str(e))
            return None

    @classmethod
    def get_by_id(cls, user_id: int) -> User:
        """Récupère l'utilisateur via son id

            Arguments:
                user_id {int} -- Id de l'utilisateur à récupèrer

            Returns:
                User -- Utilisateur trouvé
        """
        try:
            sql_select = "SELECT * FROM user WHERE idUSer = ?"

            user_dict = SqliteController().execute(sql_select, values=(user_id,), fetch_mode=SqliteController.FETCH_ONE)

            if user_dict is not None:
                return User(user_dict['idUser'], user_dict['emailUser'], user_dict['nicknameUser'])

            return None
        except SqliteError as e:
            print(str(e))
            return None

    @classmethod
    def get_by_email(cls, email: str) -> User:
        """Récupère un utilisateur via son email

            Argument:
                email {str} -- Email de l'utilisateur

            Returns:
                User -- Utilisateur trouvé
        """
        try:
            sql_select = "SELECT * FROM user WHERE emailUser = ?"

            user_dict = SqliteController().execute(sql_select, values=(email,), fetch_mode=SqliteController.FETCH_ONE)

            if user_dict is not None:
                return User(user_dict['idUser'], user_dict['emailUser'], user_dict['nicknameUser'])

            return None
        except SqliteError as e:
            print(str(e))
            return None
