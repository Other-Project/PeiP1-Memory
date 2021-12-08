# Evan Galli et Maxence Lécard
# Ce module contient le code chargé du dessin de l'interface

import formes
def main(t):
	"""Le décor dessiné avec la tortue t"""
	formes.croix(-100, -100, 100, "green", t)
	formes.croix(-100, 50, 50, "yellow", t)