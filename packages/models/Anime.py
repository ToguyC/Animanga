"""Contient le model d'un anime

@author: Tanguy Cavagna
@copyright: Copyright 2020, TPI
@version: 1.0.0
@date: 2020-05-28
"""

class Anime:
    """Modèle d'un anime
    """

    def __init__(self, anime_id: int, title: str, anime_type: str, episodes: int, status: str, picture: str, thumbnail: str, synonyms: str):
        self.id = anime_id
        self.title = title
        self.type = anime_type
        self.episodes = episodes
        self.status = status
        self.picture = picture
        self.thumbnail = thumbnail
        self.synonims = synonyms
        self.relations = None
        self.is_favorite = None
        self.in_list = None

    def serialize(self) -> dict:
        """Sérialise les données
        """
        return {
            'id': self.id,
            'title': self.title,
            'type': self.type,
            'episodes': self.episodes,
            'status': self.status,
            'picture': self.picture,
            'thumbnail': self.thumbnail,
            'synonims': self.synonims,
            'relations': self.relations,
            'is_favorite': self.is_favorite
        }
        