"""Contient les routes de l'application

@author: Tanguy Cavagna
@copyright: Copyright 2020, TPI
@version: 1.0.0
@date: 2020-05-26
"""
from flask import render_template, Response, stream_with_context, jsonify, request, Blueprint, redirect, url_for
from flask import current_app as app
from flask_swagger import swagger
from flask_login import current_user, login_required

from .packages.controllers.AnimeController import AnimeController
from .packages.controllers.ListController import ListController
from .packages.controllers.UserController import UserController

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
        anime['is_favorite'] = AnimeController().is_anime_in_user_favorite(current_user.id, anime['id'])
        anime['in_list'] = [l['id'] for l in ListController().get_list_of_an_anime(anime['id'])]

    return render_template('index.html',
                            current_user=current_user,
                            search_string=search_string,
                            search_results=searched_animes,
                            user_list=ListController().get_user_lists(current_user.id))

@main_bp.route('/profile/<string:nickname>', methods=['GET'])
@login_required
def profile(nickname: str = None):
    """Affiche la page de profile de l'utilisateur mentionner dans l'url
    """
    if nickname is None:
        nickname = current_user.nickname

    searched_user = UserController().get_by_nickname(nickname)

    if searched_user is not None:
        return render_template('profile.html',
                                searched_user=searched_user,
                                stats=UserController().get_stats_by_id(searched_user.id))
    
    return redirect(url_for('main_bp.home'))

@main_bp.route('/profile', methods=['GET'])
@main_bp.route('/profile/', methods=['GET'])
@login_required
def profile_redirect():
    """Redirige l'utilisateur sur sa page de profile si aucun pseudo indiqué dans l'url
    """
    return redirect(url_for('main_bp.profile', nickname=current_user.nickname))

@main_bp.route('/lists/<string:nickname>')
@login_required
def lists(nickname: str = None):
    """Affiche toutes les liste et leur contenu de l'utilisateur mentionné dans l'url
    """
    if nickname is None:
        nickname = current_user.nickname

    searched_user = UserController().get_by_nickname(nickname)

    if searched_user is not None:
        user_lists = ListController().get_user_lists(searched_user.id)
        return render_template('lists.html',
                                current_user=current_user,
                                user_lists=user_lists,
                                searched_user=searched_user)

    return redirect(url_for('main_bp.home'))

@main_bp.route('/lists')
@main_bp.route('/lists/')
@login_required
def lists_redirect():
    """Redirige l'utilisateur si aucuns pseudo n'est inscrit dans l'url
    """
    return redirect(url_for('main_bp.lists', nickname=current_user.nickname))

@main_bp.route('/favorites/<string:nickname>')
@login_required
def favorites(nickname: str = None):
    """Affiche tout les favoris de l'utilisateur mentionné dans l'url
    """
    if nickname is None:
        nickname = current_user.nickname

    searched_user = UserController().get_by_nickname(nickname)

    if searched_user is not None:
        user_lists = ListController().get_user_lists(searched_user.id)
        return render_template('favorites.html',
                                current_user=current_user,
                                searched_user=searched_user)

    return redirect(url_for('main_bp.home'))

@main_bp.route('/favorites')
@main_bp.route('/favorites/')
@login_required
def favorites_redirect():
    """Redirige l'utilisateur si aucuns pseudo n'est inscrit dans l'url
    """
    return redirect(url_for('main_bp.favorites', nickname=current_user.nickname))

@main_bp.route('/get/favorites', methods=['GET'])
@login_required
def get_favorites_for_loged_user():
    """Récupère tous les favoris de l'utilisateur connecté
    """
    return jsonify({'animes': AnimeController().get_favorite_by_user_id(current_user.id)})

@main_bp.route('/get/favorites/<string:nickname>', methods=['GET'])
@login_required
def get_favorites_for_user(nickname = None):
    """Récupère tous les favoris d'un 'utilisateur
    """
    searched_user = UserController().get_by_nickname(nickname)
    if searched_user is not None:
        user_id = searched_user.id
        return jsonify({'animes': AnimeController().get_favorite_by_user_id(user_id)})

    return jsonify({'animes': []})

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
@login_required
def set_favorite():
    """
    Met à jour le statut de favoris d'un anime pour un utilisateur connecté
    """
    anime_id = request.get_json()['idAnime']

    if anime_id is not None:
        return jsonify({'Status': AnimeController().set_anime_in_user_favorite(current_user.id, anime_id)})
    
    return jsonify({'Status': False})

@main_bp.route('/set/list', methods=['PUT'])
@login_required
def set_list():
    """Met à jour l'association d'un anime avec une liste
    """
    id_anime = request.get_json()['idAnime']
    id_list = request.get_json()['idList']

    if id_anime is not None:
        return jsonify({'Status': AnimeController().set_anime_in_list(id_anime, id_list)})

    return jsonify({'Status': False})

@main_bp.route('/delete/defaults', methods=['DELETE'])
@login_required
def delete_status():
    """Supprime l'anime des listes par défaut de l'utilisateur connecté
    """
    anime_id = request.get_json()['idAnime']

    if anime_id is not None:
        return jsonify({'Status': AnimeController().delete_anime_status(current_user.id, anime_id)})
    
    return jsonify({'Status': False})

@main_bp.route('/get/animes', methods=['POST'])
@login_required
def get_animes_from_list():
    """Récupère les animes d'une liste
    """
    if request.json.get('nicknameUser') is not None and request.json.get('nicknameUser') != current_user.nickname:
        user_id = UserController().get_by_nickname(request.json.get('nicknameUser')).id
    else:
        user_id = current_user.id

    return jsonify({ 'animes': AnimeController().get_animes_in_list_for_user(user_id, request.json.get('idList'), request.json.get('search-terms')) })

@main_bp.route('/add/list', methods=['PUT'])
@login_required
def add_list():
    """Ajoute une nouvelle liste à l'utilisateur connecté
    """
    return jsonify({ 'list': ListController().add_new_list(request.json.get('newListName'), current_user.id) })

@main_bp.route('/delete/list', methods=['DELETE'])
@login_required
def delete_list():
    """Supprime une liste à l'utilisateur connecté
    """
    return jsonify({ 'Status': ListController().delete_by_id(request.json.get('idList'), current_user.id) })

@main_bp.route('/set/list/name', methods=['PATCH'])
@login_required
def rename_list():
    """Renomme une liste
    """
    list_id = request.get_json()['idList']
    new_list_name = request.get_json()['newListName']

    return jsonify({'Status': ListController().rename(list_id, new_list_name)})

@main_bp.route('/set/favorites-order', methods=['PATCH'])
@login_required
def set_favorites_order():
    """Met à jour l'ordre des favoris
    """
    return jsonify({ 'Status': AnimeController().reorder_favorites(current_user.id, request.json.get('ids')) })
