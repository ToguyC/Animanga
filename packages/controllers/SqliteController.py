"""Contient la classe de contrôle de la base de données Sqlite

@author: Tanguy Cavagna
@copyright: Copyright 2020, TPI
@version: 1.0.0
@date: 2020-05-26
"""
import sqlite3
from typing import Any
from sqlite3 import Error as SqliteError
from mysql.connector import Error as MysqlError
from flask import g

from .MySQLController import MySQLController
from .logger import log

class SqliteController:
    """Classe permettant d'accéder à ma base de données Sqlite
    """

    FETCH_ALL = 0
    FETCH_ONE = 1
    NO_FETCH = 2

    connection = None

    @classmethod
    def __get_cursor(cls) -> object:
        """Récupère le curseur de ma connexion
        """
        return cls.get_instance().cursor()

    #pylint: disable=no-self-use
    @classmethod
    def __dict_factory(cls, cursor: object, row: object) -> dict:
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

    @classmethod
    def get_instance(cls) -> object:
        """Récupère l'instance de connexion à la base
        """
        SqliteController.connection = getattr(g, '_database', None)
        if SqliteController.connection is None:
            SqliteController.connection = g._database = sqlite3.connect("/home/cavagnat/Documents/programmation/python/Animanga/static/database/tpi.db", detect_types=sqlite3.PARSE_DECLTYPES)
            SqliteController.connection.row_factory = cls.__dict_factory

        return SqliteController.connection

    #pylint: disable=no-self-use
    @classmethod
    def close(cls) -> None:
        """Ferme la connexion courante
        """
        SqliteController.connection = getattr(g, '_database', None)
        if SqliteController.connection is not None:
            SqliteController.connection.close()

    @classmethod
    def execute_many(cls, query: str, values: tuple) -> None:
        """Fait une requete de type many. (INSERT INTO <table> VALUES(...values), (...values), (...values), ...)
        """
        cursor = cls.__get_cursor()

        cursor.executemany(query, values)

        cls.get_instance().commit()

    @classmethod
    def execute(cls, query: str, values = None, fetch_mode = 2) -> Any:
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
            cursor = cls.__get_cursor()

            if values is not None:
                cursor.execute(query, values)
            else:
                cursor.execute(query)

            last_row_id = cursor.lastrowid

            cls.get_instance().commit()

            if fetch_mode == cls.FETCH_ONE:
                result = cursor.fetchone()
            elif fetch_mode == cls.FETCH_ALL:
                result = cursor.fetchall()
            else:
                result = None

            if (fetch_mode == cls.NO_FETCH):
                return last_row_id

            return result
        except sqlite3.Error as e:
            raise e

    # Données de la base de données

    @classmethod
    def truncate_anime_related(cls) -> None:
        """Vide toutes les tables relatives aux animes
        """
        try:
            cls.execute("DELETE FROM `user_has_favorite`")
            cls.execute("DELETE FROM `list_has_anime`")
            cls.execute("DELETE FROM `anime_ft`")
            cls.execute("DELETE FROM `anime`")
            cls.execute("DELETE FROM `url`")
            cls.execute("DELETE FROM `type`")
            cls.execute("DELETE FROM `status`")

            return True
        except SqliteError as e:
            log(e)
            return False

    @classmethod
    def setup_anime_table(cls) -> None:
        """Créer la table anime si elle n'existe pas
        """
        try:
            cls.execute(
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
            cls.execute("CREATE VIRTUAL TABLE IF NOT EXISTS `anime_ft` USING FTS5(`idAnime`, `title`)")
            return True
        except SqliteError as e:
            log(e)
            return False

    @classmethod
    def setup_type_table(cls) -> None:
        """Créer la table type si elle n'existe pas
        """
        try:
            cls.execute(
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
            log(e)
            return False

    @classmethod
    def setup_status_table(cls) -> None:
        """Créer la status anime si elle n'existe pas
        """
        try:
            cls.execute(
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
            log(e)
            return False

    @classmethod
    def setup_url_table(cls) -> None:
        """Créer la url anime si elle n'existe pas
        """
        try:
            cls.execute(
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
            log(e)
            return False

    @classmethod
    def setup_user_table(cls) -> None:
        """Créer la user anime si elle n'existe pas
        """
        try:
            cls.execute(
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
            log(e)
            return False

    @classmethod
    def setup_list_table(cls) -> None:
        """Créer la list anime si elle n'existe pas
        """
        try:
            cls.execute(
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
            log(e)
            return False

    @classmethod
    def setup_user_has_list_table(cls) -> None:
        """Créer la user_has_list anime si elle n'existe pas
        """
        try:
            cls.execute(
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
            log(e)
            return False

    @classmethod
    def setup_list_has_anime_table(cls) -> None:
        """Créer la table list_has_anime si elle n'existe pas
        """
        try:
            cls.execute(
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
            log(e)
            return False

    @classmethod
    def setup_user_has_favorite_table(cls) -> None:
        """Créer la table user_has_favorite si elle n'existe pas
        """
        try:
            cls.execute(
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
            log(e)
            return False

    # pylint: disable=too-many-locals,too-many-nested-blocks
    @classmethod
    def synchronise_with_mysql(cls) -> bool:
        """Synchronise la base MySQL avec Sqlite3

            Returns:
                bool -- Status de la synchronisation
        """
        try:
            tables = {
                'type': 'idType',
                'status': 'idStatus',
                'anime': 'idAnime',
                'url': 'idUrl',
                'user': 'idUser',
                'list': 'idList',
                'user_has_list': 'idUserHasList',
                'list_has_anime': 'idListHasAnime',
                'user_has_favorite': 'idUserHasFavorite',
            }
            sql_table_columns = "PRAGMA table_info("
            sql_entries = "SELECT * FROM "
            sql_insert = "INSERT INTO "
            sql_delete = "DELETE FROM "

            connection = MySQLController().openConnection()
            MySQLController().executeQuery(connection, "SET FOREIGN_KEY_CHECKS=0;", fetch_mode=MySQLController.NO_FETCH, close_connection=False)

            for current_table in tables:
                print('TABLE COURANTE :', current_table)

                # Récupération des noms de colonnes de la table courante
                current_tables_columns = SqliteController().execute(sql_table_columns + current_table + ')', fetch_mode=SqliteController.FETCH_ALL)
                current_tables_columns = [item['name'] for item in current_tables_columns]

                # Récupération des enregistrements de la table courante sur sqlite et mysql
                sqlite_entries = cls.execute(sql_entries + current_table, fetch_mode=SqliteController.FETCH_ALL)
                mysql_entries = MySQLController().executeQuery(connection, sql_entries + current_table, fetch_mode=MySQLController.FETCH_ALL, close_connection=False)

                # Création d'un tableau contenant l'id et la modificationDate de chaque enregistrement
                sqlite_ids_timestamps = [{'id': sqlite_entry[tables[current_table]], 'timestamp': sqlite_entry['modificationDate'].replace(microsecond=0)} for sqlite_entry in sqlite_entries]
                mysql_ids_timestamps = [({'id': mysql_entry[tables[current_table]], 'timestamp': mysql_entry['modificationDate'].replace(microsecond=0)}) for mysql_entry in mysql_entries]

                # Tri des tableaux par id
                sqlite_ids_timestamps = sorted(sqlite_ids_timestamps, key=lambda k: k['id'])
                mysql_ids_timestamps = sorted(mysql_ids_timestamps, key=lambda k: k['id'])
                
                print('Data same', len(sqlite_entries) == len(mysql_entries))
                ids_to_skip_for_update = []
                # Ajout des données manquantes mysql et suppression des données en trop mysql
                if len(sqlite_entries) != len(mysql_entries):
                    # Ajout des éléments manquants dans mysql
                    ids_non_present_in_mysql = []
                    if len(sqlite_ids_timestamps) > len(mysql_ids_timestamps):
                        # Éléments non présents dans la table myqsl
                        ids_non_present_in_mysql = [i['id'] for i in sqlite_ids_timestamps if i['id'] not in [j['id'] for j in mysql_ids_timestamps]]

                        # Récupère les valeurs sqlite a ajouté dans mysql seulement si elles ne sont déjà présentes dans mysql
                        values_to_append = []
                        for sqlite_entry in sqlite_entries:
                            if sqlite_entry[tables[current_table]] in ids_non_present_in_mysql:
                                values_to_append.append(tuple(sqlite_entry.values()))
                                ids_to_skip_for_update.append(sqlite_entry[tables[current_table]])

                        # Construction de la requête d'ajout de données et insertion des données dans mysql
                        columns_list = ''
                        for column in current_tables_columns: columns_list += column + ','
                        parameter_list = ''
                        for _ in range(len(current_tables_columns)): parameter_list += '%s,'
                        # Format de la requete :
                        #       INSERT INTO <table>(...champs) VALUES(...valeurs)
                        MySQLController().executeMany(connection,
                                                         sql_insert + current_table + "(" + columns_list[:-1] + ") VALUES(" + parameter_list[:-1] + ")",
                                                         values=values_to_append)
                    # Suppression des éléments en trop de mysql
                    elif len(sqlite_ids_timestamps) < len(mysql_ids_timestamps):
                        # Éléments non présents dans la tablea sqlite
                        ids_non_present_in_sqlite = [i['id'] for i in mysql_ids_timestamps if i['id'] not in [j['id'] for j in sqlite_ids_timestamps]]

                        # Construction de la requête de suppressions de données
                        delete_list = ''
                        for delete in ids_non_present_in_sqlite: delete_list += str(delete) + ','

                        # Format de la requete :
                        #       DELETE FROM <table> WHERE <id table> IN (...valeurs)
                        MySQLController().executeQuery(connection,
                                                         sql_delete + current_table + " WHERE " + tables[current_table] + " IN (" + delete_list[:-1] + ")",
                                                         fetch_mode=MySQLController.NO_FETCH,
                                                         close_connection=False)

                # Réafectation des variables pour avoir les données à jour
                mysql_entries = MySQLController().executeQuery(connection, sql_entries + current_table, fetch_mode=MySQLController.FETCH_ALL, close_connection=False)
                mysql_ids_timestamps = [({'id': mysql_entry[tables[current_table]], 'timestamp': mysql_entry['modificationDate'].replace(microsecond=0)}) for mysql_entry in mysql_entries]
                mysql_ids_timestamps = sorted(mysql_ids_timestamps, key=lambda k: k['id'])

                # Récupération des id à mettre à jour dans mysql
                elements_to_updates = []
                for sqlite_element in mysql_ids_timestamps:
                    if sqlite_element['id'] not in ids_to_skip_for_update:
                        # Format de la requete :
                        #       SELECT <id table> AS `id` FROM <table> WHERE modificationDate NOT LIKE '<date mysql>%' AND <id table> = <id mysql>
                        # Je suis obliger de mettre le `NOT LIKE` pour la date car Sqlite contient les millisecondes et pas mysql
                        entry = SqliteController().execute("SELECT " + tables[current_table] + " AS `id` FROM " + current_table + " WHERE modificationDate NOT LIKE '" + str(sqlite_element['timestamp']) + "%' AND " + tables[current_table] + " = " + str(sqlite_element['id']),
                                                           fetch_mode=SqliteController.FETCH_ONE)
                        if entry is not None:
                            elements_to_updates.append(entry['id'])

                print(elements_to_updates)
                # A voir avec Bonvin car trop long
                for index in elements_to_updates:
                    # Récupération des valeurs sqlite à mettre dans mysql
                    values_to_append = None
                    for item in sqlite_entries:
                        if item[tables[current_table]] == index:
                            # [1:] pour éviter de prendre l'id
                            values_to_append = tuple(list(item.values())[1:])
                            break
                        
                    # Mise à jours des données mysql avec les valeurs sqlite
                    set_list = ''
                    # [1:] pour éviter de mettre à jour l'id
                    for column in current_tables_columns[1:]: set_list += column + "=%s,"
                    MySQLController().executeQuery(connection,
                                                      "UPDATE " + current_table + " SET " + set_list[:-1] + " WHERE " + tables[current_table] + " = " + str(index),
                                                      values=values_to_append,
                                                      fetch_mode=MySQLController.NO_FETCH, 
                                                      close_connection=False)
            MySQLController().executeQuery(connection, "SET FOREIGN_KEY_CHECKS=1;", fetch_mode=MySQLController.NO_FETCH, close_connection=False)
            MySQLController().closeConnection(connection)
            return True
        except (SqliteError, MysqlError, ValueError, TypeError) as e:
            log(e)
            return False
