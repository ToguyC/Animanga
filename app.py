"""Contient le coeur de l'application

Toutes les routes de l'appplication sont décrites dans ce fichier.

@author: Tanguy Cavagna
@copyright: Copyright 2020, TPI
@version: 1.0.0
@date: 2020-05-26
"""
from flask import Flask, url_for, redirect, flash, g
from flask_login import LoginManager
from dotenv import load_dotenv

from .config import DevConfig, ProdConfig
from .packages.controllers.UserController import UserController

app = Flask(__name__)
app.config.from_object(DevConfig())
app.secret_key = "8185c8ac4656219f4aa5541915079f7b3743e1b5f48bacfcc3386af016b55320"

login_manager = LoginManager()
login_manager.init_app(app)

# Chargement des routes
with app.app_context():
    from . import routes, auth

    # Enregistre les routes
    app.register_blueprint(routes.main_bp)
    app.register_blueprint(auth.auth_bp)

# ================
#      OTHER
# ================
@login_manager.user_loader
def load_user(user_id):
    """Test si l'utilisateur est connecté sur toutes les pages. Si oui, retourne l'utilisateur"""
    if user_id is not None:
        return UserController().get_by_id(user_id)
    return None

# ================
#       Run
# ================
if __name__ == "__main__":
    app.run()