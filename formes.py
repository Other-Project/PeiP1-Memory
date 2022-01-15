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


def point(x, y, t, w=5, c="blue"):
    dessine(x, y, c, t, w=w)
    t.forward(1)

def texte(x, y, texte, t, fontSize=14, c="white"):
    """Ecrit du texte centré en x,y"""
    width=fontSize/1.5 # Monaco utilise un rapport h/l de ~1.5
    dessine(x - width//2*len(texte), y-fontSize, c, t)
    t.write(texte, font=("Monaco", fontSize, "normal"))

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


def polygone(x, y, taille, couleur, t, nbCotes, resetHeading=True, fill=True, fillColor=None):
    """Dessine aux coordonnees (x,y) et avec la tortue t, un polygone regulier a nbCotes, de taille et de couleur definies"""
    dist = calculeLongueurCote(taille, nbCotes)
    marginX = (taille - dist) / 2

    dessine(x + marginX, y, couleur, t, resetHeading)
    angle = 360 / nbCotes
    if fill:
        t.fillcolor(fillColor or couleur)
        t.begin_fill()
    for _ in range(nbCotes):
        t.forward(dist)
        t.left(angle)
    if fill:
        t.end_fill()
    t.width(1)


def triangle(x, y, taille, c, t, fill=True):
    """Dessine un triangle"""
    tailleY = math.sqrt(calculeLongueurCote(taille, 3)**2 - (taille / 2)**2)
    y += (taille - tailleY) / 2
    polygone(x, y, taille, c, t, 3, fill=fill)


def carre(x, y, longueur, c, t, fill=True, fillColor=None):
    """Dessine un carre"""
    polygone(x, y, longueur, c, t, 4, fill=fill, fillColor=fillColor)


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

def rectangle(x, y, lX, lY, c, t, resetHeading=True, a=0):
    """Dessine un rectangle"""
    dessine(x, y, c, t, resetHeading=resetHeading, a=a)
    t.begin_fill()
    for _ in range(2):
        t.forward(lX)
        t.left(90)
        t.forward(lY)
        t.left(90)
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
    polygone(x + taille, y + 2 * longueur / 3, taille, c, t, 3, False)  # Deuxieme triangle


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
