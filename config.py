"""Contient les différentes configuration du serveur Flask

@author: Tanguy Cavagna
@copyright: Copyright 2020, TPI
@version: 1.0.0
@date: 2020-05-26
"""
class ProdConfig:
    TESTING = False
    DEBUG = False
    TEMPLATES_AUTO_RELOAD = False

class DevConfig:
    TESTING = True
    DEBUG = True
    TEMPLATES_AUTO_RELOAD = True