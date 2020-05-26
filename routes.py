"""Contient les routes de l'application

@author: Tanguy Cavagna
@copyright: Copyright 2020, TPI
@version: 1.0.0
@date: 2020-05-26
"""
from flask import render_template, Response, stream_with_context, jsonify, request, Blueprint
from flask import current_app as app
from flask_swagger import swagger
from flask_login import current_user, login_required

# Configuration du Blueprint
main_bp = Blueprint('main_bp', __name__,
                    template_folder='templates',
                    static_folder='static')

# ================
#       GET
# ================
@main_bp.route('/')
def home():
    """Affiche la page d'accueil
    """
    return render_template('index.html')
