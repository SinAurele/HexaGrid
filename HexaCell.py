from tools import *


class HexaCellException(Exception):
    pass

class HexaCellDefException(HexaCellException):
    def __init__(self, message = ""):
        result_message = f"Error in the definition of the cell"
        if message == "":
            result_message += "."
        else:
            result_message += " : "+message
        return super().__init__(result_message)

class HexaCell:
    class Direction:
        TOP_LEFT = 0
        LEFT = 1
        BOTTOM_LEFT = 2
        BOTTOM_RIGHT = 3
        RIGHT = 4
        TOP_RIGHT = 5
        
        string = ["top left", "left", "bottom left", "bottom right", "right", "top right"]
        @staticmethod
        def opposite(direction):
            # return la direction opposée à celle passé en paramètre
            return (direction + 3) % 6 
        
        
    
    def __init__(self, id, nextCell = None, direction = None,  value = None):
        self.id = id
        self.value = value
        self.next = [None for _ in range(6)]
        if nextCell != None :
            if direction == None:
                raise HexaCellDefException(f"You must define a direction for the next cell (id:{nextCell.id}).")
            else:
                self.place(nextCell, direction)
        
        
                
    def __str__(self):
        return str(self.id)
    
    def __repr__(self):
        return str(self)
    
    def display(self, depth = 1):
        # TODO : Affiche la case avec toutes les voisines jusqu'à une profodeur données
        raise NotImplementedError()
    
    
    def set(self, nextCell, direction):
        self.next[direction] = nextCell
        # Mise à jour de valeur voisine
        for i in range(6):
            n = self.next[i]
            if n != None:
                opp_direction = HexaCell.Direction.opposite(direction)
                n.next[opp_direction] = self
    
    def place(self, nextCell, direction, force = False):
        # Si force == True : on passe par la fonciton set qui va mettre à jour  l'ensemble
        if force == True:
            self.set(nextCell, direction)
        # On verifie que la case n'a pas déjà un voisin à cette endroit
        if self.next[direction] != None and self.next[direction] != nextCell:
            raise HexaCellDefException(f"Cell '{self.id}' already has a neighbourg in direction {HexaCell.Direction.string[direction]}")
        
        # On vérifie que la case voisine n'a pas déjà un voisin à l'opposé
        opp_direction = HexaCell.Direction.opposite(direction)
        if nextCell.next[opp_direction] != None:
            raise HexaCellDefException(f"Cell '{nextCell.id}' already has a neighbourg in direction {HexaCell.Direction.string[opp_direction]}")
        # TODO : Verifier les incohérences de case voisines. -> passer par une structure en tableau.
        self.set(nextCell, direction)