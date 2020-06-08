#!/bin/bash

# Fichier final
final=../compiled/final.md

# Écrase le fichier
echo "" > $final

# Parcour tout les fichiers md souhaité dans un certain ordre
for f in ../index.md \
         ../resume-enonce.md \
         ../methodologie.md \
         ../planning.md \
         ../implementation.md \
         ../librairies.md \
         ../scenarios-tests.md \
	     ../bibliographie.md \
	     ../conclusion.md
do
    echo >> $final
    cat $f >> $final
done

# Éxecuter le script python pour générer la table des matières
exec python3 toc.py
