Title:A la découverte de netcat
Date: 2015-10-22 11:03
Tags:Dev, Dev web, netcat
Category:Admin Sys
Summary:
Subtitle:
Status: draft

Aujourd'hui faisons la découverte du merveilleux outils `netcat` ou le *couteau suisse du développement web*.

Cet application est très pratique quand on fait de la programmation réseau, pour déboguer, mais aussi pour les admins sys.

Par exemple, a chaque fois que j'ai fait de la prog réseau, tout était fragile : un socket qui n'écoute qu'en local, un parefeu capricieux, une interface réseau qui fait n'importe quoi et plus rien ne marche sans savoir d'où ça peut venir. Et le débug n'est pas évident en réseau, c'est là que l'on est content d'avoir `netcat`.

## Installation

`netcat` n'est pas installé par défaut sur certains linux. Il existe 2 versions, qui malheureusement n'acceptent pas les même options : `netcat-openbsd` et `netcat-traditional`.

Vous pouvez savoir lequel est installé en faisant
```sh
netcat
```

Et la réponse devrait être quelque chose du genre (ubuntu 14.04):
```sh
This is nc from the netcat-openbsd package. An alternative nc is available
in the netcat-traditional package.
usage: nc [-46bCDdhjklnrStUuvZz] [-I length] [-i interval] [-O length]
    [-P proxy_username] [-p source_port] [-q seconds] [-s source]
    [-T toskeyword] [-V rtable] [-w timeout] [-X proxy_protocol]
    [-x proxy_address[:port]] [destination] [port]
```
Dans ce cas, on a... la version openbsd.

Pour passer d'une version à une autre, il suffit de faire :
```sh
apt-get remove netcat-traditional
apt-get install netcat-openbsd
```

Dans ce tutoriel, nous utiliserons `netcat-openbsd`.

### Et pour windows ?

Il existe une version windows, je vous laisse la trouver :p

## Utilisation basique

On va faire un petit tchat en ligne de commandes. En 2 lignes. La classe quoi.

En réseau il s'agit souvent d'une communication entre en serveur et un client. Comme au restaurant, le serveur écoute le client qui lui demande des choses et un serveur peu servir plusieurs clients (mais en se concentrant sur un seul à la fois).

Par défaut `netcat` effectue ses connexions en TCP, mais il est possible de les passer en UDP en rajoutant l'option `-u`.

### Serveur

```sh
netcat -l 9876
```

