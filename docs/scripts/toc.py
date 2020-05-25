from subprocess import Popen, PIPE

# Execute la commande : python3 -m md_toc github ../compiled/final.md
# Cette commande sert à générer une table des matières pour un document markdown.
p = Popen(['python3', '-m', 'md_toc', 'github', '../compiled/final.md'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
# Récupère la sortie de la commande (la table des matière)
(output, err) = p.communicate()
toc = output.decode('utf-8') # Decode la sortie

# Ajoute le titre "Table des matières" juste avant la table des matières
toc = '## Table des matière\n\n' + toc + "\n<div style='page-break-after: always; break-after: page; text-align:right;'></div>"

updated_lines = []
# Ajoute la table des matière dans les lignes du fichier
with open('../compiled/final.md', 'r+') as f:
    lines = f.readlines()
    del lines[0]
    del lines[1]
    f.seek(0)
    lines.insert(0, toc)
    updated_lines = lines
    f.truncate(0) # Suppression de l'ancien contenu
    f.writelines(updated_lines) # Ajout du nouveau contenu
    f.close()