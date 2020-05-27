"""Contient tout les validateurs de champs de formulaire

@author: Tanguy Cavagna
@copyright: Copyright 2020, TPI
@version: 1.0.0
@date: 2020-05-27
"""
import re

class ValidationError(ValueError):
    """Levée lorsqu'un validateur ne valide pas une entrée utilisateur
    """
    
    def __init__(self, message=''):
        super().__init__(message)

class StopValidation(Exception):
    """Arrête la validation du champ si cette exception est levée
    """

    def __init__(self, message=''):
        super().__init__(message) 

class Length(object):
    """Vérifie la longueur d'un string
    """

    def __init__(self, min: int = -1, max: int = -1, message=None):
        """
            Arguments:
                min {int} -- Longueur minium. Si pas donné, la longueur min ne sera pas testée
                max {int} -- Longueur maximum. Si pas donné, la longueur max ne sera pas testée
                message {str} -- Message d'erreur en cas d'erreur de validation.
        """
        assert min != -1 or max != -1, 'Au moins `min` ou `max` doit être spécifié'
        assert max == -1 or min <= max, '`min` ne doit pas être plus grand que `max`'
        self.min = min
        self.max = max
        self.message = message

    def __call__(self, form: dict, field_name: str):
        """Exécute la validation

            Arguments:
                form {dict} -- Dictionnaire fournit par `request.form` de flask
                field_name {str} -- Nom du champ à tester
        """
        length = len(form.get(field_name))

        # Si la longueur de la string dépasse les limites
        if length < self.min or (self.max != -1 and length > self.max):
            if self.message is None:
                if self.max == -1: # Seulement une limite minimum est présent
                    self.message = f'Le champ doit au moins avoir {self.min} caractères.'
                elif self.min == -1: # Seulement une limite maximum est présent
                    self.message = f'Le champ ne peut pas excedé {self.max} caractères.'
                else:
                    self.message = f'Le champ doit être compris entre {self.min} et {self.max} caractères'
            
            raise ValidationError(self.message)

class Required(object):
    """Vérifie la présence d'un champ
    """

    def __init__(self, message=None):
        """
            Arguments:
                message {str} -- Message d'erreur en cas d'erreur de validation.
        """
        self.message = message

    def __call__(self, form: dict, field_name: str):
        """Exécute la validation

            Arguments:
                form {dict} -- Dictionnaire fournit par `request.form` de flask
                field_name {str} -- Nom du champ à tester
        """
        if len(form.get(field_name)) == 0:
            if self.message is None:
                self.message = 'Ce champ est obligatoire'

            raise StopValidation(self.message)

class Regex(object):
    """Vérifie si le regex donné correspond au champ
    """

    def __init__(self, regex: str, message=None):
        """
            Arguments:
                regex {str} -- Expression régulière à tester
                message {str} -- Message d'erreur en cas d'erreur de validation.
        """
        self.regex = regex
        self.message = message

    def __call__(self, form: dict, field_name: str):
        """Exécute la validation

            Arguments:
                form {dict} -- Dictionnaire fournit par `request.form` de flask
                field_name {str} -- Nom du champ à tester
        """
        if not re.search(self.regex, form.get(field_name)):
            if self.message is None:
                self.message = 'Champ invalide'

            raise ValidationError(self.message)

class Email(Regex):
    """Valide un email grâce à un regex
    """

    def __init__(self, message=None):
        super(Email, self).__init__(r'^[a-zA-z0-9._-]+@[^\.]+\..+$', message)

    def __call__(self, form: dict, field_name: str):
        """Exécute la validation

            Arguments:
                form {dict} -- Dictionnaire fournit par `request.form` de flask
                field_name {str} -- Nom du champ à tester
        """
        if self.message is None:
            self.message = 'Adresse email invalide'
        
        super(Email, self).__call__(form, field_name)

class EqualTo(object):
    """Valide si un champ est égale à un autre
    """
    
    def __init__(self, field_name_to_equal: str, message=None):
        """
            Arguments:
                field_name_to_equal {str} -- Nom du champ sur lequel le champs testé doit être égale
                message {str} -- Message d'erreur en cas d'erreur de validation.
        """
        self.field_name_to_equal = field_name_to_equal
        self.message = message

    def __call__(self, form: dict, field_name: str):
        """Exécute la validation

            Arguments:
                form {dict} -- Dictionnaire fournit par `request.form` de flask
                field_name {str} -- Nom du champ à tester
        """
        try:
            field_to_equal = form.get(self.field_name_to_equal)
            
            if field_to_equal is None:
                raise KeyError
        except KeyError:
            raise ValidationError(f'Nom de champs à égalé incorrect `{self.field_name_to_equal}`')

        if form.get(field_name) != field_to_equal:
            if self.message is None:
                self.message = f'Le champ doit être égale à {self.field_name_to_equal}'
            
            raise ValidationError(self.message)