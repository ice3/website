Title:La réécriture d'URL avec NGINX
Date: 2015-10-12 17:58
Tags:
Category:
Summary:
Subtitle:
Status: draft


Le problème c'est que les URLs transmises au port `12345` contiennent également `/monapp` alors que l'application n'a pas à savoir comment sont organisées nos URL.

On peut l'éliminer en faisant une réécriture d'URL (*URL rewritting*).


```
location /monapp/ {
    rewrite ^/monapp/?(.*)$ /$1 break;
    proxy_pass  http://127.0.0.1:12345;
}
```

La réécriture se base sur des expressions régulières. Il faut donc être un minimum à l'aise avec elles.

Dans cet exemple, `^/monapp/?(.*)$` signifie que l'on va rechercher des URL commençant par /monapp/ et contenant peut-être quelque chose après et `$1` représente ce qui a été trouvé précédemment.

Un exemple pour comprendre : `monip.net/monapp/page1.html` sera réécrit comme `monip.net/page1.html` et cette URL sera transmise au port 12345.