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
from .packages.controllers.ListController import ListControlleur

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
    return render_template('index.html',
                            current_user=current_user)

@main_bp.route('/search/<string:search_string>', methods=['GET'])
@login_required
def search(search_string: str = None):
    """Recherche un anime
    """
    # Parse la chaine de recherche pour tansformer la chaine comme suit (facilite la recherche fulltext) :
    # Chaine de base : Ma chaine de recherche
    # Chaine parsée : "Ma" "chaine" "de" "recherche"
    search_string_parsed = ' '.join(['"' + escaped + '"' for escaped in search_string.split(' ')])
    searched_animes = AnimeController().get_from_search_string(search_string_parsed)
    
    # Ajout des relations
    for anime in searched_animes:
        anime['relations'] = AnimeController().get_relations_by_anime_id(anime['id'])
        anime['is_favorite'] = AnimeController().is_anime_is_user_favorite(current_user.id, anime['id'])

    return render_template('index.html',
                            current_user=current_user,
                            search_string=search_string,
                            search_results=searched_animes,
                            user_list=ListControlleur().get_defaults_for_user(current_user.id))

@main_bp.route('/random', methods=['GET'])
@login_required
def random_anime():
    """Récupère une anime aléatoire dans la base
    """
    random_anime = AnimeController().get_random_anime()

    random_anime['relations'] = AnimeController().get_relations_by_anime_id(random_anime['id'])

    return jsonify({'anime': random_anime})

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

# ================
#      POST, PATCH, PUT, DELETE
# ================
@main_bp.route('/set/favorite', methods=['PATCH'])
def set_favorite():
    """
    Met à jour le statut de favoris d'un anime pour un utilisateur connecté
    """
    anime_id = request.get_json()['idAnime']

    if anime_id is not None:
        return jsonify({'Status': AnimeController().set_anime_in_user_favorite(current_user.id, anime_id)})
    
    return jsonify({'Status': False})
