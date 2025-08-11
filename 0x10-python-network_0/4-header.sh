#!/bin/bash
# Envoie une requête GET avec le header X-School-User-Id: 98 et affiche le corps de la réponse
curl -s -H "X-School-User-Id: 98" "http://$1"
