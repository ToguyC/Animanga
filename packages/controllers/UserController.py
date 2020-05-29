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
from .logger import log

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
            log(e)
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
            log(e)
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
            log(e)
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
            log(e)
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
            log(e)
            return None

    @classmethod
    def get_by_nickname(cls, nickname: str) -> User:
        """Récupère un utilisateur via son pseudo

            Arguments:
                nickname {str} -- Pseudo de l'utilisateur cherché
            
            Returns:
                User -- Utilisateur trouvé
        """
        try:
            sql_select = "SELECT * FROM user WHERE nicknameUser = ?"

            user_dict = SqliteController().execute(sql_select, values=(nickname,), fetch_mode=SqliteController.FETCH_ONE)

            if user_dict is not None:
                return User(user_dict['idUser'], user_dict['emailUser'], user_dict['nicknameUser'])

            return None
        except SqliteError as e:
            log(e)
            return None

    @classmethod
    def setup_default_lists(cls, user_id: int) -> bool:
        """Créer les listes par défaut si inexistantes

            Arguments:
                user_id {int} -- Id de l'utilisateur
            
            Returns:
                bool -- `True` si tout c'est bien passé
        """
        try:
            sql_default_list = "INSERT INTO list(nameList, modificationDate) VALUES(?, ?)"
            sql_link_list_user = "INSERT INTO user_has_list(idUser, idList, modificationDate) VALUES(?, ?, ?)"

            values_list = [
                'Complétés',
                'En cours',
                'Abandonés',
                'Planifiés'
            ]

            current_time = dt.now()
            for list_name in values_list:
                list_id = SqliteController().execute(sql_default_list, values=(list_name,current_time,), fetch_mode=SqliteController.NO_FETCH)
                SqliteController().execute(sql_link_list_user, values=(user_id,list_id,current_time,), fetch_mode=SqliteController.NO_FETCH)

            return True
        except SqliteError as e:
            log(e)
            return False

    @classmethod
    def get_stats_by_id(cls, user_id: int) -> []:
        """Récupère les statistiques pour un utilisateur

            Arguments:
                user_id {int} -- Id de l'utilisateur
            
            Returns:
                [] -- Liste des statistiques
        """
        try:
            sql_stats = """SELECT COUNT(*) AS `Count`
                           FROM anime
                           WHERE idAnime IN (
                               SELECT list_has_anime.idAnime
                               FROM user_has_list
                               JOIN list_has_anime ON user_has_list.idList = list_has_anime.idList
                               WHERE user_has_list.idUser = ?
                               AND user_has_list.idList = (
                                   SELECT list.idList
                                   FROM list
                                   JOIN user_has_list ON list.idList = user_has_list.idList
                                   WHERE user_has_list.idUser = ?
                                   AND list.nameList LIKE "Complétés"
                               )
                           )
                           AND type = (
                               SELECT idType
                               FROM type
                               WHERE nameType LIKE ?
                           )"""
            
            types = TypeController().get_all()

            stats = {}
            for t in types:
                stats[t.name] = SqliteController().execute(sql_stats, values=(user_id,user_id,t.name,), fetch_mode=SqliteController.FETCH_ONE)['Count']

            return stats
        except SqliteError as e:
            log(e)
            return []
