"""Contient la classe permettant de gérer les champs d'un formulaire

@author: Tanguy Cavagna
@copyright: Copyright 2020, TPI
@version: 1.0.0
@date: 2020-05-27
"""
class Form(object):
    """Contient le comportement des forumlaire comme la validations
       des champs et la récupération d'erreurs
    """

    def __init__(self, form: dict, fields: list):
        """
            Arguments:
                fields {dict} -- Dictionnaire contenant les champs
        """
        self._errors = None
        self._fields = fields
        self._form = form

    @property
    def errors(self):
        if self._errors is None:
            self._errors = dict((f.name, f.errors) for f in self._fields if len(f.errors) > 0)
        return self._errors

    def validate(self):
        """Valide le formulaire en appellant `validate` sur chaque champs

            Returns:
                bool -- Aucune erreurs
        """
        self._errors = None
        success = True

        for field in self._fields:
            if not field.validate(self._form):
                success = False

        return success
