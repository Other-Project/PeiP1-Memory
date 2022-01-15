"""
Evan Galli et Maxence Lécard
Ce module contient le code chargé du dessin du decor
Theme: Hiver
"""

import turtle
import random
import math
import itertools

import formes
import cartes


def main(screenX: int, screenY: int, t: turtle.Turtle):
    """Le decor dessine avec la tortue t"""

    leftScreen = screenX / -2
    rightScreen = -leftScreen
    bottomScreen = screenY / -2

    # On trace le sol
    solHauteur = 250
    formes.rectangle(leftScreen, bottomScreen, 1000, solHauteur, "#EFEDED", t)

    turtle.bgcolor("midnightblue")  # On defini la couleur du fond (ciel)

    # On trace les bonhommes de neige
    etoilesLeftY = bonhommeDeNeige(leftScreen + 50, bottomScreen + 100, t)
    etoilesRightY = bonhommeDeNeige(rightScreen - 150, bottomScreen + 100, t)

    # Generation et affichage des etoiles
    tailleEtoiles = 25  # Taille maximale d'une etoile
    gapEtoiles = tailleEtoiles * 2  # Espacement entre chaque coordonnees d'etoile
    coordonneesEtoiles = generateEtoiles(
        # Etoiles a gauche
        leftScreen,  # X
        etoilesLeftY,  # Y
        abs(leftScreen - cartes.xGrille) - tailleEtoiles,  # W
        screenY - abs(etoilesLeftY) - tailleEtoiles,  # H
        gapEtoiles,
        random.randint(10, 20),
    )
    coordonneesEtoiles += generateEtoiles(
        # Etoiles a droite
        cartes.xGrille + cartes.longueurGrille,
        etoilesRightY,
        abs(rightScreen + cartes.xGrille) - tailleEtoiles,
        screenY - abs(etoilesRightY) - tailleEtoiles,
        gapEtoiles,
        random.randint(10, 20),
    )
    etoiles(coordonneesEtoiles, turtle.Turtle(visible=False))


def generateEtoiles(left, bottom, width, height, gap, n):
    """Generes une liste de n tuples (x,y,s)
    dont les coordonnees sont comprise dans le rect
    tout en respectant un espacement minimum"""

    # On divise toutes les valeurs par le gap
    # Afin de s'assurer que les etoiles ne se touchent pas
    leftWG = math.ceil(left / gap)
    rightWG = math.floor((left + width) / gap)
    bottomWG = math.ceil(bottom / gap)
    topWG = math.floor((bottom + height) / gap)

    # On calcul l'ensemble des coordonnees possibles
    coordonnees = list(itertools.product(range(leftWG, rightWG + 1), range(bottomWG, topWG + 1)))

    # On selection n couples parmis les coordonnees possibles,
    # on re-multiplie les coordonnees precedemment divisee par le gap
    # et on genere une taille aleatoire
    return [(coor[0] * gap, coor[1] * gap, random.randint(10, 25)) for coor in random.sample(coordonnees, n)]


def etoiles(infos, t):
    """Dessine les etoiles de coordonnees et tailles definies"""
    t.clear()
    for info in infos:
        r = 255
        g = random.randint(200, 230)
        b = 0
        formes.etoile(info[0], info[1], info[2], (r, g, b), t)

    # On actualise l'affichage toute les demie-secondes
    turtle.ontimer(lambda: etoiles(infos, t), t=500)


#####
# On definit les fonctions dont on va avoir besoin pour tracer le bonhomme de neige
#####


def carotte(x, y, longueur, c, t):
    formes.dessine(x, y, c, t)
    t.fillcolor(c)
    t.begin_fill()
    t.left(10)
    t.forward(longueur)
    t.left(180 - 10)
    t.forward(longueur)
    t.left(90)
    t.forward(longueur / 5)
    t.end_fill()


def bonhommeDeNeige(x, y, t):
    diametre = 100  # Diametre de la premiere boule de neige
    diametre2 = diametre * 0.75  # Diametre de la 2e
    diametre3 = diametre * 0.50  # Diametre de la 3e
    x2 = x + (diametre - diametre2) / 2  # Coordonnee x (du pt en bas à gauche) de la 2e boule de neige
    x3 = x + (diametre - diametre3) / 2  # Coordonnee x (du pt en bas à gauche) de la 3e boule de neige
    y2 = y + diametre2  # Coordonnee y (du pt en bas a gauche) de la 2e boule de neige
    y3 = y2 + diametre3 + (diametre / 10)  # Coordonnee y (du pt en bas à gauche) de la 3e boule de neige

    # batons qui forment les bras du bonhomme de neige
    angleBaton = 30
    formes.rectangle(x2, y2 + diametre2 / 2, 50, 5, "brown", t, a=180 - angleBaton)
    formes.rectangle(x2 + diametre2, y2 + diametre2 / 2, 50, 5, "brown", t, a=angleBaton)

    # boules de neiges qui forment le corps du bonhomme
    formes.rond(x, y, diametre, "white", t, fill=True)
    formes.rond(x2, y2, diametre2, "white", t, fill=True)
    formes.rond(x3, y3, diametre3, "white", t, fill=True)

    # carotte du bonhomme de neige
    carotte(x3 + diametre3 / 2, y3 + diametre3 / 3, 20, "orange", t)

    # yeux sur le corps du bonhomme
    rayonYeux = 3
    formes.rond(x3 + diametre3 / 6 - rayonYeux, y3 + 2 * diametre3 / 3, rayonYeux * 2, "black", t, fill=True)
    formes.rond(x3 + 5 * diametre3 / 6 - rayonYeux, y3 + 2 * diametre3 / 3, rayonYeux * 2, "black", t, fill=True)

    # boutons sur le corps du bonhomme
    rayonBouton = 4
    yButton = y + 25
    for i in range(3):
        formes.rond(x + diametre / 2 - rayonBouton, yButton + i * 25, rayonBouton * 2, "black", t, fill=True)

    return y3 + diametre3
