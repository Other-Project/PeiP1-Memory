"""
Evan Galli et Maxence Lécard
Ce fichier contient les parametres de notre jeu de memory
"""

import formes

# Grille
grilleColonnes = 4  # Nombre de cases sur x
grilleLignes = 3  # Nombre de cases sur y
tailleCase = 60  # Taille des cases
grillePadding = 40  # Espacement entre les cases
grilleCentreX = 0 # Position en x du centre de la grille
grilleCentreY = 100 # Position en y du centre de la grille

# Couleurs et formes disponibles
couleurs = [
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
formes = [
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
