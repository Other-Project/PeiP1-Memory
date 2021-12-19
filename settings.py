"""
Evan Galli et Maxence Lécard
Ce fichier contient les parametres de notre jeu de memory
"""

import formes

# Grille
grilleColonnes = 4  # X
grilleLignes = 3  # Y
tailleCase = 60  # Taille des cases
grillePadding = 40  # Espacement entre les cases

# Couleurs et formes disponibles
_couleurs = [
    "blue",
    "red",
    "green",
    "yellow",
    "orange",
    "pink",
    "gray",
    "violet",
    "lightBlue",
    "lightGreen",
    "brown",
    "magenta",
]
_formes = [
    formes.rond,
    formes.triangle,
    formes.carre,
    formes.pentagone,
    formes.hexagone,
    formes.octogone,
    formes.croix,
    formes.etoile,
    formes.coeur,
]
