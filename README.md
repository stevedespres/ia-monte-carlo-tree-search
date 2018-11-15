# IA_MonteCarlo

Projet d'IA : algorithme MCTS Monte Carlo, exploration d'arbres

## Dossier HEXGAME

Arène du jeu de HEX. MCTS non implémenté ; nous n'avons pas réussi à adapter notre algorithme mcts sur le joueur BOB.

## mcts.py

Algorithme MCTS fonctionnel.

Classe Game : modelise un jeu avec un nombre de tours (profondeur) et les mouvements possibles (exemple : [0,1,2]).

Classe Node : Modélise les noeuds qui compose l'arbre

Plusieurs fonctions du MCTS : UCTSEARCH, BESTCHILD, TREEPOLICY, DEFAULTPOLICY, EXPAND, UPDATE, DISPLAY
Le rôle de ces fonctions est décrit en commentaire.

Main :
Notre programme lance le MCTS sur le jeu définit, avec un nombre de simulation (1000) ; un arbre est donc créé et retourné.

Les paramètres :
Possibilité de modifier le nombre de tours et les mouvements possibles de jeu (classe Game).
Possibilité de modifier le nombre de simulation effectuer (dans le main, en parametre de UTCSEARCH) et le position du noeud à observer (POS_NODE).


La fonction DISPLAY permet d'afficher les statistiques des noeuds enfants à une position donnée.

Exemple :

POS_NODE = [0,1]

Position actuelle : noeud X01
0 Node; children: 3; visits: 21; reward: 15.897778
1 Node; children: 3; visits: 24; reward: 18.733333
2 Node; children: 3; visits: 32; reward: 27.040000

A la position [0,1] dans l'arbre, nous obtenons le nombre de visite et les rewards des noeuds enfant 010, 011 et 012.
Le meilleur choix possible est donc le noeud ayant le reward le plus élevé, soit le noeud 012.

Nous n'avons pas réussit à adapter cet algorithme sur l'arène du jeu de HEX.

## Projet secondaire

En parallèle nous sommes partit sur une autre solution avec l'éllaboration d'un arbre des coups en JSON.
Sur cette solution nous nous sommes arrêté à la création d'une classe Node et d'une classe Tree.
