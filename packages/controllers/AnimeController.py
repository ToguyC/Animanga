"""Contient la classe de contrôle des animes

@author: Tanguy Cavagna
@copyright: Copyright 2020, TPI
@version: 1.0
@date: 2020-05-26
"""
import json
import pathlib
import sys
import os
from sqlite3 import Error as SqliteError
from datetime import datetime as dt

from .SqliteController import SqliteController
from .TypeController import TypeController
from .StatusController import StatusController

class AnimeController:
    """Controlleur d'un anime
    """

    @classmethod
    def override_local_with_json(cls, path: str) -> None:
        """Écrase toutes les données en base

            Arguments:
                path {string} -- Chemin du fichier json
        """
        with open(pathlib.Path(__file__).parent / path, 'r', encoding="utf8") as f:
            animes = json.load(f)

        try:
            # Mise en place des tables si elles ne sont pas présente et truncate tout ce qui est en lien direct avec la table 'anime'
            if not SqliteController().setup_type_table(): return False
            if not SqliteController().setup_status_table(): return False
            if not SqliteController().setup_anime_table(): return False
            if not SqliteController().setup_url_table(): return False
            if not SqliteController().setup_user_table(): return False
            if not SqliteController().setup_list_table(): return False
            if not SqliteController().setup_user_has_list_table(): return False
            if not SqliteController().setup_list_has_anime_table(): return False
            if not SqliteController().setup_user_has_favorite_table(): return False
            if not SqliteController().truncate_anime_related(): return False

            # Requêtes pour les insertions de nouvelles données
            sql_query_type = "INSERT INTO type(nameType, modificationDate) VALUES(?, ?)"
            sql_query_status = "INSERT INTO status(nameStatus, modificationDate) VALUES(?, ?)"
            sql_query_anime = "INSERT INTO anime(title, type, episodes, status, picture, thumbnail, synonyms, modificationDate) VALUES(?, ?, ?, ?, ?, ?, ?, ?)"
            sql_query_anime_ft = "INSERT INTO anime_ft(idAnime, title) VALUES(?, ?)"
            sql_query_url = "INSERT INTO url(urlName, idAnime, isRelation, modificationDate) VALUES(?, ?, ?, ?)"

            # Tableaux ayant pour but de stocké les futures valeurs à mettre dans les table pour faire un insert_many
            values_type = []
            values_status = []
            values_anime = []
            values_anime_ft = []
            values_source = []
            values_relation = []

            current_time = dt.now()

            yield "Récupération des types et status"

            # Récupération des statuts et des types
            for anime in animes['data']:
                # Suppression de tout les OVA car souvent ayant un contenu innaproprié pour un TPI
                if anime['type'] == 'OVA':
                    continue
                
                # Ajout distinct des types
                if not any(anime['type'] in i for i in values_type):
                    values_type.append((
                        anime['type'],
                        current_time
                    ))

                # Ajout distinct des statuts
                if not any(anime['status'] in i for i in values_status):
                    values_status.append((
                        anime['status'],
                        current_time
                    ))

            yield "Insertion des types et status"
            SqliteController().execute_many(sql_query_type, values_type)
            SqliteController().execute_many(sql_query_status, values_status)

            yield "Récupération des animes et urls"
            types = TypeController().get_all_as_dict()
            status = StatusController().get_all_as_dict()

            print(len(types), len(status))

            yield 'redirect'
        except SqliteError as e:
            print(str(e))
            return False