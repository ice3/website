# Pour installer

  pip install requirement.txt

#Pour compiler

On utilise le makefile.

  make devserver

La commande regarde les modifications sur les fichiers et regénère à la volée et lance un serveur web en arrière plan.

#Pour installer des thèmes

Il faut copier quelque part le thème. Pour qu'un thème soit utilisable, il faut l'installer.
Pour cela, il faut utiliser la commande `pelican-themes -i LE_DOSSIER_DU_THEME`.
On peut lister les thèmes installés avec `pelican-themes -l`
Pour l'utiliser, on met juste le nom du thème installé dans la variable `THEME` de `pelicanconf.py`.
