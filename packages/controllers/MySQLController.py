"""Contient la classe de contrôle de la base de données MySQL

@author: Tanguy Cavagna
@copyright: Copyright 2020, TPI
@version: 1.0.0
@date: 2020-06-04
"""
from typing import Any

import mysql.connector
from mysql.connector import Error
from .logger import log

class MySQLController:
    """Classe permettant d'accéder à ma base de données MySQL
    """

    #region Public constants
    FETCH_ALL = 0
    FETCH_ONE = 1
    NO_FETCH = 2
    #endregion

    def __init__(self):
        """Constructeur vide
        """  

    def __getattr__(self, attr):
        """Essaie d'accéder à une variable ou fonction innexistante
        """
        return "Tried to handle unknown method / attribute : {0}".format(attr)

    def __connection(self) -> mysql.connector.MySQLConnection:
        """Créer et retourne la connexion

            Returns:
                {mysql.connector.MySQLConnection} -- Nouvelle connexion
        """
        return mysql.connector.connect(host='localhost',
                                       database='tpi',
                                       user='root',
                                       password='root')
    
    def openConnection(self) -> mysql.connector.MySQLConnection:
        """Ouvre une connexion
        
            Returns:
               {mysql.connector.MySQLConnection} -- Connection to the database
        """
        return self.__connection()

    def closeConnection(self, connection) -> None:
        """Ferme une connexion données

            Arguments:
                connection {mysql.connector.MySQLConnection} -- Connexion à fermer
        """
        connection.close()

    def executeMany(self, connection, query, values) -> None:
        """Fait une requete de type many. (INSERT INTO <table> VALUES(...values), (...values), (...values), ...)

            Arguments:
                connection {mysql.connector.MySQLConnection} -- Connexion sur laquelle faire la requête
                query {str} -- Requête à faire
                values {tuple} -- Valeurs à attribué à la requête
        """
        try:
            cursor = connection.cursor(prepared=True)
            cursor.executemany(query, values)
            connection.commit()
        except Error as e:
            log(e)

    def executePrepare(self, connection, query, values = None, fetch_mode = 0) -> Any:
        """Éxecute une requête préparée
        
            Arguments:
                connection {mysql.connector.MySQLConnection} -- Connexion sur laquelle faire la requête
                query {str} -- Requête à faire
            
            Keyword Arguments:
                values {tuple} -- Valeurs à attribué à la requête (default: {None})
                fetch_mode {int} -- Type de fetch (default: {0})

            Returns:
                Depending on which fetch mod you are, you could get bool or a list of tuples
        """
        rows = None

        try:
            cursor = connection.cursor(prepared=True)

            cursor.execute(query, values)

            fields_names = [i[0] for i in cursor.description]

            # Fetch datas
            if fetch_mode == self.FETCH_ALL:
                results = cursor.fetchall()

                rows = [dict(zip(fields_names, results[i])) for i in range(len(results))]
            elif fetch_mode == self.FETCH_ONE:
                rows = cursor.fetchone()
            elif fetch_mode == self.NO_FETCH:
                rows = None
        
            # Return datas
            if rows is not None:
                return rows

            return None
        except Error as e:
            log(e)
            return False
        finally:
            self.closeConnection(connection)

    def executeQuery(self, connection, query, values = None, fetch_mode = 0, last_insert_id = False, close_connection = True) -> Any:
        """Execute and retrieve data from querie
        
            Arguments:
                connection {mysql.connector.MySQLConnection} -- Connexion sur laquelle faire la requête
                query {str} -- Requête à faire

            Keyword Arguments:
                values {tuple} -- Valeurs à attribué à la requête (default: {None})
                fetch_mode {int} -- Type de fetch (default: {0})
                last_insert_id {bool} -- Retourne le last_insert_id ou pas (default: {False})
                close_connection {bool} -- Fermer la connexion à la fin de l'éxecution de la requête
            
            Returns:
                Depending on which fetch mod you are, you could get bool or a list of tuples
        """
        rows = None
        last_id = None

        try:
            cursor = connection.cursor(dictionary=True)
            
            # Execute the query
            if (values is not None):
                cursor.execute(query, values)
                if not query.startswith("SELECT"):
                    connection.commit()
            else:
                cursor.execute(query)
                if query.startswith("DELETE"):
                    connection.commit()
                

            # Fetch datas
            if fetch_mode == self.FETCH_ALL:
                rows = cursor.fetchall()
            elif fetch_mode == self.FETCH_ONE:
                rows = cursor.fetchone()
            elif fetch_mode == self.NO_FETCH:
                rows = None

            if last_insert_id:
                last_id = cursor.lastrowid

            if last_id is not None:
                return last_id

            # Return datas
            if rows is not None:
                return rows

            return None
        except Error as e:
            log(e)
            return False
        finally:
            if close_connection:
                self.closeConnection(connection)