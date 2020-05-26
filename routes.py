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

from .packages.controllers.AnimeController import AnimeController

# Configuration du Blueprint
main_bp = Blueprint('main_bp', __name__,
                    template_folder='templates',
                    static_folder='static')

# ================
#      STREAM
# ================
def stream_template(template_name, **context):
    """Le but est de récupérer l'objet template de Jinja2 et d'appeler la fonction stream() qui renvoie un stream au lieu de render() qui renvoie un string.
    Étant donné que l'on bypass le template de Flask, on doit être sûre de mettre à jour de template nous meme en appelant update_template_context().
    Le template sera évalué chaque fois que le stream sera modifier. À chaque yield, le serveur va envoyer le contenu au client et donc modifier le stream.
    
    Arguments:
        template_name {string} -- Nom du template a appeler
        **context -- Tous les autres argument mixes représentant les variables à envoyer au template
    
    Returns:
        stream -- Stream à envoyer
    """
    # https://flask.palletsprojects.com/en/1.1.x/patterns/streaming/
    app.update_template_context(context)
    t = app.jinja_env.get_template(template_name)
    rv = t.stream(context)
    return rv

# ================
#       GET
# ================
@main_bp.route('/')
def home():
    """Affiche la page d'accueil
    """
    return render_template('index.html')

@main_bp.route('/endpoints', methods=['GET'])
def endpoints():
    """Affiche les points de sorties de l'api. Comprend uniquement les urls documentées avec de la docstring swagger
    """
    return render_template('endpoints.html')

@main_bp.route("/specs", methods=['GET']) 
def spec():
    """
    Retourne un JSON comportant toutes les informations contenues dans les docstring des fonctions
    ---
    tags:
      - API
    response:
      200:
        description: objet JSON comportant toutes les informations nécessaire à l'affichage des points de sortie de l'API
    """
    swag = swagger(app)
    swag['info']['version'] = "0.1"
    swag['info']['title'] = "Animanga"
    return jsonify(swag)

# J'ai été obliger de mettre la route en GET, car ce n'est pas possible de streamer des infos si elles viennent d'un post
# Lors de l'affichage des specs - '/enpoints' - j'ai remplacer le type de methode de GET à PUT pour une meilleur comprehention de l'api
# La fonction stream_with_context() permet de garder le contexte de la requete qui se fait supprimer en tant normale. Indispensable lors de stream avec template contenant un layout
@main_bp.route('/override')
def override_datas():
    """
    Écrase les données existantes de la bd avec de nouvelles données
    ---
    tags:
      - animes
    responses:
      200:
        description: Remplacement effecuté et redirection sur l'index
    """
    current_directory = '/'.join(__file__.split('/')[:-1])
    return Response(stream_with_context(stream_template('index.html',
                                                         override_messages=AnimeController().override_local_with_json(current_directory + '/static/json/anime.json'))))