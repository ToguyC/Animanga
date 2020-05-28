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
from .packages.controllers.authentication import SignupController, LoginController

# Configuration du Blueprint
auth_bp = Blueprint('auth_bp', __name__,
                    template_folder='templates',
                    static_folder='static')

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    """Affiche la page d'inscription
        \nGET: Affiche la page
        \nPOST: Si les informations de connexion sont valides, redirection sur l'accueil
    """
    auth_validation = SignupController(request.form)
    
    if request.method == 'POST':
        if auth_validation.validate():
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
                            auth_errors=auth_validation.get_state())

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """Affiche la page de connexion
        \nGET: Affiche la page
        \nPOST: Si les informations de connexion sont valides, redirection sur l'accueil
    """
    auth_validation = LoginController(request.form)

    if request.method == 'POST':
        if auth_validation.validate():
            email = request.form.get('email')
            password = request.form.get('password')
            hashed_password = hashlib.sha256(password.encode('utf8')).hexdigest()

            if UserController().check_password(email, hashed_password):
                user = UserController().get_by_email(email)
                login_user(user)
                return redirect(url_for('main_bp.home'))

            flash('Combinaison email - mot de passe invalide')
            return redirect(url_for('auth_bp.login'))

    print(auth_validation)
    return render_template('login.html',
                            current_user=current_user,
                            auth_errors=auth_validation.get_state())

@auth_bp.route('/logout', methods=['GET'])
@login_required
def logout():
    """Déconnecte l'utilisateur"""
    logout_user()
    return redirect(url_for('auth_bp.login'))
