# Evan Galli et Maxence Lécard
# Ce fichier contient les fonctions principales de notre jeu de memory

import turtle
import time
import random
import formes
import decor

# Grille
grilleColonnes = 4   # X
grilleLignes   = 3   # Y
tailleCase     = 60  # Taille des cases
grillePadding  = 40  # Espacement entre les cases
nombreDeCases=grilleLignes * grilleColonnes
tailleContenu = tailleCase / 2
marginContenu = (tailleCase - tailleContenu) / 2

# Couleurs et formes disponibles
_couleurs = [ "blue", "red", "green", "yellow", "orange", "pink", "gray", "violet", "lightBlue", "lightGreen", "brown", "magenta" ]
_formes = [ formes.rond, formes.triangle, formes.carre, formes.pentagone, formes.hexagone, formes.octogone, formes.croix, formes.etoile, formes.coeur ]

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


def afficheContenu(choix=[]):
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


screen = turtle.Screen()
screen.cv._rootwindow.resizable(False, False) # On désactive le redimensionnement
turtle.setworldcoordinates(-1, -1, screen.window_width() - 1, screen.window_height() - 1) # On crée un systeme de coordonnées commencant en bas à gauche de l'écran

turtle.tracer(0)  # le dessin est instantané (on ne voit pas le déplacement de la tortue)
td = turtle.Turtle(visible=False)  # tortue du décor
tc = turtle.Turtle(visible=False)  # tortue des cases

decor.main(td)  # on dessine le décor


#### Génération aléatoire des paires de cartes
cases = []
for i in range(nombreDeCases//2):
   couleur = random.choice(_couleurs) # On choisit une couleur aléatoirement
   _couleurs.remove(couleur)
   forme = random.choice(_formes) # On choisit une forme aléatoirement
   _formes.remove(forme)
   cases += [[couleur, forme, False]]*2 # On ajoute 2 fois la carte afin qu'il existe une paire
random.shuffle(cases) # On mélange les cartes


#### Boucle de jeu
afficheContenu()
while True:
	choix1 = int(turtle.numinput("choix 1 ?", "n ?")) - 1  # choix de la case par le joueur
	afficheContenu([choix1])
	choix2 = int(turtle.numinput("choix 2 ?", "n ?")) - 1  # choix de la case par le joueur
	afficheContenu([choix1, choix2])

	turtle.update() # On force l'actualisation de l'affichage
	if cases[choix1][0] == cases[choix2][0] and cases[choix1][1] == cases[choix2][1]:
		cases[choix1][2] = cases[choix2][2] = True # Si les formes et les couleurs sont les mêmes, on garde les cases retournées
	else:
		time.sleep(1) # On attend 1s
		afficheContenu()
	if not any(not case[2] for case in cases):
		break
