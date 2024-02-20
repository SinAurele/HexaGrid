from HexaCell import *

c = HexaCell(0)
print(c)

print("Ajout de voisin")
# d = HexaCell(1, c) # Exception
d = HexaCell(1, c,HexaCell.Direction.TOP_LEFT)

print(d)
dir = HexaCell.Direction.TOP_LEFT

print(d.next[dir])
print(c.next[HexaCell.Direction.opposite(dir)])