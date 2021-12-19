"""
Evan Galli et Maxence Lécard
Ce fichier contient le code principal de notre jeu de memory
"""

import turtle
import time
import random
import decor
import cartes
import settings


screen = turtle.Screen()
screen.cv._rootwindow.resizable(False, False)  # On desactive le redimensionnement
# On cree un systeme de coordonnees commencant en bas à gauche de l'écran
turtle.setworldcoordinates(-1, -1, screen.window_width() - 1, screen.window_height() - 1)

turtle.tracer(0)  # le dessin est instantané (on ne voit pas le deplacement de la tortue)
td = turtle.Turtle(visible=False)  # tortue du decor
tc = turtle.Turtle(visible=False)  # tortue des cases

decor.main(td)  # on dessine le decor


# Generation aleatoire des paires de cartes
nombreDeCases = settings.grilleLignes * settings.grilleColonnes
cases = []
for i in range(nombreDeCases // 2):
   couleur = random.choice(settings._couleurs)  # On choisit une couleur aleatoirement
   settings._couleurs.remove(couleur)
   forme = random.choice(settings._formes)  # On choisit une forme aleatoirement
   settings._formes.remove(forme)
   cases += [[couleur, forme, False]] * 2  # On ajoute 2 fois la carte afin qu'il existe une paire
random.shuffle(cases)  # On melange les cartes


#### Boucle de jeu
cartes.afficheContenu(tc, cases)
while True:
	choix1 = int(turtle.numinput("choix 1 ?", "n ?")) - 1  # choix de la case par le joueur
	cartes.afficheContenu(tc, cases, [choix1])
	choix2 = int(turtle.numinput("choix 2 ?", "n ?")) - 1  # choix de la case par le joueur
	cartes.afficheContenu(tc, cases, [choix1, choix2])

	turtle.update() # On force l'actualisation de l'affichage
	if cases[choix1][0] == cases[choix2][0] and cases[choix1][1] == cases[choix2][1]:
		cases[choix1][2] = cases[choix2][2] = True # Si les formes et les couleurs sont les mêmes, on garde les cases retournées
	else:
		time.sleep(1) # On attend 1s
		cartes.afficheContenu(tc, cases)
	if not any(not case[2] for case in cases):
		break
