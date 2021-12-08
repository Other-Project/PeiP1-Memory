# Evan Galli et Maxence Lécard
# Ce fichier contient les fonctions principales de notre jeu de memory

from turtle import *
import time
import formes
import decor

tailleCase = 60
tailleContenu = tailleCase / 2
marginContenu = (tailleCase - tailleContenu) / 2
grillePadding = 40
grilleColonnes = 4

def positionCase(i):
   y=int(i/grilleColonnes)
   x=i-y*grilleColonnes
   dist=tailleCase+grillePadding
   return (x*dist,y*dist)


def dessineCase(x, y, l, n, t, c="blue"):
	"""Dessine une case avec un nombre dessus"""
	formes.carre(x, y, tailleCase, c, t)
	# on se place pour écrire le chiffre i
	t.up()
	t.goto(x + l / 2 - 10, y + l / 2 - 10)
	t.down()
	c = t.color()
	t.color("white")
	t.write(str(n), font=("Arial", 14, "normal"))
	t.color(c[0])


def dessineCases(cases):
	afficheContenu([])


def afficheContenu(choix):
	tc.clear() 	# on efface ce qui a été dessiné par la tortue des cases

	# selon le choix on dessine la case ou ce qui est caché dessous
	for i in range(len(cases)):
		case=cases[i]
		x,y=positionCase(i)
		if case[2] or i in choix:
			formes.carre(x, y, tailleCase, "blue", tc, False)
			case[1](
				x + marginContenu,  # X
				y + marginContenu,  # Y
				tailleContenu,  # Largeur
				case[0],  # Couleur
				tc,  # Turtle
			)
		else:
			dessineCase(x, y, tailleCase, i + 1, tc)
	ontimer(lambda: dessineCases(cases), 5000)  # On appelle dessineCases après une attente de 2s


tracer(0)  # le dessin est instantané (on ne voit pas le déplacement de la tortue)
td = Turtle()  # tortue du décor
tc = Turtle()  # tortue des cases

decor.main(td)  # on dessine le décor

# dessin des cases
cases = [
	["blue", formes.coeur, False],
	["red", formes.coeur, False],
	["green", formes.croix, False],
	["yellow", formes.rond, False],
	["orange", formes.rond, False],
	["pink", formes.croix, False],
	["gray", formes.triangle, False],
	["violet", formes.triangle, False],
	["lightBlue", formes.octogone, False],
	["lightGreen", formes.octogone, False],
	["brown", formes.carre, False],
	["magenta", formes.carre, False],
]
dessineCases(cases)

while True:
	choix1 = int(numinput("choix 1 ?", "n ?")) - 1  # choix de la case par le joueur
	afficheContenu([choix1])
	choix2 = int(numinput("choix 2 ?", "n ?")) - 1  # choix de la case par le joueur
	afficheContenu([choix1, choix2])

	if cases[choix1][1] == cases[choix2][1]:
		cases[choix1][2] = cases[choix2][2] = True
		if not any(not case[2] for case in cases):
			break
