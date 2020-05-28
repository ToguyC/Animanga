"""Contient la classe de contrôle de la base de données Sqlite

@author: Tanguy Cavagna
@copyright: Copyright 2020, TPI
@version: 1.0.0
@date: 2020-05-26
"""
import sqlite3
#import sys
#from os import path
from typing import Any
from sqlite3 import Error as SqliteError
#from datetime import datetime as dt

from flask import g

class SqliteController:
    """Classe permettant d'accéder à ma base de données Sqlite
    """

    FETCH_ALL = 0
    FETCH_ONE = 1
    NO_FETCH = 2

    connection = None

    def __init__(self):
        """Constructeur vide
        """

    def __get_cursor(self) -> object:
        """Récupère le curseur de ma connexion
        """
        return self.get_instance().cursor()

    #pylint: disable=no-self-use
    def __dict_factory(self, cursor: object, row: object) -> dict:
        """Retourne les valeurs du fetch comme dictionnaire
            see: https://stackoverflow.com/questions/3300464/how-can-i-get-dict-from-sqlite-query

            Arguments:
                cursor {object} -- Cursor of the connection
                row {object} -- Returned rows

            Returns:
                dict -- Full dict
        """
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    def get_instance(self) -> object:
        """Récupère l'instance de connexion à la base
        """
        SqliteController.connection = getattr(g, '_database', None)
        if SqliteController.connection is None:
            SqliteController.connection = g._database = sqlite3.connect("/home/cavagnat/Documents/programmation/python/Animanga/static/database/tpi.db", detect_types=sqlite3.PARSE_DECLTYPES)
            SqliteController.connection.row_factory = self.__dict_factory

        return SqliteController.connection

    #pylint: disable=no-self-use
    def close(self) -> None:
        """Ferme la connexion courante
        """
        SqliteController.connection = getattr(g, '_database', None)
        if SqliteController.connection is not None:
            SqliteController.connection.close()

    def execute_many(self, query: str, values: tuple) -> None:
        """Fait une requete de type many. (INSERT INTO <table> VALUES(...values), (...values), (...values), ...)
        """
        cursor = self.__get_cursor()

        cursor.executemany(query, values)

        self.get_instance().commit()

    def execute(self, query: str, values = None, fetch_mode = 2) -> Any:
        """Exécute une requete en base

            Arguments:
                query {str} -- Requete à executer

            Keyword Arguments:
                values {tuple} -- Valeurs à utilisé (default: {None})
                fetch_mode {int} -- Type de fetch voulu (default: {2}) -> pas de fetch

            Returns:
                None|[]|int -- Si pas de fetch, retourne le last_row_id, sinon retourne le fetch voulu
        """
        try:
            cursor = self.__get_cursor()

            if values is not None:
                cursor.execute(query, values)
            else:
                cursor.execute(query)

            last_row_id = cursor.lastrowid

            self.get_instance().commit()

            if fetch_mode == self.FETCH_ONE:
                result = cursor.fetchone()
            elif fetch_mode == self.FETCH_ALL:
                result = cursor.fetchall()
            else:
                result = None

            if (fetch_mode == self.NO_FETCH):
                return last_row_id

            return result
        except sqlite3.Error as e:
            raise e

    # Données de la base de données

    def truncate_anime_related(self) -> None:
        """Vide toutes les tables relatives aux animes
        """
        try:
            self.execute("DELETE FROM `user_has_favorite`")
            self.execute("DELETE FROM `list_has_anime`")
            self.execute("DELETE FROM `anime_ft`")
            self.execute("DELETE FROM `anime`")
            self.execute("DELETE FROM `url`")
            self.execute("DELETE FROM `type`")
            self.execute("DELETE FROM `status`")

            return True
        except SqliteError as e:
            print(str(e))
            return False

    def setup_anime_table(self) -> None:
        """Créer la table anime si elle n'existe pas
        """
        try:
            self.execute(
                """
                    CREATE TABLE IF NOT EXISTS `anime` (
                        `idAnime` integer NOT NULL PRIMARY KEY,
                        `title` text NOT NULL,
                        `type` integer NOT NULL,
                        `episodes` integer NOT NULL,
                        `status` integer NOT NULL,
                        `picture` text NOT NULL,
                        `thumbnail` text NOT NULL,
                        `synonyms` text DEFAULT NULL,
                        `modificationDate` timestamp DEFAULT NULL,
                        FOREIGN KEY (`type`) REFERENCES `type`(`idType`),
                        FOREIGN KEY (`status`) REFERENCES `status`(`idStatus`)
                    )
                """,
                None
            )
            # Obligatoire pour pouvoir faire une recherche full text
            self.execute("CREATE VIRTUAL TABLE IF NOT EXISTS `anime_ft` USING FTS5(`idAnime`, `title`)")
            return True
        except SqliteError as e:
            print(str(e))
            return False

    def setup_type_table(self) -> None:
        """Créer la table type si elle n'existe pas
        """
        try:
            self.execute(
                """
                    CREATE TABLE IF NOT EXISTS `type` (
                        `idType` integer NOT NULL PRIMARY KEY,
                        `nameType` text NOT NULL,
                        `modificationDate` timestamp DEFAULT NULL
                    )
                """,
                None
            )
            return True
        except SqliteError as e:
            print(str(e))
            return False

    def setup_status_table(self) -> None:
        """Créer la status anime si elle n'existe pas
        """
        try:
            self.execute(
                """
                    CREATE TABLE IF NOT EXISTS `status` (
                        `idStatus` integer NOT NULL PRIMARY KEY,
                        `nameStatus` text NOT NULL,
                        `modificationDate` timestamp DEFAULT NULL
                    )
                """,
                None
            )
            return True
        except SqliteError as e:
            print(str(e))
            return False

    def setup_url_table(self) -> None:
        """Créer la url anime si elle n'existe pas
        """
        try:
            self.execute(
                """
                    CREATE TABLE IF NOT EXISTS `url` (
                        `idUrl` integer NOT NULL PRIMARY KEY,
                        `urlName` text NOT NULL,
                        `idAnime` integer NOT NULL,
                        `isRelation` integer NOT NULL,
                        `modificationDate` timestamp DEFAULT NULL,
                        FOREIGN KEY (`idAnime`) REFERENCES `anime`(`idAnime`)
                    )
                """
            )
            return True
        except SqliteError as e:
            print(str(e))
            return False

    def setup_user_table(self) -> None:
        """Créer la user anime si elle n'existe pas
        """
        try:
            self.execute(
                """
                    CREATE TABLE IF NOT EXISTS `user` (
                        `idUser` integer NOT NULL PRIMARY KEY,
                        `emailUser` text NOT NULL,
                        `password` text NOT NULL,
                        `nicknameUser` text NOT NULL,
                        `modificationDate` timestamp DEFAULT NULL
                    )
                """,
                None
            )
            return True
        except SqliteError as e:
            print(str(e))
            return False

    def setup_list_table(self) -> None:
        """Créer la list anime si elle n'existe pas
        """
        try:
            self.execute(
                """
                    CREATE TABLE IF NOT EXISTS `list` (
                        `idList` integer NOT NULL PRIMARY KEY,
                        `nameList` text NOT NULL,
                        `modificationDate` timestamp DEFAULT NULL
                    )
                """,
                None
            )
            return True
        except SqliteError as e:
            print(str(e))
            return False

    def setup_user_has_list_table(self) -> None:
        """Créer la user_has_list anime si elle n'existe pas
        """
        try:
            self.execute(
                """
                    CREATE TABLE IF NOT EXISTS `user_has_list` (
                        `idUserHasList` integer NOT NULL PRIMARY KEY,
                        `idUser` integer NOT NULL REFERENCES `user`(`idUser`),
                        `idList` integer NOT NULL REFERENCES `list`(`idList`),
                        `modificationDate` timestamp DEFAULT NULL
                    )
                """,
                None
            )
            return True
        except SqliteError as e:
            print(str(e))
            return False

    def setup_list_has_anime_table(self) -> None:
        """Créer la table list_has_anime si elle n'existe pas
        """
        try:
            self.execute(
                """
                    CREATE TABLE IF NOT EXISTS `list_has_anime` (
                        `idListHasAnime` integer NOT NULL PRIMARY KEY,
                        `idList` integer NOT NULL REFERENCES `list`(`idList`),
                        `idAnime` integer NOT NULL REFERENCES `anime`(`idAnime`),
                        `modificationDate` timestamp DEFAULT NULL
                    )
                """,
                None
            )
            return True
        except SqliteError as e:
            print(str(e))
            return False

    def setup_user_has_favorite_table(self) -> None:
        """Créer la table user_has_favorite si elle n'existe pas
        """
        try:
            self.execute(
                """
                    CREATE TABLE IF NOT EXISTS `user_has_favorite` (
                        `idUserHasFavorite` integer NOT NULL PRIMARY KEY,
                        `idUser` integer NOT NULL REFERENCES `user`(`idUser`),
                        `idAnime` integer NOT NULL REFERENCES `anime`(`idAnime`),
                        `orderId` integer NOT NULL,
                        `modificationDate` timestamp DEFAULT NULL
                    )
                """,
                None
            )
            return True
        except SqliteError as e:
            print(str(e))
            return False
