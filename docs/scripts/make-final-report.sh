#!/bin/sh

# Fusionne la page de garde avec le contenu du document final
pdftk ../compiled/cover.pdf \
         ../compiled/final.pdf \
         ../compiled/annexes-cover.pdf \
         ../compiled/resume-cover.pdf \
         ../compiled/enonce-cover.pdf \
         ../compiled/"Enoncé TPI CAVAGNA Tanguy  I.DA-P4B v2.pdf" \
         ../compiled/journal-de-bord-cover.pdf \
         ../compiled/journal-de-bord.pdf \
         ../compiled/code-source-cover.pdf \
         cat output \
         ../compiled/rapport-tpi-et-documentation-technique.pdf