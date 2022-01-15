"""
Evan Galli et Maxence Lécard
Ce module contient toutes fonctions de dessin des formes élémentaires
"""

import math


def dessine(x, y, couleur, t, a=0, w=5):
    """Fait les préparatifs avant de commencer à dessiner"""
    t.up()
    t.goto(x, y)
    t.down()
    if a != None:
        t.setheading(a)  # on oriente la tortue vers la droite
    t.color(couleur)
    t.width(w)


def point(x, y, t, w=5, c="blue"):
    dessine(x, y, c, t, w=w)
    t.forward(1)


def texte(x, y, texte, t, fontSize=14, c="white"):
    """Ecrit du texte centré en x,y"""
    width = fontSize / 1.5  # Monaco utilise un rapport h/l de ~1.5
    dessine(x - width // 2 * len(texte), y - fontSize, c, t)
    t.write(texte, font=("Monaco", fontSize, "normal"))


def rond(x, y, diametre, c, t, fill=True, w=5):
    """Dessine un rond"""
    rayon = diametre / 2
    dessine(x + rayon, y, c, t, w)
    if fill:
        t.begin_fill()
    t.circle(rayon)
    if fill:
        t.end_fill()


def triangle(x, y, longueur, c, t, a=180 / 3, aDepart=0):
    dessine(x, y, c, t, a=aDepart)
    t.fillcolor(c)
    t.begin_fill()

    t.forward(longueur)  # Base
    t.left(180 - a)
    t.forward(longueur / (2 * math.cos(math.radians(a))))
    t.left(a * 2)
    t.forward(longueur / (2 * math.cos(math.radians(a))))

    t.end_fill()


def rectangle(x, y, lX, lY, couleur, t, a=0, fill=True, fillColor=None):
    """Dessine un rectangle"""
    dessine(x, y, couleur, t, a=a)
    if fill:
        t.fillcolor(fillColor or couleur)
        t.begin_fill()
    for _ in range(2):
        t.forward(lX)
        t.left(90)
        t.forward(lY)
        t.left(90)
    if fill:
        t.end_fill()


def carre(x, y, longueur, c, t, fill=True, fillColor=None):
    """Dessine un carre"""
    rectangle(x, y, longueur, longueur, c, t, fill=fill, fillColor=fillColor)


def etoile(x, y, longueur, c, t):
    """Dessine une etoile"""
    taille = 2 * longueur / 3  # Les triangles font les 2/3 de la taille totale
    x += (longueur - taille) / 2  # On centre les triangles

    dessine(x, y, c, t)
    triangle(x, y + longueur / 3, taille, c, t)  # Premier triangle
    triangle(x + taille, y + 2 * longueur / 3, taille, c, t, aDepart=180)  # Deuxieme triangle


def coeur(x, y, taille, c, t):
    """Dessine un coeur"""

    # Soient hCreux la hauteur du creux du coeur
    # et l la longueur du carre
    # On sais que t = 3hCreux/4 + l/2
    # Or l = hCreux*cos(45)
    # Donc hCreux = 4t/(3+√2)
    # Et donc l = 4t*cos(45)/(3+√2)
 
    hCreux = 4 * taille / (3 + math.sqrt(2))
    l = hCreux * math.cos(math.radians(45))
    dessine(x + taille / 2, y, c, t, a=45, w=1)

    t.begin_fill()
    t.forward(l)
    t.circle(l / 2, 180)
    t.right(90)
    t.circle(l / 2, 180)
    t.forward(l)
    t.end_fill()


def sapin(x, y, taille, c, t):
    """Dessine un sapin"""
    dessine(x, y, c, t)

    # Tronc
    baseL = taille / 4
    carre(x + (taille - baseL) / 2, y, baseL, "brown", t)

    # Feuilles
    triangleH = (taille - baseL) / 2
    traingleA = math.degrees(math.atan(2 * triangleH / taille))
    triangle(x, y + baseL, taille, c, t, a=traingleA)
    triangle(x, y + baseL + triangleH, taille, c, t, a=traingleA)


def flocon(x, y, taille, c, t):
    """Dessine un flocon"""

    def branche(l):
        """Dessine une branche du flocon"""
        l /= 3  # On divise la branche en 3 parties
        t.forward(l)  # Dessine un /      |_
        for i in range(2):  # Dessine un /
            t.forward(l)  # Dessine /
            t.left(45)
            t.forward(l)  # Dessine |
            t.backward(l)
            t.right(90)
            t.forward(l)  # Dessine _
            t.backward(l)
            t.left(45)
        t.backward(l * 3)  # Retour a la pos. initiale

    dessine(x + taille / 2, y + taille / 2, c, t, w=2)
    for i in range(8):  # Dessine un flocon a 8 branches
        branche(taille / 2)
        t.left(45)  # 360 / 8


def tasse(x, y, taille, c, t):
    """Dessine une tasse"""
    dessine(x, y + taille, c, t, w=1)

    # Dessine la tasse
    t.begin_fill()
    t.right(90)
    t.forward(taille / 2)  # Cote gauche
    t.circle(taille / 2, 180)  # Fond de la tasse
    t.forward(taille / 2)  # Cote droit
    t.left(90)
    t.forward(taille)  # Dessus de la tasse
    t.end_fill()

    # Dessine la anse
    decalageAnse = taille * 0.05
    anseRayon = taille / 4 - decalageAnse
    dessine(x + taille, y + taille / 2 + decalageAnse, c, t, w=1)
    t.begin_fill()
    t.circle(anseRayon, 180)  # Exterieur de la anse
    t.left(90)
    t.forward(anseRayon / 2)  # Largeur de la anse
    t.right(90)
    t.circle(anseRayon / 2, -180)  # Interieur de la anse
    t.end_fill()


def cookie(x, y, taille, c, t):
    """Dessine un cookie"""
    rond(x, y, taille, "#DBA901", t)

    # Pepites
    rond(x + taille * 0.7, y + taille * 0.6, taille / 15, c, t, w=1)
    rond(x + taille * 0.2, y + taille * 0.4, taille / 30, c, t, w=1)
    rond(x + taille * 0.6, y + taille * 0.2, taille / 10, c, t, w=1)
