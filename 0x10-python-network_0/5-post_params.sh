#!/bin/bash
# Envoie une requête POST avec email et subject, affiche le corps de la réponse
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "http://$1"
