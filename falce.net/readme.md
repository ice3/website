# Page d'acceuil du site

## Role

* Permet de dispatcher sur les différents sous sites
* Permet de dispatcher vers les différents dossiers présents dans falce.net

## Technique

Entièrement écrit à la main en HTML

Stack bower pour minifier les CSS => quand on rajoute une classe CSS d'une lib, il faut recompiler les CSS minifier.

Installation gulp :

```
sudo add-apt-repository ppa:chris-lea/node.js
sudo apt-get update
sudo apt-get install nodejs
npm install gulp gulp-uncss gulp-cssmin gulp-rename es6-promise gulp-debug## dans le bon répertoire
```

Utilisation `gulp` (va utiliser le gulpfile.js)