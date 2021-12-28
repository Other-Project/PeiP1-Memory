"""
Evan Galli et Maxence Lécard
Ce fichier contient les fonctions dédiées au fonctionnement des cases
"""

import settings
import formes

tailleContenu = settings.tailleCase / 2  # Le contenu est deux fois plus petit que la case
marginContenu = (settings.tailleCase - tailleContenu) / 2  # Decalage (en x et y) du contenu par rapport a la case
distCases = settings.tailleCase + settings.grillePadding  # Distance entre chaque case (au pt en bas a gauche)
xGrille = distCases * settings.grilleColonnes / -2  # Position x a laquelle demarre la grille
yGrille = distCases * settings.grilleLignes / -2  # Position y a laquelle demarre la grille


def dessineCase(x, y, l, n, t, c="blue"):
    """Dessine une case avec un nombre dessus"""
    formes.carre(x, y, l, c, t)
    # on se place pour ecrire le chiffre n
    t.up()
    t.goto(x + l / 2 - 10, y + l / 2 - 10)
    t.down()
    c = t.color()
    t.color("white")
    t.write(str(n), font=("Arial", 14, "normal"))
    t.color(c[0])


def positionCase(i):
    """Calcule la position des cases"""
    y = int(i / settings.grilleColonnes)
    x = i - y * settings.grilleColonnes
    return (x * distCases + xGrille, y * distCases + yGrille)


def obtenirCase(cases, x, y):
    """Calcule l'index de la case presente aux coordonnees en parametre"""

    i = ((x - xGrille) / distCases) + ((y - yGrille) / distCases) * settings.grilleColonnes - 1

    if i < 0:
        return -1
    elif i >= len(cases):
        return -1
    else:
        return int(i)  # TODO, detecter si clic entre les cases


def afficheContenu(tc, cases, choix=[]):
    """Redessine l'entierete de la grille des cases
    en revelant le contenu des cases comprises dans choix
    (ainsi que des cases deja retournees)"""
    tc.clear()  # on efface ce qui a a ete dessine par la tortue des cases
    # selon le choix on dessine la case ou ce qui est cache dessous
    for i in range(len(cases)):
        case = cases[i]
        x, y = positionCase(i)
        if case[2] or i in choix:
            formes.carre(x, y, settings.tailleCase, "blue", tc, False)
            case[1](
                x + marginContenu,  # X
                y + marginContenu,  # Y
                tailleContenu,  # Largeur
                case[0],  # Couleur
                tc,  # Turtle
            )
        else:
            dessineCase(x, y, settings.tailleCase, i + 1, tc)
