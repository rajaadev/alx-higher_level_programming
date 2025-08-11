#!/bin/bash
# Envoie une requête GET vers /catch_me et affiche le corps de la réponse
curl -s -X GET -H "User-Agent: curl" http://0.0.0.0:5000/catch_me
