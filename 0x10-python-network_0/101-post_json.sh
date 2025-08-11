#!/bin/bash
# Envoie un POST JSON avec le contenu d’un fichier, affiche le corps de la réponse
curl -s -H "Content-Type: application/json" -X POST --data-binary @"$2" "http://$1"
