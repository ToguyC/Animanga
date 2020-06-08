"""Contient le contrôleur d'authentification

@author: Tanguy Cavagna
@copyright: Copyright 2020, TPI
@version: 1.0.0
@date: 2020-05-27
"""
import re
from typing import Any

class BaseAuthenticationControlleur:
    """Contrôleur pour l'authentification
    """

    def __init__(self, form):
        """
            Arguments:
                form {dict} -- Dictionnaire provenant de `request.form`
        """
        self.form = form
        self._auth_errors = dict()

    def update_auth_errors_dict(self, field_name: str, error_condition: bool, message: str) -> bool:
        """Met à jour le dictionnaire d'erreurs si la condition d'erreur passe

            Arguments:
                field_name {str} -- Nom du champs pour lequel la condition s'applique
                error_condition {bool} -- Condition d'erreur. Si True, alors l'erreur doit être prise en compte.
                message {str} -- Message à afficher si l'erreur est levée

            Returns:
                bool -- Est-ce que l'erreur à été levée
        """
        if error_condition:
            if field_name not in self._auth_errors.keys():
                self._auth_errors.update({ field_name: [] })

            self._auth_errors.get(field_name).append(message)

        return self._auth_errors

    def reset_auth_errors(self):
        """Supprime toutes les anciennes erreurs
        """
        self._auth_errors = dict()

    def get_state(self) -> Any:
        """Est-ce que l'authentification est validé

            Returns:
                bool -- `True` si aucune erreurs levées
                dict -- Toutes les erreurs levées
        """
        return self._auth_errors if self._auth_errors else True

    def field_empty(self, field_name: str, message: str = None) -> bool:
        """Vérifie si le champ est vide

            Arguments:
                field_name {str} -- Nom du champ à vérifier
                message {str} -- Message à afficher en cas d'erreur
        """
        error_condition = bool(self.form.get(field_name) == '')
        
        if error_condition:
            if message is None:
                message = 'Ce champ est obligatoire'
            
            return self.update_auth_errors_dict(field_name, error_condition, message)

        return None

    # pylint: disable=redefined-builtin
    def length(self, field_name: str, min: int = -1, max: int = -1, message: str = None) -> bool:
        """Vérifie si le champ respecte les longueurs imposée

            Arguments:
                field_name {str} -- Nom du champ à vérifier
                min {int} -- Valeur minimum
                max {int} -- Valeur maximum
                message {str} -- Message à afficher en cas d'erreur
        """
        length = len(self.form.get(field_name))
        error_condition = bool(length < min or (max != -1 and length > max))

        if error_condition:
            if message is None:
                if max == -1: # Seulement une limite minimum est présent
                    message = f'Le champ doit au moins avoir {min} caractères.'
                elif min == -1: # Seulement une limite maximum est présent
                    message = f'Le champ ne peut pas excéder {max} caractères.'
                else:
                    message = f'Le champ doit être compris entre {min} et {max} caractères'
            
            return self.update_auth_errors_dict(field_name, error_condition, message)

        return None

    def regex(self, field_name: str, regex: str, message: str = None) -> bool:
        """Vérifie si le champ valide le regex

            Arguments:
                field_name {str} -- Nom du champ à vérifier
                regex {str} -- Expression régulière à vérifier
                message {str} -- Message à afficher en cas d'erreur
        """
        p = re.compile(regex)
        error_condition = bool(not p.match(self.form.get(field_name)))

        if error_condition:
            if message is None:
                message = 'Champ invalide'

            return self.update_auth_errors_dict(field_name, error_condition, message)
        
        return None

    def email(self, field_name: str, message: str = None) -> bool:
        """Vérifie si le champ valide le regex

            Arguments:
                field_name {str} -- Nom du champ à vérifier
                message {str} -- Message à afficher en cas d'erreur
        """
        if message is None:
            message = 'Email invalide'
        return self.regex(field_name, r'^[a-zA-z0-9._-]+@[^\.]+\..+$', message)

    def equal_to(self, field_name: str, other_field_name: str, message: str = None) -> bool:
        """Vérifie si le champ valide le regex

            Arguments:
                field_name {str} -- Nom du champ à vérifier
                other_field_name {str} -- Nom du champ contre lequel tester l'égalité
                message {str} -- Message à afficher en cas d'erreur
        """
        try:
            field_to_equal = self.form.get(other_field_name)

            if field_to_equal is None:
                raise KeyError
        except KeyError:
            self.update_auth_errors_dict(other_field_name, True, f'Nom de champs à égalé incorrect `{other_field_name}`')

        error_condition = bool(self.form.get(field_name) != field_to_equal)

        if error_condition:
            if message is None:
                message = f'Le champ doit être égale à {other_field_name}'

            return self.update_auth_errors_dict(field_name, error_condition, message)

        return None
        
class SignupController(BaseAuthenticationControlleur):
    """Contrôleur de l'inscription
    """

    def validate(self):
        """Valide les champs du forumlaire
        """
        if not self.field_empty('email'):
            self.length('email', min=6, message='Choisissez un email plus long')
            self.email('email', 'Entrez un email valide')

        self.field_empty('nickname')

        if not self.field_empty('password'):
            self.length('password', min=6, message='Choisissez un mot de passe plus long')

        if not self.field_empty('confirm'):
            self.equal_to('confirm', 'password', 'Les mots de passes doivent correspondre')

        return not self._auth_errors

class LoginController(BaseAuthenticationControlleur):
    """Contrôleur de la connexion
    """

    def validate(self):
        """Valide les champs du forumlaire
        """
        if not self.field_empty('email'):
            self.email('email', 'Entrez un email valide')

        self.field_empty('password')
        
        return not self._auth_errors
