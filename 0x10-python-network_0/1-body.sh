#!/bin/bash
# Envoie une requête GET et affiche le corps uniquement si le code HTTP est 200
curl -s -w '%{http_code}' -o /tmp/body_$$ "http://$1" | grep -q '^200$' && cat /tmp/body_$$; rm /tmp/body_$$
