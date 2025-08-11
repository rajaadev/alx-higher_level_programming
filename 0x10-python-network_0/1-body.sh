#!/bin/bash
# Affiche la taille en octets du corps de la réponse HTTP d'une URL donnée
curl -s -o /dev/null -w '%{size_download}\n' "$1"
