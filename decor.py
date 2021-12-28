"""
Evan Galli et Maxence Lécard
Ce module contient le code chargé du dessin de l'interface
"""

import formes
import turtle


def main(screenX, screenY, t):
    """Le decor dessine avec la tortue t"""
    etoiles(screenX / -2, screenY / -2, t)
    fond(screenX, screenY, t)
    bonhommeDeNeige(screenX / -2 +  50, screenY / -2 + 100, t)
    bonhommeDeNeige(screenX /  2 - 150, screenY / -2 + 100, t)


def fond(screenX, screenY, t):
    turtle.bgcolor("midnightblue")
    sol(screenX / -2, screenY / -2, 1000, 250, t)


def etoiles(xStart, yStart, t):
    # TODO: Etoiles qui sintillent
    taille = 25
    gap = taille * 2
    for y in range(30):
        padding = 0
        if y % 2 == 0:
            padding = gap / 2
        for x in range(30):
            formes.etoile(padding + x * gap + xStart, y * gap + yStart, taille, "gold", t)


def sol(x, y, lX, lY, t):
    formes.dessine(x, y, "#EFEDED", t)
    t.begin_fill()
    for _ in range(2):
        t.forward(lX)
        t.left(90)
        t.forward(lY)
        t.left(90)
    t.end_fill()


#####
# On definit les fonctions dont on va avoir besoin pour tracer le bonhomme de neige
#####


def baton(x, y, longueur, c, angle, t):
    formes.dessine(x, y, c, t, a=angle)
    t.fillcolor(c)
    t.begin_fill()
    for i in range(2):
        t.forward(longueur)
        t.left(90)
        t.forward(longueur / 10)
        t.left(90)
    t.end_fill()


def carrote(x, y, longueur, c, t):
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
    baton(x2, y2 + diametre2 / 2, 50, "brown", 180 - angleBaton, t)
    baton(x2 + diametre2, y2 + diametre2 / 2, 50, "brown", angleBaton, t)

    # boules de neiges qui forment le corps du bonhomme
    formes.rond(x, y, diametre, "white", t, fill=True)
    formes.rond(x2, y2, diametre2, "white", t, fill=True)
    formes.rond(x3, y3, diametre3, "white", t, fill=True)

    # carrote du bonhomme de neige
    carrote(x3 + diametre3 / 2, y3 + diametre3 / 3, 20, "orange", t)

    # yeux sur le corps du bonhomme
    rayonYeux = 3
    formes.rond(x3 + diametre3 / 6 - rayonYeux, y3 + 2 * diametre3 / 3, rayonYeux * 2, "black", t, fill=True)
    formes.rond(x3 + 5 * diametre3 / 6 - rayonYeux, y3 + 2 * diametre3 / 3, rayonYeux * 2, "black", t, fill=True)

    # boutons sur le corps du bonhomme
    rayonBouton = 4
    yButton = y + 25
    for i in range(3):
        formes.rond(x + diametre / 2 - rayonBouton, yButton + i * 25, rayonBouton * 2, "black", t, fill=True)
