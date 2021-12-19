"""
Evan Galli et Maxence Lécard
Ce module contient le code chargé du dessin de l'interface
"""

import formes
import turtle


def main(t):
    """Le decor dessine avec la tortue t"""
    fond(t)
    etoiles(t)


def fond(t):
    turtle.bgcolor("midnightblue")


def etoiles(t):
    taille = 25
    gap = taille * 2
    for y in range(10):
        padding = 0
        if y % 2 == 0:
            padding = gap / 2
        for x in range(10):
            formes.etoile(padding + x * gap, y * gap, taille, "gold", t)
