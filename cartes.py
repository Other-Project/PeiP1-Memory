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
longueurGrille = distCases * settings.grilleColonnes  # Taille de la grille en x
hauteurGrille = distCases * settings.grilleLignes  # Taille de la grille en y
xGrille = longueurGrille / -2 + settings.grilleCentreX  # Position x a laquelle demarre la grille
yGrille = hauteurGrille / -2 + settings.grilleCentreY  # Position y a laquelle demarre la grille


def positionCase(i):
    """Calcule la position des cases"""
    y = int(i / settings.grilleColonnes)
    x = i - y * settings.grilleColonnes
    return (x * distCases + xGrille, y * distCases + yGrille)


def obtenirCase(x, y):
    """Calcule l'index de la case presente aux coordonnees en parametre
    Revoie -1 si les coordonnées sont invalides"""
    for i in range(nombreCases):
        posCase = positionCase(i)
        if posCase[0] <= x <= posCase[0] + settings.tailleCase and posCase[1] <= y <= posCase[1] + settings.tailleCase:
            return i
    return -1


def dessineCase(x, y, taille, index, t, covered=True, coveredColor="#0431B4", visibleColor="#BBF"):
    """Dessine une carte retournee ou non (covered)"""
    formes.rectangle(x, y, taille, taille, coveredColor if covered else visibleColor, t, w=1)

    # Neige sur la carte
    formes.dessine(x, y+taille, "white", t, w=1)
    t.begin_fill()
    t.forward(taille)
    t.right(90)
    t.forward(taille*0.05)
    t.right(65)
    t.forward(taille*0.2)
    t.left(40)
    t.forward(taille*0.075)
    t.right(70)
    t.forward(taille*0.1)
    t.right(40)
    t.forward(taille*0.2)
    t.left(35)
    t.forward(taille*0.1)
    t.left(50)
    t.forward(taille*0.1)
    t.right(40)
    t.forward(taille*0.2)
    t.end_fill()

    if covered:  # Ecrit le chiffre n
        formes.texte(x + taille / 2, y + taille / 2, str(index), t)


def afficheContenu(t, cases, choix=None):
    """Redessine l'entierete de la grille des cases
    en revelant le contenu des cases comprises dans choix
    (ainsi que des cases deja retournees)"""
    t.clear()  # on efface ce qui a a ete dessine par la tortue des cases
    # selon le choix on dessine la case ou ce qui est cache dessous
    i = 0
    for case in cases:
        x, y = positionCase(i)
        if case[2] or (choix is not None and i in choix):
            dessineCase(x, y, settings.tailleCase, i + 1, t, covered=False)
            case[1](
                x + marginContenu,  # X
                y + marginContenu,  # Y
                tailleContenu,  # Largeur
                case[0],  # Couleur
                t,  # Turtle
            )
        else:
            dessineCase(x, y, settings.tailleCase, i + 1, t)
        i += 1


def barreProgression(value, maxValue, t, xOffset=0, yOffset=100, tailleX=150, tailleY=15, fond="gray", barre="blue"):
    """dessine une barre de progression"""
    t.clear()  # On efface la barre precedente
    x = tailleX / -2 + xOffset
    y = tailleY / -2 + yOffset
    formes.rectangle(x, y, tailleX, tailleY, fond, t, w=1)  # Fond
    formes.rectangle(x + 1, y + 1, value / maxValue * (tailleX - 2), tailleY - 2, barre, t, w=1)  # Progression
    formes.texte(xOffset, yOffset, str(value) + " / " + str(maxValue), t, fontSize=int(tailleY * 0.5))  # Texte tentatives utilisées / autorisées
    