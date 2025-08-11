#!/bin/bash
# Envoie une requête DELETE et affiche le corps de la réponse
curl -s -X DELETE "http://$1"
