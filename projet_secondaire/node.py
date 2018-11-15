class Node:
    """"Classe qui définit ce qu'est un noeud"""

    def __init__(self, id, children = [], nbPassage = 0, cout = 0, parent = None):
        """"Constructeur de la classe Noeud"""
        self.id = id
        self.children = children        #Tableau de noeud que compose le noeud. Ils correspondent aux différents choix possible
        self.nbPassage = nbPassage      #Nombre de passage sur le noeud
        self.cout = cout                #Valeur du noeud
        self.parent=parent

    def AddChildren(self,nbPassage,cout,parent):
        idChild = parent.id + len(parent.children)
        self.children.append(Node(idChild, [],nbPassage,cout,parent))
        while(parent != None):
            parent.Update(cout)
            parent=parent.parent


    def Update(self,cout):
        self.cout+=cout
        self.nbPassage += 1

    def ToString(self) :
        print("Node :" , self)
        print("--- Cout / nombre de passage :" , self.cout , " / " , self.nbPassage)
        print("--- Children :")
        for c in self.children:
            print("# ", c.ToString())

class Tree:
    """"Classe qui définit ce qu'est un arbre"""
    def __init__(self):
        self.nodes = []
        self.cout = 0
        self.nbPassage = 0

    def AddNode(self, node):
        self.nodes.append(node)

