from copy import deepcopy
from random import shuffle

class Block:

    def __init__(self, x, y, color, size, empty=0):
        self.x = x
        self.y = y
        self.color = color
        self.size = size
        self.empty = empty

class Piece:

    def __init__(self, shape, rotation_state, color, name):
        self.name = name

        #   create a piece based on the nxm binary matrix given
        for i, line in enumerate(shape):
            for j, cell in enumerate(line):
                if cell:
                    shape[i][j] = Block(j+3, i, color, 25)
                else:
                    shape[i][j] = Block(j+3, i, (0,0,0),25, 1)
                
        self.shape = shape
        
        self.rotation_state = rotation_state

# retorna uma lista com todas as peças em ordem aleatória

def create_piece_list():

    pieces = [deepcopy(letter) for letter in PIECES.values()]

    shuffle(pieces)

    return pieces

# todas as 7 peças

I = Piece([[0,0,0,0],
           [1,1,1,1],
           [0,0,0,0],
           [0,0,0,0]],
           0, (0,   255, 255), "I")    # aqua

O = Piece([[1,1],
           [1,1]],
           0, (255, 255, 0), "O")    # yellow

T = Piece([[0,1,0],
           [1,1,1],
           [0,0,0]], 
           0, (128, 0, 128), "T")    # purple

S = Piece([[1,1,0],
           [0,1,1],
           [0,0,0]],
           0, (255, 0, 0), "S")    # lime

Z = Piece([[0,1,1],
           [1,1,0],
           [0,0,0]], 
           0, (0,   255,   0), "Z")    # red

J = Piece([[1,0,0],
           [1,1,1],
           [0,0,0]], 
           0, (0,   0,   255), "J")    # blue

L = Piece([[0,0,1],
           [1,1,1],
           [0,0,0]], 
           0, (255, 127, 0), "L")    # orange

PIECES = {"I":I,"O":O,"T":T,"S":S,"Z":Z,"J":J,"L":L}