Crée un serveur (l'option `-l`) qui écoute sur le port 9876

### Client

```sh
netcat localhost 9876
```

Crée un client qui se connecte à `localhost` sur le port 9876.


### Tchat

Pour faire un tchat, il suffit d'ouvrir 2 terminaux, de créer un serveur et un client. Les commandes ne devraient pas rendre la main et vous pouvez taper du texte, appuyer sur entrée et le voir s'afficher sur l'autre terminal.

Pour terminer, appuyez sur `Ctrl-C`, fermer le client ou le serveur va déconnecter l'autre automatiquement.

N'oubliez pas, il faut lancer le serveur en premier puis créer un client.

Essayez maintenant de lancer un autre client, il ne peut pas se connecter. `netcat` ne permet pas d'avoir de connections concurrentes, si vous en avez besoin, il faut utiliser d'autres outils.

### Remarque

Vu que les communications passent par TCP ou UDP, on n'est pas obligé d'utiliser netcat de chaque côté, il suffit d'utiliser une connexion socket.

Vous pouvez donc déboguer vos codes Python ou C ou n'importe quoi avec des sockets en utilisant le tchat. C'est très pratique pour savoir s'il y a des problèmes au niveau de caractères (rajoutés ou supprimés) ou bien si des connexions se ferment alors qu'elles ne devraient pas.

### Application : savoir si vous êtes bloqués par un parefeu

On peut utiliser ce tchat pour savoir si un parefeu vous bloque ou s'il y a un problème quelconque au niveau de la connexion. Pour rappel, les pare-feu peuvent être sortant ou entrant, et un port qui laisse passer dans un sens et pas dans l'autre peut être assez long à déboguer.

Voilà comment faire :

 * vous avez un ordinateur accessible par une IP sur internet, on va l'appeler S et un ordinateur qui veux y accéder, que l'on va appeler A.
 * vous pingez S depuis A. Si ça ne marche pas il y a un problème de connexion.
 * vous lancez un serveur `netcat` sur S sur le port d'intérêt.
 * vous lancez un client sur A vers l'IP de S avec le bon port. Si le client n'arrive pas à se connecter c'est que le port est bloqué en entré, sinon c'est bon
 * vous essayez d'écrire depuis S sur A si ça marche, il n'y a pas de pare-feu sortant.

Bon après, on peut faire un nmap aussi, mais je ne me souviens jamais de la ligne de commande à faire...


## Utilisation plus avancée

Tester des pare-feu, c'est sympa, mais on peu faire plus.

### Débug de serveur web

Si vous utilisez un serveur web avec un proxy inverse ou des réécritures d'URL, vous pouvez avoir envie de tester s'il est réglé correctement, au niveau des URL ou des header HTTP par exemple.

Il suffit de faire un serveur en netcat et de se connecter sur l'URL ou le port avec un navigateur pour voir les header HTTP.

Voilà un exemple avec firefox sur un Ubuntu (connexion sur localhost:8855) :
```config
➭ nc -l 8855
GET / HTTP/1.1
Host: localhost:8855
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: keep-alive
```

Exemple d'une connexion sur localhost:8855/une-autre-URL
```config
➭ nc -l 8855
GET /une-autre-URL HTTP/1.1
Host: localhost:8855
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: keep-alive
```

Comme `netcat` se ferme à chaque connexion, on peut utiliser la commande suivante pour la rouvrir automatiquement :

```sh
while true ; do nc -l PORT ; done
```

### Partager des fichiers

`netcat` permettant d'ouvrir des communications réseau et de faire passer du texte, on peut aussi faire passer des fichiers d'un ordinateur à un autre :

 * sur le serveur :
```
cat backup.iso | nc -l 3333
```

* sur le client :
```
nc IP_SERVEUR 3333 > backup.iso
```

Le seul problème c'est que l'on ne peut pas savoir où en est le téléchargement. Dans ce cas, on peut faire :

* sur le serveur :

```
pv backup.iso | nc -l 3333
```

* sur le client :
```
nc IP_SERVEUR 3333 |pv > backup.iso
```

Avec [pv](http://linux.die.net/man/1/pv) qui est l'utilitaire `pipe view` (à installer) qui permet d'afficher des barres de progressions.

### SSH hopping

Imaginons le cas suivant pour une connexion SSH :

 * vous avez un serveur publique : _GW_, accessible par internet, qui sert de porte d'entrée sur votre réseau privé, un Gateway
 * vous avez un serveur sur un réseau privé : _SPr_, qui ne sont pas accessible par internet, mais _GW_ peut y accéder

Si vous voulez vous connecter à _SPr_ par `ssh`, vous devez faire une connexion à _GW_ puis une autre à _SPr_. C'est long et ça peut amener à faire des erreurs. Il faudrait une façon automatique de sauter de _GW_ à _Spr_, de faire un 'hop' entre les deux (d'où le nom de la technique)  .

Dans ce cas, vous pouvez utiliser `netcat` dans votre `~/.ssh/config` :

```yaml
Host GW
  HostName GW.example.com

Host SPr
  ProxyCommand ssh -q GW nc -q0 SPr 22

```

Le `proxycommand` signifie que `ssh SPr` va en fait exécuter `ssh -q GW nc -q0 SPr 22`. Donc execute une connexion `ssh` classique sur _GW_ puis une fois connecté, fait un `nc` sur le port 22 du _SPr_. Comme le port 22 est le port classique pour `ssh`, tout ce qui passe dans le premier `ssh` sera transmit à la 2ème machine.

## Bonus

### Un outil de supervision

Vous utilisez `Munin` ou un truc dans le genre pour savoir les ressources utilisées par vos serveurs ou les processus qui tournent ? Laissez tomber et utilisez netcat !

On peut afficher le résultat d'un `top` dans une page web :

```sh

(
  trap "exit" INT ;
  while true;
    do
      top -b  -n1 | nc -l 8855 ;
  done
)
```

`top -b  -n1` permet d'avoir une sortie récupérable (et non pas interactive) pour `top`.

Le `trap "exit" INT` permet de quitter le programme, sinon il ignore les interruptions avec `Ctrl-C`.


### NGINX c'est surfait, utilisons nc :)

On peut servir une page statique avec `netcat` pour remplacer vite fait un serveur web en rade. Bon, ça sert juste du HTML, sans autres ressources et ça sert la même chose sur toutes les URL mais ça dépanne :

On peut tester quelque chose comme ça :

```sh
while true ;
  do nc -l 80 < index.html ;
done
```

Cependant, le navigateur affiche le texte sans faire le rendu HTML. `netcat` ne respectant pas HTTP de base, il faut rajouter un header HTTP minimum : `"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"`

```sh
(
  trap "exit" INT ;
  while true;
    do
    {
      echo "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n" ;
      cat index.html
    } | nc -l 8855 ;
  done
)

```

## Pour aller plus loin :

 * vous pouvez installer `netcat-traditional` et jouer avec les options `-e` et `-c`
 * on peut utiliser netcat comme scanner de ports
 * on peut crypter les communications en passant la connexion dans un SSH ou en utilisant d'autres outils
 * Avec des FIFO, on peut faire un "man-in-the-middle" pour avoir tous les logs navigateur et serveur dans un fichier tout en continuant à servir le site normalements
 * allez, faites un skype du pauvre avec netcat !


## Sources

 * [Lien SO expliquant comment passer d'une version traditionelle à une version bsd.](http://stackoverflow.com/questions/12266898/start-netcat-server)
 * [Lien askubuntu sur le ssh hopping](http://askubuntu.com/questions/311447/how-do-i-ssh-to-machine-a-via-b-in-one-command)
 * [Plus d'infos sur le multi hop](http://sshmenu.sourceforge.net/articles/transparent-mulithop.html)
 * [Quelques utilisations de netcat, j'en ai repris la plupart](http://www.g-loaded.eu/2006/11/06/netcat-a-couple-of-useful-examples/)
 * [Capture de top](http://www.thegeekstuff.com/2009/10/how-to-capture-unix-top-command-output-to-a-file-in-readable-format/)
 * [Inspiration pour le serveur web en nc](http://www.commandlinefu.com/commands/view/9164/one-command-line-web-server-on-port-80-using-nc-netcat)
 * [Cool stuff to do with netcat sur HN](https://news.ycombinator.com/item?id=1873386)
 * [Inspiration pour le serveur web qui fonctionne, proxy TCP](http://www.stearns.org/doc/nc-intro.current.html)

J'espère avoir pu vous faire partager la puissance de cet outil. Il ne vous reste plus qu'à utiliser `nc` pour vos débugs réseau et autres geekeries ;)

Si vous avez d'autres techniques, n'hésitez pas à les partager en commentaire.