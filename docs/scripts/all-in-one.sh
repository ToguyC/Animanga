#!/bin/bash

# Fichier final
final=../compiled/final.md

# Écrase le fichier
echo "" > $final

# Parcour tout les fichiers md souhaité dans un certain ordre
for f in ../index.md \
         ../resume-enonce.md \
         ../methodologie.md \
         ../user-stories.md \
do
    # Si le fichier courant est l'index, écraser tout le fichier pour éviter d'avoir une ligne vide au début
    if [ $f == '../index' ] ; then
        cat $f > $final
    # Sinon ajouter le contenu de chaque fichier à la fin
    else
        echo "" >> $final
        cat $f >> $final
    fi
done

# Éxecuter le script python pour générer la table des matières
exec python3 toc.py