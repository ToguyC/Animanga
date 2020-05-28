"""Contient tout les loggers

@author: Tanguy Cavagna
@copyright: Copyright 2020, TPI
@version: 1.0
@date: 2020-05-26
"""
import os

def log(e, in_terminal: bool = True, in_file: bool = True) -> None:
    """Log les erreurs

        Arguments:
            in_terminal {bool} -- Ajoute le log dans le temrinal
            in_file {bool} -- Aout le log dans un fichier
    """
    try:
        assert in_terminal or in_file, 'Au moins `in_terminal` ou `in_file` doit être à `True`'
        assert e is not None, 'L\'exception donnée n\'est pas valide'

        if in_terminal:
            print(str(e))
        
        if in_file:
            log_file_path = os.path.dirname(os.path.realpath(__file__)) + '/log.txt'

            append_write = 'a+' if os.path.exists(log_file_path) else 'w+'

            with open(log_file_path, append_write) as log_file:
                log_file.write(str(e) + '\n')
                log_file.close()
    except AssertionError:
        raise 
