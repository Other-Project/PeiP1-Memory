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
    if a is not None:
        t.setheading(a)  # on oriente la tortue vers la droite
    t.color(couleur)
    t.width(w)


def point(x, y, t, w=5, couleur="blue"):
    """Fonction dessinant un point (utile pour le debogage)"""
    dessine(x, y, couleur, t, w=w)
    t.forward(1)


def texte(x, y, txt, t, fontSize=14, c="white"):
    """Ecrit du texte centré en x,y"""
    width = fontSize / 1.5  # Monaco utilise un rapport h/l de ~1.5
    dessine(x - width // 2 * len(txt), y - fontSize, c, t)
    t.write(txt, font=("Monaco", fontSize, "normal"))


def rond(x, y, diametre, couleur, t, fill=True, w=5):
    """Dessine un rond"""
    rayon = diametre / 2
    dessine(x + rayon, y, couleur, t, w)
    if fill:
        t.begin_fill()
    t.circle(rayon)
    if fill:
        t.end_fill()


def triangle(x, y, longueur, couleur, t, a=180 / 3, aDepart=0):
    """Dessine un triangle en fct de la longueur de sa base"""
    dessine(x, y, couleur, t, a=aDepart)
    t.fillcolor(couleur)
    t.begin_fill()

    t.forward(longueur)  # Base
    t.left(180 - a)
    t.forward(longueur / (2 * math.cos(math.radians(a))))
    t.left(a * 2)
    t.forward(longueur / (2 * math.cos(math.radians(a))))

    t.end_fill()


def rectangle(x, y, longueur, hauteur, couleur, t, a=0, fill=True, fillColor=None, w=5):
    """Dessine un rectangle"""
    dessine(x, y, couleur, t, a=a, w=w)
    if fill:
        t.fillcolor(fillColor or couleur)
        t.begin_fill()
    for _ in range(2):
        t.forward(longueur)
        t.left(90)
        t.forward(hauteur)
        t.left(90)
    if fill:
        t.end_fill()


def etoile(x, y, longueur, couleur, t):
    """Dessine une etoile"""
    taille = 2 * longueur / 3  # Les triangles font les 2/3 de la taille totale
    x += (longueur - taille) / 2  # On centre les triangles

    dessine(x, y, couleur, t)
    triangle(x, y + longueur / 3, taille, couleur, t)  # Premier triangle
    triangle(x + taille, y + 2 * longueur / 3, taille, couleur, t, aDepart=180)  # Deuxieme triangle


def coeur(x, y, taille, couleur, t):
    """Dessine un coeur"""

    # Soient hCreux la hauteur du creux du coeur
    # et l la longueur du carre
    # On sais que t = 3hCreux/4 + l/2
    # Or l = hCreux*cos(45)
    # Donc hCreux = 4t/(3+√2)
    # Et donc l = 4t*cos(45)/(3+√2)

    hCreux = 4 * taille / (3 + math.sqrt(2))
    l = hCreux * math.cos(math.radians(45))
    dessine(x + taille / 2, y, couleur, t, a=45, w=1)

    t.begin_fill()
    t.forward(l)
    t.circle(l / 2, 180)
    t.right(90)
    t.circle(l / 2, 180)
    t.forward(l)
    t.end_fill()


def sapin(x, y, taille, couleur, t):
    """Dessine un sapin"""
    dessine(x, y, couleur, t)

    # Tronc
    baseL = taille / 4
    rectangle(x + (taille - baseL) / 2, y, baseL, baseL, "brown", t)

    # Feuilles
    triangleH = (taille - baseL) / 2
    traingleA = math.degrees(math.atan(2 * triangleH / taille))
    triangle(x, y + baseL, taille, couleur, t, a=traingleA)
    triangle(x, y + baseL + triangleH, taille, couleur, t, a=traingleA)


def flocon(x, y, taille, couleur, t):
    """Dessine un flocon"""

    def branche(l):
        """Dessine une branche du flocon"""
        l /= 3  # On divise la branche en 3 parties
        t.forward(l)  # Dessine un /      |_
        for _ in range(2):  # Dessine un /
            t.forward(l)  # Dessine /
            t.left(45)
            t.forward(l)  # Dessine |
            t.backward(l)
            t.right(90)
            t.forward(l)  # Dessine _
            t.backward(l)
            t.left(45)
        t.backward(l * 3)  # Retour a la pos. initiale

    dessine(x + taille / 2, y + taille / 2, couleur, t, w=2)
    for _ in range(8):  # Dessine un flocon a 8 branches
        branche(taille / 2)
        t.left(45)  # 360 / 8


def tasse(x, y, taille, couleur, t):
    """Dessine une tasse"""
    dessine(x, y + taille, couleur, t, w=1)

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
    dessine(x + taille, y + taille / 2 + decalageAnse, couleur, t, w=1)
    t.begin_fill()
    t.circle(anseRayon, 180)  # Exterieur de la anse
    t.left(90)
    t.forward(anseRayon / 2)  # Largeur de la anse
    t.right(90)
    t.circle(anseRayon / 2, -180)  # Interieur de la anse
    t.end_fill()


def cookie(x, y, taille, couleur, t):
    """Dessine un cookie"""
    rond(x, y, taille, "#DBA901", t)

    # Pepites
    rond(x + taille * 0.7, y + taille * 0.6, taille / 15, couleur, t, w=1)
    rond(x + taille * 0.2, y + taille * 0.4, taille / 30, couleur, t, w=1)
    rond(x + taille * 0.6, y + taille * 0.2, taille / 10, couleur, t, w=1)
