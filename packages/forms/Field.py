"""Contient la classe permettant de généré un champ pour formulaire afin de le valider par la suite

@author: Tanguy Cavagna
@copyright: Copyright 2020, TPI
@version: 1.0.0
@date: 2020-05-27
"""
from .validators import ValidationError, StopValidation

class Field(object):
    """Classe de champ de formulaire
    """
    errors = list()

    def __init__(self, name: str, validators: list) -> None:
        assert name != ''
        self.name = name
        self.validators = validators

    def validate(self, form):
        """Valide tout les champs et retourne True ou False. `self.errors`
           contiendra toutes les erreurs relevées durant la validation.
           Tout ceci est fait lors de `Form.validate`
        """
        self.errors = list()
        # Exécute les validateurs
        for validator in self.validators:
            try:
                validator(form, self.name) # Appel la fonction magic `__call__` du validateur. C'set un raccourci de validator.__call__(form, self.name)
            except StopValidation as e: # Si cette erreur est levée, stop tout le reste des validations et n'affiche que le message de cette exception
                self.errors = list()
                self.errors.append(str(e))
                break
            except ValidationError as e:
                self.errors.append(str(e))

        return len(self.errors) == 0
