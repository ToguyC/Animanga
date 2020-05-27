"""Contient les routes d'authentifiation de l'application

@author: Tanguy Cavagna
@copyright: Copyright 2020, TPI
@version: 1.0.0
@date: 2020-05-27
"""
import hashlib
import re
from typing import Any

from flask import redirect, render_template, flash, Blueprint, request, url_for
from flask_login import login_required, current_user, login_user, logout_user

from .packages.controllers.UserController import UserController

# Configuration du Blueprint
auth_bp = Blueprint('auth_bp', __name__,
                    template_folder='templates',
                    static_folder='static')

# ================
#    Utilities
# ================
def validate_signup_inputs(form: dict) -> Any:
    """Valide les différents inputs du formulaire d'inscription

        Arguments:
            form {dict} -- Dictionnaire contenant les valeurs des inputs du formulaire

        Returns:
            bool -- Est-ce que tout les inputs sont valide
            [] -- Liste des erreurs
    """
    errors = {}
    email_errors = { 'errors': [] }
    nickname_errors = { 'errors': [] }
    password_errors = { 'errors': [] }
    confirm_errors = { 'errors': [] }

    # Email
    if form.get('email') == '':
        email_errors['errors'].append('Ce champ est obligatoire')
    else:
        if len(form.get('email')) < 6:
            email_errors['errors'].append('Choisissez un email plus long')
        if not re.search('^[a-zA-z0-9._-]+@[^\.]+\..+$', form.get('email')):
            email_errors['errors'].append('Entrez un email valide')

    # Pseudo
    if form.get('nickname') == '':
        nickname_errors['errors'].append('Ce champ est obligatoire')

    # Mot de passe
    if form.get('password') == '':
        password_errors['errors'].append('Ce champ est obligatoire')
    else:
        if len(form.get('email')) < 6:
            password_errors['errors'].append('Choisissez un mot de passe plus long')

    if form.get('confirm') == '':
        confirm_errors['errors'].append('Ce champ est obligatoire')
    else:
        if form.get('confirm') != form.get('password'):
            confirm_errors['errors'].append('Les mots de passes doivent correspondre')

    # Ajout des erreur dans la réponse
    if len(email_errors['errors']) > 0: errors['email'] = email_errors
    if len(nickname_errors['errors']) > 0: errors['nickname'] = nickname_errors
    if len(password_errors['errors']) > 0: errors['password'] = password_errors
    if len(confirm_errors['errors']) > 0: errors['confirm'] = confirm_errors

    return True if len(errors.keys()) == 0 else errors

def validate_login_inputs(form: dict) -> Any:
    """Valide les différents inputs du formulaire de connexion

        Arguments:
            form {dict} -- Dictionnaire contenant les valeurs des inputs du formulaire

        Returns:
            bool -- Est-ce que tout les inputs sont valide
            [] -- Liste des erreurs
    """
    errors = {}
    email_errors = { 'errors': [] }
    password_errors = { 'errors': [] }

    # Email
    if form.get('email') == '':
        email_errors['errors'].append('Ce champ est obligatoire')
    else:
        if len(form.get('email')) < 6:
            email_errors['errors'].append('Choisissez un email plus long')
        if not re.search('^[a-zA-z0-9._-]+@[^\.]+\..+$', form.get('email')):
            email_errors['errors'].append('Entrez un email valide')

    # Mot de passe
    if form.get('password') == '':
        password_errors['errors'].append('Ce champ est obligatoire')

    # Ajout des erreur dans la réponse
    if len(email_errors['errors']) > 0: errors['email'] = email_errors
    if len(password_errors['errors']) > 0: errors['password'] = password_errors

    return True if len(errors.keys()) == 0 else errors

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    """Affiche la page d'inscription
        \nGET: Affiche la page
        \nPOST: Si les informations de connexion sont valides, redirection sur l'accueil
    """
    validation = {}
    if request.method == 'POST':
        validation = validate_signup_inputs(request.form)

        if validation == True:
            email = request.form.get('email')
            nickname = request.form.get('nickname')
            password = request.form.get('password')

            if not UserController().exists(email):
                hashed_password = hashlib.sha256(password.encode('utf8')).hexdigest()
                user = UserController().insert(email, nickname, hashed_password)

                if user is not None:
                    login_user(user)
                    return redirect(url_for('main_bp.home'))
            
            flash('Un utilisateur utilise déjà cet email')
            return redirect(url_for('auth_bp.signup'))

    return render_template('signup.html',
                            current_user=current_user,
                            validation=validation)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """Affiche la page de connexion
        \nGET: Affiche la page
        \nPOST: Si les informations de connexion sont valides, redirection sur l'accueil
    """
    validation = {}
    if request.method == 'POST':
        validation = validate_login_inputs(request.form)

        if validation == True:
            email = request.form.get('email')
            password = request.form.get('password')
            hashed_password = hashlib.sha256(password.encode('utf8')).hexdigest()

            if UserController().check_password(email, hashed_password):
                user = UserController().get_by_email(email)
                login_user(user)
                return redirect(url_for('main_bp.home'))

            flash('Combinaison email - mot de passe invalide')
            return redirect(url_for('auth_bp.login'))

    return render_template('login.html',
                            current_user=current_user,
                            validation=validation)

@auth_bp.route('/logout', methods=['GET'])
@login_required
def logout():
    """Déconnecte l'utilisateur"""
    logout_user()
    return redirect(url_for('auth_bp.login'))
