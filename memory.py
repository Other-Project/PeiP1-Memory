"""
Evan Galli et Maxence Lecard
Ce fichier contient le code principal de notre jeu de memory
"""

# Les librairies tierces
import turtle
import time
import random

# Nos modules
import decor
import cartes
import settings


screen = turtle.Screen()
# pylint: disable=protected-access
screen.cv._rootwindow.resizable(False, False)  # On desactive le redimensionnement
screenX = screen.window_width()
screenY = screen.window_height()

turtle.tracer(0)  # le dessin est instantané (on ne voit pas le deplacement de la tortue)
td = turtle.Turtle(visible=False)  # tortue du decor
tc = turtle.Turtle(visible=False)  # tortue des cases

decor.main(screenX, screenY, td)  # on dessine le decor


# Generation aleatoire des paires de cartes
nombreDeCases = settings.grilleLignes * settings.grilleColonnes
_formes = settings.formes
_couleurs = settings.couleurs
cases = []
for i in range(nombreDeCases // 2):
    couleur = random.choice(_couleurs)  # On choisit une couleur aleatoirement
    _couleurs.remove(couleur)
    forme = random.choice(_formes)  # On choisit une forme aleatoirement
    _formes.remove(forme)
    cases += [[couleur, forme, False]] * 2  # On ajoute 2 fois la carte afin qu'il existe une paire
random.shuffle(cases)  # On melange les cartes


choix1 = -1
sleeping = False
def clickCases(x, y):
    """Fonction appelee lorsque l'utilisateur clique
    Elle detecte si le clic s'est produit sur une case, revelle son contenu
    Elle est aussi en charge de la verification du couple"""
    # pylint: disable=global-statement
    global choix1, sleeping

    # Un couple a ete selectionne, on attend que les cartes soient de nouveau
    # retournee avant d'accepter d'autres commandes
    if sleeping:
        return

    choix = cartes.obtenirCase(x, y)
    if choix in (choix1, -1) or cases[choix][2]: # Clic hors des cases ou cases deja retournees
        return
    if choix1 == -1:
        cartes.afficheContenu(tc, cases, [choix])
        choix1 = choix
        return

    cartes.afficheContenu(tc, cases, [choix1, choix])
    turtle.update()  # On force l'actualisation de l'affichage

    if cases[choix1][0] == cases[choix][0] and cases[choix1][1] == cases[choix][1]:
        # Si les formes et les couleurs sont les memes, on garde les cases retournees
        cases[choix1][2] = cases[choix][2] = True
    else:
        sleeping = True
        time.sleep(1)  # On attend une seconde
        cartes.afficheContenu(tc, cases)
        sleeping = False

    # S'il n'y a pas de case qui n'est pas retournee (cad toute les cases sont retourne)
    if not any(not case[2] for case in cases):
        turtle.bye()  # On ferme le jeu
    else:
        choix1 = -1  # Sinon, on se prepare a recevoir un prochain couple


# Boucle de jeu
cartes.afficheContenu(tc, cases)
turtle.onscreenclick(clickCases)
turtle.mainloop()
