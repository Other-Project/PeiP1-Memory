# Evan Galli et Maxence Lécard
# Ce fichier contient les fonctions dédiées au fonctionnement des cases

import settings
import formes

tailleContenu  = settings.tailleCase / 2
marginContenu  = (settings.tailleCase - tailleContenu) / 2

def dessineCase(x, y, l, n, t, c="blue"):
	"""Dessine une case avec un nombre dessus"""
	formes.carre(x, y, l, c, t)
	# on se place pour écrire le chiffre n
	t.up()
	t.goto(x + l / 2 - 10, y + l / 2 - 10)
	t.down()
	c = t.color()
	t.color("white")
	t.write(str(n), font=("Arial", 14, "normal"))
	t.color(c[0])


def positionCase(i):
   """Calcule la position des cases"""
   y=int(i/settings.grilleColonnes)
   x=i-y*settings.grilleColonnes
   dist=settings.tailleCase+settings.grillePadding
   return (x*dist,y*dist)


def afficheContenu(tc, cases, choix=[]):
	"""Redessine l'entièreté de la grille des cases 
		en révélant le contenu des cases comprises dans choix
		(ainsi que des cases déja retournées)"""
	tc.clear() 	# on efface ce qui a été dessiné par la tortue des cases

	# selon le choix on dessine la case ou ce qui est caché dessous
	for i in range(len(cases)):
		case=cases[i]
		x,y=positionCase(i)
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