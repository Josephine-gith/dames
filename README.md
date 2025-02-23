## Dames
Alexandre Viot et Joséphine Péronne

# Consignes de jeu
Pour jouer au jeu de dames, exécuter main.py.
Cliquer sur une case pour sélectionner le pion, puis sur la case de destination. Dans ce jeu, les deux joueur.euses sont derrière le même ordinateur et jouent chacun.e leur tour, en suivant les indications de tour de jeu, inscrite dans le terminal. 

Les règles sont revisitées : 
 1. Si un.e joueur.euse mange le pion de l'adversaire, il peut rejouer.
 2. Un fois arrivée au bout du plateau, un pion ne peut pas faire demi-tour (en revanche, conformément à la règle un pion peut manger en reculant).
 3. Un pion n'est jamais obligé de manger une pièce.
 4. Un.e joueur.euse ne gagne que s'il ne reste que ses pions sur le plateau.

# Réalisation du projet
A deux, nous nous sommes mis d'accord sur le format du rendu (utilisation de pygame, plateau représenté par un dictionnaire avec les coordonnées comme clé).

Roles :
 - Alexandre : règles de jeu (mouvement autorisés, etc.)
 - Joséphine : affichage avec pygame  et interaction avec joueur.euses

Difficultés :
1. Choix de la structure représentant le plateau. Première idée : créer une classe Pion avec ses coordonnées comme attribut, et faire une liste avec l'ensemble des pions. Abandonné, car il était difficile de sélectionner les pions (pour un.e joueur.euse).
2. Utilisation de pygame et keyboard incompatible. Le code ne fonctionnait pas et je (Joséphine) ne comprenais vraiment pas l'erreur. J'ai envoyé le code sur chatgpt, qui m'a expliqué quel était le problème.