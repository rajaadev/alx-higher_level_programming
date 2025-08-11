#!/bin/bash
# Affiche les méthodes HTTP acceptées par le serveur pour une URL donnée via OPTIONS
curl -s -X OPTIONS -i "http://$1" | grep -i Allow: | cut -d' ' -f2-
