"""
Evan Galli et Maxence Lécard
Ce fichier contient le code principal de notre jeu de memory
"""

# Les librairies tierces
import turtle
import time
import random
import itertools

# Nos modules
import decor
import cartes
import settings
import formes


screen = turtle.Screen()
screen.colormode(255)  # On represente les couleurs par un nombre entier de 0 a 255
# pylint: disable=protected-access
screen.cv._rootwindow.resizable(False, False)  # On desactive le redimensionnement
screenX = screen.window_width()
screenY = screen.window_height()

turtle.tracer(0)  # le dessin est instantané (on ne voit pas le deplacement de la tortue)
td = turtle.Turtle(visible=False)  # tortue du decor
tc = turtle.Turtle(visible=False)  # tortue des cases
tp = turtle.Turtle(visible=False)  # tortue de la progression

decor.main(screenX, screenY, td)  # on dessine le decor


#############################################
# Generation aleatoire des paires de cartes #
#############################################
# Genere en priorité des couples de couleur et de forme unique
# puis utilise des formes/couleurs deja sorties pour les couples restant

nombreDeCouples = settings.grilleLignes * settings.grilleColonnes // 2 # Nb de couples a generer
# On genere une liste de l'ensemble des couples forme/couleur
couples = [list(case) for case in itertools.product(settings.couleurs, settings.formes, [False])]
nombreDeCouplesTotalementUniques = min(len(settings.couleurs), len(settings.formes), nombreDeCouples)
# On genere une liste avec le maximum de couple dont la couleur et la forme n'ont pas ete choisie
cases = [
    couples[i * len(settings.couleurs) + random.randint(0, nombreDeCouplesTotalementUniques)]
    for i in range(nombreDeCouplesTotalementUniques)
]
couples = [case for case in couples if case not in cases]  # On ne garde que les couples forme/couleur non tires
# On selectionne le restant des couples forme/couleur
cases += random.choices(couples, k=nombreDeCouples - len(cases))
cases *= 2  # On dupplique la selection afin d'obtenir des couples de cartes
random.shuffle(cases)  # On melange les cartes


##############################################
#                     Jeu                    #
##############################################

tentatives = 0
tentativesMax = nombreDeCouples * settings.tentativesMax

choix1 = -1
sleeping = False # Desactive les actions du joueur
def clickCases(x, y):
    """Fonction appelee lorsque l'utilisateur clique
    Elle detecte si le clic s'est produit sur une case, revelle son contenu
    Elle est aussi en charge de la verification du couple"""
    # pylint: disable=global-statement
    global tentatives, choix1, sleeping

    # Un couple a ete selectionne, on attend que le contenu soit de nouveau
    # cache avant d'accepter d'autres commandes
    if sleeping:
        return

    choix = cartes.obtenirCase(x, y)
    if choix in (choix1, -1) or cases[choix][2]:  # Clic hors des cases ou case deja retournee
        return
    if choix1 == -1:  # Premiere case du couple
        cartes.afficheContenu(tc, cases, [choix])
        choix1 = choix
        return  # On attend le choix de la seconde case

    cartes.afficheContenu(tc, cases, [choix1, choix])
    turtle.update()  # On force l'actualisation de l'affichage

    if cases[choix1][0] == cases[choix][0] and cases[choix1][1] == cases[choix][1]:
        # Si les formes et les couleurs sont les memes, on garde les cases retournees
        cases[choix1][2] = cases[choix][2] = True
    else:
        tentatives += 1
        sleeping = True
        time.sleep(1)  # On attend une seconde
        cartes.afficheContenu(tc, cases)
        sleeping = False
    cartes.barreProgression(tentatives, tentativesMax, tp, yOffset=screenY / -2 + 100)

    # S'il n'y a pas de case qui n'est pas retournee (cad toutes les cases sont retournees)
    if not any(not case[2] for case in cases):  # Gagne !
        ecranDeFin("Gagné !")
    elif tentatives > tentativesMax:  # Perdu !
        ecranDeFin("Perdu !")
    else:  # Le jeu continue
        choix1 = -1  # Sinon, on se prepare a recevoir un prochain couple


def ecranDeFin(texte):
    # On efface tout
    tc.clear()
    tp.clear()

    formes.texte(settings.grilleCentreX, settings.grilleCentreY, texte, tc, fontSize=24)
    turtle.onscreenclick(lambda x, y: turtle.bye())  # On ferme le jeu si l'utilisateur clique


# Boucle de jeu
cartes.barreProgression(tentatives, tentativesMax, tp, yOffset=screenY / -2 + 100)
cartes.afficheContenu(tc, cases)
turtle.onscreenclick(clickCases)
turtle.mainloop()
