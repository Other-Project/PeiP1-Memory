"""
Evan Galli et Maxence Lécard
Ce fichier contient les parametres de notre jeu de memory
"""

import formes

# Grille
grilleColonnes = 4  # Nombre de cases sur x
grilleLignes = 4  # Nombre de cases sur y
tailleCase = 60  # Taille des cases
grillePadding = 40  # Espacement entre les cases
grilleCentreX = 0  # Position en x du centre de la grille
grilleCentreY = 150  # Position en y du centre de la grille

tentativesMax = 2 # Rapport entre le nb de tentatives autorisees et le nb de couples

# Couleurs disponibles
couleurs = [
    "blue",
    "red",
    "green",
    "gray",
    "violet",
    "brown",
    "magenta"
]

# Formes disponibles
# Les fonctions doivent imperativement respecter les parametres suivants: 
# coordonnees x, y en bas a gauche, taille, couleur, tortue
formes = [
    formes.etoile,
    formes.coeur,
    formes.sapin,
    formes.flocon,
    formes.tasse,
    formes.cookie
]
