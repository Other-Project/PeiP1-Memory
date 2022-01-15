"""
Evan Galli et Maxence Lécard
Ce fichier contient les fonctions dédiées au fonctionnement des cases
"""

import settings
import formes

nombreCases = settings.grilleLignes * settings.grilleColonnes
tailleContenu = settings.tailleCase / 2  # Le contenu est deux fois plus petit que la case
marginContenu = (settings.tailleCase - tailleContenu) / 2  # Decalage (en x et y) du contenu par rapport a la case
distCases = settings.tailleCase + settings.grillePadding  # Distance entre chaque case (au pt en bas a gauche)
longueurGrille = distCases * settings.grilleColonnes
hauteurGrille = distCases * settings.grilleLignes
xGrille = longueurGrille / -2 + settings.grilleCentreX  # Position x a laquelle demarre la grille
yGrille = hauteurGrille / -2 + settings.grilleCentreY  # Position y a laquelle demarre la grille


def positionCase(i):
    """Calcule la position des cases"""
    y = int(i / settings.grilleColonnes)
    x = i - y * settings.grilleColonnes
    return (x * distCases + xGrille, y * distCases + yGrille)


def obtenirCase(x, y):
    """Calcule l'index de la case presente aux coordonnees en parametre"""
    for i in range(nombreCases):
        posCase = positionCase(i)
        if (posCase[0] <= x <= posCase[0] + settings.tailleCase) and (posCase[1] <= y <= posCase[1] + settings.tailleCase):
            return i
    return -1


def dessineCase(x, y, l, n, t, c="blue"):
    """Dessine une case avec un nombre dessus"""
    formes.carre(x, y, l, c, t)
    # Ecrit le chiffre n
    formes.texte(x + l / 2, y + l / 2, str(n), t)


def afficheContenu(tc, cases, choix=None):
    """Redessine l'entierete de la grille des cases
    en revelant le contenu des cases comprises dans choix
    (ainsi que des cases deja retournees)"""
    tc.clear()  # on efface ce qui a a ete dessine par la tortue des cases
    # selon le choix on dessine la case ou ce qui est cache dessous
    for i in range(len(cases)):
        case = cases[i]
        x, y = positionCase(i)
        if case[2] or (choix is not None and i in choix):
            formes.carre(x, y, settings.tailleCase, "blue", tc, fillColor="#BBF")
            case[1](
                x + marginContenu,  # X
                y + marginContenu,  # Y
                tailleContenu,  # Largeur
                case[0],  # Couleur
                tc,  # Turtle
            )
        else:
            dessineCase(x, y, settings.tailleCase, i + 1, tc)


def barreProgression(tentatives, tentativesMax, t, xOffset=0, yOffset=100, tailleX=150, tailleY=10):
    """dessine une barre de progression"""
    t.clear()  # On efface la barre precedente
    x = tailleX / -2 + xOffset
    y = tailleY / -2 + yOffset
    formes.rectangle(x, y, tailleX, tailleY, "gray", t)  # Fond
    formes.rectangle(x + 1, y + 1, tentatives / tentativesMax * (tailleX - 2), tailleY - 2, "blue", t)  # Progression
    formes.texte(xOffset, yOffset, str(tentatives) + " / " + str(tentativesMax), t, fontSize=int(tailleY * 0.75))  # Texte tentatives utilisées / autorisées
    