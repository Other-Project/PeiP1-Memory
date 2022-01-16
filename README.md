[![Codacy Badge](https://app.codacy.com/project/badge/Grade/b0442d23f7fa4098ba6f658824359a98)](https://www.codacy.com/gh/Other-Project/PeiP1-Memory/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Other-Project/PeiP1-Memory&amp;utm_campaign=Badge_Grade)  
Projet réalisé par [Evan Galli](https://github.com/06Games) et [Maxence Lécard](https://github.com/Maxence83170) dans le cadre du cours de **Programmation imperative 1**

# Memory

<p align=center>
  <img src="docs/En%20fonctionnement.png" alt="En fonctionnement" /><br />
  <a href="https://github.com/Other-Project/PeiP1-Memory/raw/main/docs/Rapport%20projet%20Galli%20Lecard%20G5.docx">Version DOCX</a>
  <a href="https://github.com/Other-Project/PeiP1-Memory/raw/main/docs/Rapport%20projet%20Galli%20Lecard%20G5.odt">Version ODT</a>
  <a href="https://github.com/Other-Project/PeiP1-Memory/raw/main/docs/Rapport%20projet%20Galli%20Lecard%20G5.pdf">Version PDF</a>
</p>

## Répartition et organisation du travail

Nous avons utilisé l’IDE Visual studio 2022 afin de profiter de la richesse de ses outils et de son confort d’utilisation. 

Nous avons aussi utilisé GitHub afin de nous faciliter la tâche en termes de communication du code et notamment pour le suivi du travail grâce à un historique nous permettant de suivre les modifications apportées par notre binôme.

Nous avons aussi essayé de respecter au maximum les conventions de code, nous avons pour cela utilisé pylint, un outil de vérification de code qui nous a rapporté les changements nécessaires. Pylint attribue à notre projet une note de 9.48 / 10

Pour la répartition du travail, Evan s’est occupé du système de jeu, alors que Maxence s’est occupé du décor. Nous avons aménagé des horaires de travail pendant les vacances, notamment par appels discord.

Bien que ce rapport soit destiné à apporter des explications quant à notre programme, le code contient de nombreux commentaires afin d’expliquer plus en détail certains passages.

## Thème graphique et niveaux de difficulté

Nous avons choisi le niveaux 2+ pour le projet, l'utilisateur peut donc cliquer sur l'objet de son choix. Nous avons aussi implémenté une barre de progression permettant au joueur de visualiser le nombre de tentatives restantes (nous reviendrons plus en détail sur ce point).
Le thème de notre jeu est l’hiver.
Concernant les éléments du décor nous avons mis deux bonhommes de neige au premier plan et les éléments du décor qui se répètent sont les étoiles, celles-ci scintillent et sont positionnées aléatoirement à chaque redémarrage du jeu. Les éléments graphiques comme le reste du système de jeu ont été créé par nos soins.

## Règle du jeu

Le joueur clique une première fois pour retourner la carte, puis il clique sur une seconde carte. Si les deux cartes ont la même forme et la même couleur alors le couple de carte reste retourné, (le cas échéant, les cartes se retournent après un délai d’une seconde). On continue ainsi de suite jusqu’à avoir trouvé toutes les paires de la partie. 
Il y a un nombre maximum d’essai qui dépend du nombre de cartes dans la partie (il correspond au double du nombre de couple de cartes), on peut visualiser ce nombre d’essai grâce à la barre de progression située au milieu en bas de l’écran, au-delà de ce nombre d’essai, la partie s’arrête, et on a perdu.

