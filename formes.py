"""
Evan Galli et Maxence Lécard
Ce module contient toutes fonctions de dessin des formes élémentaires
"""

import math


def dessine(x, y, couleur, t, resetHeading=True, a=0, w=5):
    """Fait les préparatifs avant de commencer à dessiner"""
    t.up()
    t.goto(x, y)
    t.down()
    if resetHeading:
        t.setheading(a)  # on oriente la tortue vers la droite
    t.color(couleur)
    t.width(w)


def point(x, y, t, w=10, c="blue"):
    dessine(x, y, t, w=w)
    t.forward(1)


def calculeLongueurCote(tailleMax, nbCotes):
    """Calcule la longueur des cotes d'un polynome régulier en
    utilisant les proprietes du cercles circonscrit (https://en.wikipedia.org/wiki/Regular_polygon#Circumradius)
    et de l'apothème (https://fr.wikipedia.org/wiki/Apothème)"""
    a = math.pi / nbCotes
    if nbCotes % 2:  # nb pair de cotes
        cote = tailleMax * 2 * math.sin(a) / (1 + math.cos(a))
    else:  # nb impaire de cotes
        cote = tailleMax * math.tan(a)

    # Pour des raisons que j'ignore,
    # la taille retournee est parfois plus grande que la taille maximale,
    # dans ces cas, on se rabat sur la taille max
    return min(tailleMax, cote)


def polygone(x, y, taille, couleur, t, nbCotes, resetHeading=True, fill=True):
    """Dessine aux coordonnÃ©es (x,y) et avec la tortue t, un polygone a nbCotes, de taille et de couleur definies"""
    dist = calculeLongueurCote(taille, nbCotes)
    marginX = (taille - dist) / 2

    dessine(x + marginX, y, couleur, t, resetHeading)
    angle = 360 / nbCotes
    if fill:
        t.begin_fill()
    for i in range(nbCotes):
        t.forward(dist)
        t.left(angle)
    if fill:
        t.end_fill()
    t.width(1)


def triangle(x, y, taille, c, t, fill=True):
    """Dessine un triangle"""
    tailleY = math.sqrt(calculeLongueurCote(taille, 3) ** 2 - (taille / 2) ** 2)
    y += (taille - tailleY) / 2
    polygone(x, y, taille, c, t, 3, fill=fill)


def carre(x, y, longueur, c, t, fill=True):
    """Dessine un carre"""
    polygone(x, y, longueur, c, t, 4, fill=fill)


def pentagone(x, y, longueur, c, t, fill=True):
    """Dessine un pentagone"""
    polygone(x, y, longueur, c, t, 5, fill=fill)


def hexagone(x, y, longueur, c, t, fill=True):
    """Dessine un hexagone"""
    polygone(x, y, longueur, c, t, 6, fill=fill)


def octogone(x, y, longueur, c, t, fill=True):
    """Dessine un octogone"""
    polygone(x, y, longueur, c, t, 8, fill=fill)


def rond(x, y, diametre, c, t, fill=True):
    """Dessine un rond"""
    rayon = diametre / 2
    dessine(x + rayon, y, c, t)
    if fill:
        t.begin_fill()
    t.circle(rayon)
    if fill:
        t.end_fill()


# dessine une croix dans le carré de largeur l dont le point en bas
# à gauche est (x,y), avec la tortue t
def croix(x, y, l, c, t):
    """Dessine une croix"""
    dessine(x, y, c, t)
    t.width(5)
    t.goto(x + l, y + l)
    t.up()
    t.goto(x + l, y)
    t.down()
    t.goto(x, y + l)
    t.width(1)


def etoile(x, y, longueur, c, t):
    """Dessine une etoile"""
    taille = 2 * longueur / 3  # Les triangles font les 2/3 de la taille totale
    x += (longueur - taille) / 2  # On centre les triangles

    dessine(x, y, c, t)
    polygone(x, y + longueur / 3, taille, c, t, 3, False)  # Premier triangle
    t.right(180)  # On dessine le triangle dans le sens inverse
    polygone(
        x + taille, y + 2 * longueur / 3, taille, c, t, 3, False
    )  # Deuxieme triangle


def coeur(x, y, taille, c, t):
    """Dessine un coeur"""
    a = 45
    l = 2 / 3 * taille
    dessine(x + taille / 2 - 2.5, y, c, t, True, a)

    t.begin_fill()
    t.forward(l)
    t.circle(taille / 4, 180 + a)
    t.right(180)
    t.circle(taille / 4, 180 + a)
    t.forward(l)
    t.end_fill()
