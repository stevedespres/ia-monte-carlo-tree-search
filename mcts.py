#!/usr/bin/env python
import random
import math
import hashlib
import logging
import argparse

# MCTS scalaire.
# Un grand scalaire va augmenter l'exploitation, un petit va augmenter l'exploration.
SCALAR = 1 / math.sqrt(2.0)

# Représentation du jeu
class Game():

    # Nombre de tour = profondeur de l'arbre
    NUM_TURNS = 10
    # Choix possibles ; 1, 2, 3,4,5,6
    MOVES = [0, 1, 2 ]
    # Valeur maximale
    MAX_VALUE = (5.0 * (NUM_TURNS - 1) * NUM_TURNS) / 2
    # Objectif
    GOAL = 0
    # Nombre de mouvement
    num_moves = len(MOVES)
    # Initialisation
    def __init__(self, value=0, moves=[] ,turn = NUM_TURNS):
        self.value = value
        self.moves = moves
        self.turn = turn

    # Etat suivant
    def next_state(self):
        #Choix aléatoire du mouvement
        nextmove = random.choice([x * self.turn for x in self.MOVES])
        next = Game(self.value + nextmove, self.moves + [nextmove], self.turn - 1)
        return next

    # Etat terminal du jeu
    def terminal(self):
        if self.turn == 0:
            return True
        return False

    # Calcul de la Recompense
    def reward(self):
        r = 1.0 - (abs(self.value-self.GOAL) / self.MAX_VALUE)
        return r

# Représentation d'un noeud
class Node():
    #Initialisation
    def __init__(self, state, parent=None):
        self.visits = 1
        self.reward = 0.0
        self.state = state
        self.children = []
        self.parent = parent

    # Ajout d'un noeuf enfant
    def add_child(self, child_state):
        child = Node(child_state, self)
        self.children.append(child)
    # Mise à jour du noeuf
    def update(self, reward):
        self.reward += reward
        self.visits += 1

    # Test de l'expansion de l'arbre ; retourne true lorsque l'expansion est complète
    def fully_expanded(self):
        if len(self.children) == self.state.num_moves:
            return True
        return False

    def __repr__(self):
        s = "Node; children: %d; visits: %d; reward: %f" % (len(self.children), self.visits, self.reward)
        return s

# Retourne l'arbre
def UCTSEARCH(budget, root):
    for iter in range(int(budget)):
        front = TREEPOLICY(root)
        reward = DEFAULTPOLICY(front.state)
        UPDATE(front, reward)
    return BESTCHILD(root, 0)


# Calcule le meilleur noeud enfant en calculant les UBC
def BESTCHILD(node, scalar):
    bestscore = 0.0
    bestchildren = []
    for c in node.children:
        exploit = c.reward / c.visits
        explore = math.sqrt(2.0 * math.log(node.visits) / float(c.visits))
        score = exploit + scalar * explore
        if score == bestscore:
            bestchildren.append(c)
        if score > bestscore:
            bestchildren = [c]
            bestscore = score
    return random.choice(bestchildren)

# GROWTH : Choix de la branche à explorer
def TREEPOLICY(node):
    while node.state.terminal() == False:
        if len(node.children) == 0:
            return EXPAND(node)
        elif random.uniform(0, 1) < .5:
            node = BESTCHILD(node, SCALAR)
        else:
            if node.fully_expanded() == False:
                return EXPAND(node)
            else:
                node = BESTCHILD(node, SCALAR)
    return node

# Retourne une valeur estimée d'un noeud exploré
def DEFAULTPOLICY(state):
    while state.terminal() == False:
        state = state.next_state()
    return state.reward()

# ROLL OUT : exploration
def EXPAND(node):
    tried_children = [c.state for c in node.children]
    new_state = node.state.next_state()
    while new_state in tried_children:
        new_state = node.state.next_state()
    node.add_child(new_state)
    return node.children[-1]

# UPDATE
def UPDATE(node, reward):
    while node != None:
        node.visits += 1
        node.reward += reward
        node = node.parent
    return


# Affiche les statistiques des noeuds enfants à une position donnée
def DISPLAY(node, pos):

    level = len(pos);
    current_node=node;
    rang ="Position actuelle : noeud X";

    for n in range(level):
        rang+=str(pos[n])
        current_node = current_node.children[pos[n]];
    print(rang)
    for i,c in enumerate(current_node.children):
        print(i,c)

    return

def getChildren(node, idx):

    return node.children[idx]

# Main
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='MCTS')

    args = parser.parse_args()
    # Noeud courant
    current_node = Node(Game())
    # Lancement du MCTS avec 1000 simulations
    current_node = UCTSEARCH(1000, current_node)
    POS_NODE = [0,1]
    # Affichage des statistique des noeuds enfants à la position POS_NODE
    DISPLAY(current_node, POS_NODE)
