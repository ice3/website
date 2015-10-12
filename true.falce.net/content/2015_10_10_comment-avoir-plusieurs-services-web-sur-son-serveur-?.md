Title:Comment avoir plusieurs services web sur son serveur ?
Date: 2015-10-12 21:34
Tags:NGINX, Apache, serveur web, proxy, dev web
Category: Admin Sys
Summary:Comme ne le chantait pas Pierre Perret "Tout tout tout, vous saurez tout sur les reverse proxy"
Subtitle:En utilisant un "reverse proxy" pardi
Status: published

C'est le genre de questions bêtes que l'on se pose quand on débute. Les tutoriels parlent de configuration de serveurs et on ne comprend pas l'intérêt réel.

La philosophie de l'article est plus de découvrir le principe que de fournir une solution clef en main :)

## Le problème

J'ai un serveur web (un ordinateur), sur lequel tourne un serveur web (un logiciel, NGINX) qui sert mon site web, sur le port 80 donc.

Maintenant imaginons que je veuille développer une application web, en Python/Flask par exemple. L'application va écouter sur un certain port, disons `12345`. Je peux y accéder en faisant `http://monip:12345`.

Bon jusque là rien de nouveau sous le soleil. Mais ce n'est pas très sérieux :

 * ça fait peut aux gens d'accéder à un port précis, ils n'ont pas l'habitude et ne se connecterons pas
 * c'est plus simple de se souvenir d'un nom que d'un chiffre aléatoire

Une meilleure solution c'est d'accéder à `http://monip/monapp` ou `http://monapp.monip` plutôt que sur un port. Sauf que le serveur web est déjà attaché au port 80 et qu'un seul processus peut se connecter sur un port.


## La solution

### Pré-requis

Je pars du principe que vous utilisez un Linux et avez [installé un serveur web](https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-14-04-lts) (NGINX ou Apache) qui fonctionne. Même si vous n'avez encore rien configuré parce que vous ne pigez rien aux tutos. Les examples se baseront sur NGINX.

### [Un proxy inverse](https://fr.wikipedia.org/wiki/Proxy_inverse)

{% img images/reverse_proxy.svg Schema expliquant le fonctionnement d'un reverse proxy (source: wikipedia) %}

Nous allons utiliser un reverse proxy géré par votre serveur web.

Mais c'est quoi donc ?

C'est simple, le proxy va recevoir toutes les requêtes (les URL tapées par les visiteurs) et va les transmettre à un serveur web selon certaines règles.

Pour comprendre les exemples, il faut partir du principe que les connexions reçues par le proxy ne contiennent plus le nom de domaine. C'est à dire, pour NGINX `www.monsite.com/maPage` sera vu comme `/maPage`.

Voilà un exemple pour NGINX. Il faut rajouter ces directives dans un fichier de configuration dans `/etc/nginx/site-available/`, dans un bloc `server` :
```
location / {
    proxy_pass http://localhost:12345/;
}
```
 Ainsi, toutes les requêtes commençant par `/` (c'est à dire toutes) seront renvoyées au port `12345` (ce qui est intéressant si vous utilisez des sous domaines par exemple).


Dans le cas où vous voulez transférer les connexions sur `/monapp` vers le port `12345`, vous devrez avoir une règle dans le genre :

```
location /monapp/ {
    proxy_pass  http://127.0.0.1:12345/;
}
```

Dans ce cas, une URL vers `monip/monapp/page1` sera transmise vers `127.0.01:12345/page1` (avec 127.0.0.1, le localhost du serveur).

Attention, n'oubliez pas le `/` final, il permet d'éliminer le `/monapp` de l'URL. Grâce à lui votre application écoutant sur le port `12345` pourra analyser ses URL à partir de la racine comme si rien ne s'était passé.

### Les variables spéciales

Comme on le voit sur le schéma, le proxy est situé sur votre réseau et va transmettre les requêtes, ce qui modifier les headers HTTP. Du coup, vous ne pouvez plus savoir quelle est l'IP de votre visiteur par exemple, vu qu'elle sera remplacée par celle indiquée dans le `proxy_pass` (le plus souvent 127.0.0.1).

Dans ce cas, vous pouvez rajouter des variables qui permettent de remodifier le header.

```
location /monapp/ {
    ...
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    ...
}
```

## Conclusion

L'exemple complet :

```
location /monapp/ {
    proxy_pass  http://127.0.0.1:12345/;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
}
```

Finalement, il est assez aisé de faire fonctionner plusieurs services web sur son serveur en utilisant NGINX. De plus, la configuration est assez aisé, 10 lignes à rajouter dans un fichier au maximum.

Il ne faut donc pas se laisser dépasser par la complexité relative de NGINX, ou d'un serveur web en général (il y a des centaines de directives et de variables).

Il faut juste y aller petit à petit et se concentrer sur une configuration à la fois.

## Pour aller plus loin

 * [nous pouvons servir des contenus statiques avec `location`](https://www.nginx.com/resources/admin-guide/serving-static-content/)
 * [un tutoriel pour débutants (en anglais)](http://nginx.org/en/docs/beginners_guide.html#proxy)
 * [pour en savoir plus sur les variables du `proxy_set_header`](http://nginx.org/en/docs/http/ngx_http_proxy_module.html#proxy_set_header)